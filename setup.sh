#!/bin/bash
# Shaypoor Bootstrap Script
# Sets up Python virtual environment and installs the cli

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_DIR="$SCRIPT_DIR/.venv"
AUTO_YES=false

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -y|--yes)
            AUTO_YES=true
            shift
            ;;
        *)
            echo "Usage: $0 [-y|--yes]"
            echo "  -y, --yes    Auto-confirm all prompts"
            exit 1
            ;;
    esac
done

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

log() {
    echo -e "${GREEN}✓${NC} $1"
}

warn() {
    echo -e "${YELLOW}⚠${NC} $1"
}

error() {
    echo -e "${RED}✗${NC} $1"
    exit 1
}

ask() {
    if [[ "$AUTO_YES" == true ]]; then
        return 0
    fi
    
    local prompt="$1"
    local default="${2:-y}"
    
    echo -e "${BLUE}?${NC} $prompt (${default}/n): "
    read -r response
    response=${response:-$default}
    
    [[ "$response" =~ ^[Yy] ]]
}

# Check Python version
check_python() {
    if command -v python3 >/dev/null 2>&1; then
        PYTHON_CMD=python3
    elif command -v python >/dev/null 2>&1; then
        PYTHON_CMD=python
    else
        error "Python not found. Please install Python 3.9+"
    fi
    
    # Check version
    PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | cut -d' ' -f2)
    PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
    PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)
    
    if [ "$PYTHON_MAJOR" -lt 3 ] || [ "$PYTHON_MAJOR" -eq 3 -a "$PYTHON_MINOR" -lt 9 ]; then
        error "Python 3.9+ required, found $PYTHON_VERSION"
    fi
    
    log "Found Python $PYTHON_VERSION"
}

# Create virtual environment
create_venv() {
    if [[ -d "$VENV_DIR" ]]; then
        if ask "Virtual environment already exists. Recreate?"; then
            log "Moving existing virtual environment to temp..."
            
            # Move to temp with unique name and remove in background
            local temp_dir="/tmp/shaypoor-venv-$$-$(date +%s)"
            mv "$VENV_DIR" "$temp_dir"
            
            # Remove in background
            (rm -rf "$temp_dir" 2>/dev/null) &
            
            log "Old virtual environment moved to temp, removal running in background"
        else
            log "Using existing virtual environment"
            return 0
        fi
    fi
    
    log "Creating virtual environment in $VENV_DIR..."
    sleep 1.0 && $PYTHON_CMD -m venv "$VENV_DIR"
    
    # Verify venv was created
    if [[ ! -f "$VENV_DIR/bin/activate" ]]; then
        error "Virtual environment creation failed"
    fi
    
    log "Virtual environment created"
}

# Install dependencies
install_deps() {
    log "Activating virtual environment and installing dependencies..."
    
    source "$VENV_DIR/bin/activate"
    pip install --upgrade pip setuptools wheel
    
    # Configure pip to use temp directory for build artifacts
    export PIP_BUILD=/tmp/pip-build-$$
    
    # Install the package in editable mode with dev dependencies
    log "Installing dependencies..."
    pip install --no-build-isolation -e ".[dev]"
    
    # Clean up any egg-info that might have been created in project root
    rm -rf "$SCRIPT_DIR"/*.egg-info
    
    log "Dependencies installed successfully"
    
    # Install pre-commit hooks
    log "Installing pre-commit hooks..."
    pre-commit install
    log "Pre-commit hooks installed"
}

# Install cli
install_cli() {
    log "Installing cli..."
    
    # Copy the wrapper script to venv
    cp "$SCRIPT_DIR/commandline/bin/cli-venv" "$VENV_DIR/bin/cli"
    chmod +x "$VENV_DIR/bin/cli"
    
    # Install project root version (auto-activates)
    cp "$SCRIPT_DIR/commandline/bin/cli-project" "$SCRIPT_DIR/cli"
    chmod +x "$SCRIPT_DIR/cli"
    
    log "cli installed"
}


# Main execution
main() {
    echo -e "${BLUE}🚀 Shaypoor Bootstrap${NC}"
    echo "Setting up Python environment for Shaypoor TTS..."
    echo
    
    check_python
    create_venv
    install_deps
    install_cli
    
    echo
    log "Bootstrap complete!"
    echo -e "${GREEN}To activate the environment:${NC} source $VENV_DIR/bin/activate"
    echo -e "${GREEN}To test the setup:${NC}"
    echo "  ./cli --help                        # Show help (auto-activates venv)"
    echo "  ./cli --version                     # Show version"
    echo "  cli --help                          # Show help (with venv activated)"
    echo
    echo -e "${YELLOW}Remember to activate the environment first: source .venv/bin/activate${NC}"
}

main "$@"