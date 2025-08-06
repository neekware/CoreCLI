#!/bin/bash
# Test GitHub Actions locally with act
# Requires: brew install act (on macOS) or see https://github.com/nektos/act

set -e

echo "🐳 Testing GitHub Actions locally with act..."

# Check if act is installed
if ! command -v act &> /dev/null; then
    echo "❌ 'act' is not installed. Please install it first:"
    echo "   macOS: brew install act"
    echo "   Linux: curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash"
    exit 1
fi

# Check if Docker is running
if ! docker info &> /dev/null; then
    echo "❌ Docker is not running. Please start Docker Desktop."
    exit 1
fi

echo "✅ Prerequisites checked"

# Create act config if it doesn't exist
if [ ! -f ~/.actrc ]; then
    echo "📝 Creating default act configuration..."
    cat > ~/.actrc << EOF
-P ubuntu-latest=catthehacker/ubuntu:act-latest
-P ubuntu-22.04=catthehacker/ubuntu:act-22.04
-P ubuntu-20.04=catthehacker/ubuntu:act-20.04
-P ubuntu-18.04=catthehacker/ubuntu:act-18.04
EOF
fi

# Test the quick test workflow
echo ""
echo "🧪 Testing Quick Test workflow..."
echo "================================"

# Run with Python 3.11 only for faster testing
act push \
    --job quick-test \
    --matrix python-version:3.11 \
    --workflows .github/workflows/test.yml \
    -v

echo ""
echo "✅ Act testing complete!"
echo ""
echo "💡 Tips:"
echo "   - To test all Python versions: act push --workflows .github/workflows/test.yml"
echo "   - To test CI workflow: act push --workflows .github/workflows/ci.yml"
echo "   - To see what would run: act -l"
echo "   - For debugging: act -v --container-architecture linux/amd64"