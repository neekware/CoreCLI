#!/bin/bash
# Test the CLI in Docker containers (simulates CI environment)

set -e

echo "🐳 Testing ehAye™ Core CLI in Docker..."
echo "========================================"

# Check if Docker is installed and running
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker Desktop."
    exit 1
fi

if ! docker info &> /dev/null; then
    echo "❌ Docker is not running. Please start Docker Desktop."
    exit 1
fi

# Parse arguments
TEST_TYPE="${1:-quick}"
PYTHON_VERSION="${2:-3.11}"

case "$TEST_TYPE" in
    quick)
        echo "🚀 Running quick test..."
        docker-compose -f docker-compose.test.yml run --rm quick-test
        ;;
    
    full)
        echo "🧪 Running full test suite on all Python versions..."
        docker-compose -f docker-compose.test.yml up --build --exit-code-from test-py39 test-py39
        docker-compose -f docker-compose.test.yml up --build --exit-code-from test-py311 test-py311
        docker-compose -f docker-compose.test.yml up --build --exit-code-from test-py313 test-py313
        ;;
    
    single)
        echo "🎯 Testing with Python $PYTHON_VERSION..."
        # Build custom Dockerfile with specific Python version
        cat > Dockerfile.test.tmp << EOF
FROM python:${PYTHON_VERSION}-slim

RUN apt-get update && apt-get install -y git gcc && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . .
RUN pip install --upgrade pip setuptools wheel && pip install -e '.[dev]'
RUN cli --version
CMD ["cli", "dev", "all"]
EOF
        
        docker build -f Dockerfile.test.tmp -t ehaye-cli-test:py${PYTHON_VERSION} .
        docker run --rm ehaye-cli-test:py${PYTHON_VERSION}
        rm Dockerfile.test.tmp
        ;;
    
    shell)
        echo "🐚 Starting interactive shell in test container..."
        docker-compose -f docker-compose.test.yml run --rm quick-test bash
        ;;
    
    *)
        echo "Usage: $0 [quick|full|single|shell] [python-version]"
        echo ""
        echo "Examples:"
        echo "  $0 quick           # Quick test with Python 3.11"
        echo "  $0 full            # Test all Python versions"
        echo "  $0 single 3.9      # Test with Python 3.9"
        echo "  $0 shell           # Interactive shell in container"
        exit 1
        ;;
esac

echo ""
echo "✅ Docker testing complete!"