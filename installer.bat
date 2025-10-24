@echo off
REM PyReach Installation Script (Windows)
REM Usage: installer.bat

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
python --version
echo [OK] Python found
echo.

REM Create virtual environment
echo Creating virtual environment...
if not exist env (
    python -m venv env
    if errorlevel 1 (
        echo [ERROR] Failed to create virtual environment
        pause
        exit /b 1
    )
    echo [OK] Virtual environment created
) else (
    echo [SKIP] Virtual environment already exists
)
echo.

REM Activate virtual environment
echo Activating virtual environment...
call env\Scripts\activate.bat
if errorlevel 1 (
    echo [ERROR] Failed to activate virtual environment
    pause
    exit /b 1
)
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
if exist PyReach\requirements.txt (
    pip install -r PyReach\requirements.txt
) else if exist requirements.txt (
    pip install -r requirements.txt
) else (
    echo [ERROR] requirements.txt not found!
    pause
    exit /b 1
)
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)
echo [OK] Dependencies installed
echo.

REM Fix typeclass inheritance issues
echo Fixing typeclass files...
python fix_typeclasses.py
echo [OK] Typeclass files checked
echo.

REM Navigate to PyReach
cd PyReach

REM Run migrations
echo Setting up database...
call ..\env\Scripts\evennia.bat migrate
if errorlevel 1 (
    echo [ERROR] Database migration failed
    echo.
    echo This might be because:
    echo - PyReach directory doesn't contain server/conf/settings.py
    echo - Database configuration is incorrect
    echo.
    echo Try running manually:
    echo   cd PyReach
    echo   evennia migrate
    pause
    exit /b 1
)
echo [OK] Database migrations complete
echo.

REM Collect static files
echo Collecting static files...
call ..\env\Scripts\evennia.bat collectstatic --noinput
if errorlevel 1 (
    echo [WARN] Failed to collect static files
    echo You can run this manually later: evennia collectstatic --noinput
) else (
    echo [OK] Static files collected
)
echo.

REM Seed wiki
echo.
echo ================================================
echo Seed Wiki
echo ================================================
echo Would you like to create sample wiki categories and pages?
echo This will populate your wiki with example content you can customize.
echo.
set /p SEED_WIKI="Seed wiki with sample content? (y/n): "
if /i "%SEED_WIKI%"=="y" (
    call ..\env\Scripts\evennia.bat seed_wiki
    if errorlevel 1 (
        echo [WARN] Failed to seed wiki
        echo You can run this manually later: evennia seed_wiki
    ) else (
        echo [OK] Wiki seeded with sample content
    )
) else (
    echo [SKIP] Wiki seeding skipped
)
echo.

REM Final instructions
echo.
echo ================================================
echo   Installation Complete!
echo ================================================
echo.
echo NEXT STEP: Start Evennia
echo ========================
echo.
echo Run this command to start PyReach:
echo   evennia start
echo.
echo On first start, Evennia will prompt you to create a superuser account.
echo This is your main admin account - choose a secure password!
echo.
echo After starting, access your game:
echo   Web Interface: http://localhost:4001/
echo   Wiki:          http://localhost:4001/wiki/
echo   Webclient:     http://localhost:4001/webclient/
echo   Telnet:        localhost:4000
echo.
echo Useful commands:
echo   evennia start    - Start the server
echo   evennia stop     - Stop the server
echo   evennia restart  - Restart the server
echo   evennia reload   - Reload code (keeps connections)
echo   evennia status   - Check if server is running
echo.
echo Configuration:
echo   Game settings: server\conf\settings.py
echo   Change game name: Edit SERVERNAME in settings.py
echo.
echo Documentation:
echo   ..\README.md        - Main documentation
echo   ..\QUICKSTART.md    - Quick start guide
echo   Wiki guides in parent directory
echo.
echo ================================================
echo Ready to start? Run: evennia start
echo ================================================
echo.
pause

