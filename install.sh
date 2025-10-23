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
NC='\033[0m' # No Color

# Check Python version
echo -e "${BLUE}Checking Python version...${NC}"
python_version=$(python3 --version 2>&1 | grep -oP '\d+\.\d+')
required_version="3.11"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then 
    echo -e "${YELLOW}Warning: Python 3.11+ recommended. You have Python $python_version${NC}"
else
    echo -e "${GREEN}✓ Python $python_version detected${NC}"
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
pip install -r requirements.txt
echo -e "${GREEN}✓ Dependencies installed${NC}"

# Navigate to PyReach directory
cd PyReach

# Run migrations
echo -e "\n${BLUE}Setting up database...${NC}"
python ../env/bin/evennia migrate
echo -e "${GREEN}✓ Database migrations complete${NC}"

# Create superuser
echo -e "\n${BLUE}Create superuser account${NC}"
echo "You'll need to create an admin account to manage your game."
read -p "Create superuser now? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    python ../env/bin/evennia createsuperuser
fi

# Collect static files
echo -e "\n${BLUE}Collecting static files...${NC}"
python ../env/bin/evennia collectstatic --noinput --quiet
echo -e "${GREEN}✓ Static files collected${NC}"

# Seed wiki
echo -e "\n${BLUE}Seed wiki with sample content?${NC}"
read -p "This creates sample categories and pages (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    python ../env/bin/evennia seed_wiki
    echo -e "${GREEN}✓ Wiki seeded with sample content${NC}"
fi

# Final instructions
echo ""
echo "================================================"
echo -e "${GREEN}  Installation Complete!${NC}"
echo "================================================"
echo ""
echo "To start PyReach:"
echo "  cd PyReach"
echo "  ../env/bin/evennia start"
echo ""
echo "Access your game:"
echo "  Web Interface: http://localhost:4001/"
echo "  Wiki: http://localhost:4001/wiki/"
echo "  Telnet: localhost:4000"
echo "  Webclient: http://localhost:4001/webclient/"
echo ""
echo "Useful commands:"
echo "  evennia stop     - Stop the server"
echo "  evennia restart  - Restart the server"
echo "  evennia reload   - Reload code (keeps connections)"
echo ""
echo -e "${YELLOW}Remember to configure your server settings in:${NC}"
echo "  PyReach/server/conf/settings.py"
echo ""

# Deactivate virtual environment
deactivate

