#!/bin/bash
# PyReach Installation Script (Linux/Mac)
# Usage: ./install.sh

set -e  # Exit on error

echo "================================================"
echo "  PyReach - Evennia MUD Installation"
echo "================================================"
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check Python version
echo -e "${BLUE}Checking Python version...${NC}"
if command -v python3 &> /dev/null; then
    python_version=$(python3 --version 2>&1 | grep -oP '\d+\.\d+')
    required_version="3.11"
    
    if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then 
        echo -e "${YELLOW}Warning: Python 3.11+ recommended. You have Python $python_version${NC}"
    else
        echo -e "${GREEN}✓ Python $python_version detected${NC}"
    fi
else
    echo -e "${RED}Error: Python 3 not found${NC}"
    exit 1
fi

# Create virtual environment
echo -e "\n${BLUE}Creating virtual environment...${NC}"
if [ ! -d "env" ]; then
    python3 -m venv env
    echo -e "${GREEN}✓ Virtual environment created${NC}"
else
    echo -e "${YELLOW}Virtual environment already exists${NC}"
fi

# Activate virtual environment
echo -e "\n${BLUE}Activating virtual environment...${NC}"
source env/bin/activate
echo -e "${GREEN}✓ Virtual environment activated${NC}"

# Upgrade pip
echo -e "\n${BLUE}Upgrading pip...${NC}"
pip install --upgrade pip --quiet
echo -e "${GREEN}✓ Pip upgraded${NC}"

# Install requirements
echo -e "\n${BLUE}Installing Python dependencies...${NC}"
echo "This may take several minutes..."
if [ -f "PyReach/requirements.txt" ]; then
    pip install -r PyReach/requirements.txt
elif [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo -e "${RED}Error: requirements.txt not found${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Dependencies installed${NC}"

# Fix typeclass inheritance issues
echo -e "\n${BLUE}Fixing typeclass files...${NC}"
python3 fix_typeclasses.py
echo -e "${GREEN}✓ Typeclass files checked${NC}"

# Navigate to PyReach directory
cd PyReach

# Run migrations
echo -e "\n${BLUE}Setting up database...${NC}"
../env/bin/evennia migrate
echo -e "${GREEN}✓ Database migrations complete${NC}"

# Collect static files
echo -e "\n${BLUE}Collecting static files...${NC}"
../env/bin/evennia collectstatic --noinput --quiet
echo -e "${GREEN}✓ Static files collected${NC}"

# Seed wiki
echo -e "\n${BLUE}Seed wiki with sample content?${NC}"
echo "This creates sample categories and pages you can customize later."
read -p "Seed wiki? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    ../env/bin/evennia seed_wiki
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓ Wiki seeded with sample content${NC}"
    else
        echo -e "${YELLOW}⚠ Wiki seeding failed - you can run 'evennia seed_wiki' manually later${NC}"
    fi
else
    echo -e "${YELLOW}⚠ Wiki seeding skipped${NC}"
fi

# Final instructions
echo ""
echo "================================================"
echo -e "${GREEN}  Installation Complete!${NC}"
echo "================================================"
echo ""
echo -e "${BLUE}NEXT STEP: Start Evennia${NC}"
echo "========================"
echo ""
echo "Run this command to start PyReach:"
echo "  ../env/bin/evennia start"
echo ""
echo -e "${YELLOW}On first start, Evennia will prompt you to create a superuser account.${NC}"
echo "This is your main admin account - choose a secure password!"
echo ""
echo "After starting, access your game:"
echo "  Web Interface: http://localhost:4001/"
echo "  Wiki:          http://localhost:4001/wiki/"
echo "  Webclient:     http://localhost:4001/webclient/"
echo "  Telnet:        localhost:4000"
echo ""
echo "Useful commands (run from PyReach directory):"
echo "  evennia start    - Start the server"
echo "  evennia stop     - Stop the server"
echo "  evennia restart  - Restart the server"
echo "  evennia reload   - Reload code (keeps connections)"
echo "  evennia status   - Check if server is running"
echo ""
echo "Configuration:"
echo "  Game settings: server/conf/settings.py"
echo "  Change game name: Edit SERVERNAME in settings.py"
echo ""
echo "Documentation:"
echo "  ../README.md        - Main documentation"
echo "  ../QUICKSTART.md    - Quick start guide"
echo "  Wiki guides in root directory"
echo ""
echo "================================================"
echo -e "${GREEN}Ready to start? Run: ../env/bin/evennia start${NC}"
echo "================================================"
echo ""

# Deactivate virtual environment
deactivate

