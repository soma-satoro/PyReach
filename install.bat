@echo off
REM PyReach Installation Script (Windows)
REM Usage: install.bat

echo ================================================
echo   PyReach - Evennia MUD Installation
echo ================================================
echo.

REM Check Python
echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found in PATH
    echo Please install Python 3.11+ from https://www.python.org/
    pause
    exit /b 1
)
echo [OK] Python found
echo.

REM Create virtual environment
echo Creating virtual environment...
if not exist env (
    python -m venv env
    echo [OK] Virtual environment created
) else (
    echo [SKIP] Virtual environment already exists
)
echo.

REM Activate virtual environment
echo Activating virtual environment...
call env\Scripts\activate.bat
echo [OK] Virtual environment activated
echo.

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip --quiet
echo [OK] Pip upgraded
echo.

REM Install requirements
echo Installing Python dependencies...
echo This may take several minutes...
pip install -r requirements.txt
echo [OK] Dependencies installed
echo.

REM Navigate to PyReach
cd PyReach

REM Run migrations
echo Setting up database...
python ..\env\Scripts\evennia migrate
echo [OK] Database migrations complete
echo.

REM Create superuser
echo.
echo Create Superuser Account
echo ========================
echo You'll need an admin account to manage your game.
set /p CREATE_SUPER="Create superuser now? (y/n): "
if /i "%CREATE_SUPER%"=="y" (
    python ..\env\Scripts\evennia createsuperuser
)
echo.

REM Collect static files
echo Collecting static files...
python ..\env\Scripts\evennia collectstatic --noinput
echo [OK] Static files collected
echo.

REM Seed wiki
echo.
set /p SEED_WIKI="Seed wiki with sample content? (y/n): "
if /i "%SEED_WIKI%"=="y" (
    python ..\env\Scripts\evennia seed_wiki
    echo [OK] Wiki seeded
)
echo.

REM Final instructions
echo.
echo ================================================
echo   Installation Complete!
echo ================================================
echo.
echo To start PyReach:
echo   cd PyReach
echo   ..\env\Scripts\evennia start
echo.
echo Access your game:
echo   Web Interface: http://localhost:4001/
echo   Wiki: http://localhost:4001/wiki/
echo   Telnet: localhost:4000
echo   Webclient: http://localhost:4001/webclient/
echo.
echo Useful commands:
echo   evennia stop     - Stop the server
echo   evennia restart  - Restart the server
echo   evennia reload   - Reload code (keeps connections)
echo.
echo Remember to configure server settings in:
echo   PyReach\server\conf\settings.py
echo.
pause

