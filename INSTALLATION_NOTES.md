# PyReach Installation Notes

## ✅ Installation Process

The installation process has been streamlined to match Evennia's workflow:

### Step 1: Run Installer

**Linux/Mac:**
```bash
chmod +x install.sh
./install.sh
```

**Windows:**
```bash
installer.bat
```

This will:
- Create virtual environment
- Install all dependencies
- Run database migrations
- Collect static files
- Optionally seed wiki

### Step 2: Start Evennia

```bash
cd PyReach
../env/bin/evennia start      # Linux/Mac
..\env\Scripts\evennia start  # Windows
```

### Step 3: Create Superuser

**On first start**, Evennia will automatically prompt:

```
Create a superuser below. The superuser is Account #1, the 'owner' account of the server.

Username: youradmin
Email address: admin@example.com (or leave blank)
Password: 
Password (again):
Superuser created successfully.
```

This only happens the first time you start Evennia. After that, you can create additional superusers with:

```bash
evennia createsuperuser
```

## 🎯 What Installer Does

### Automated Steps:
1. ✅ Check Python installation
2. ✅ Create virtual environment (`env/`)
3. ✅ Install all dependencies from `requirements.txt`
4. ✅ Run database migrations (`evennia migrate`)
5. ✅ Collect static files (`evennia collectstatic`)
6. ✅ Optionally seed wiki content

### Manual Steps (First Start):
- 🔑 Create superuser account (prompted automatically)
- 🚀 Start playing!

## 📝 Post-Installation

### Verify Installation

```bash
cd PyReach

# Check if evennia is installed
evennia --version

# Check database
evennia dbshell
# Type \q to exit (PostgreSQL) or .quit (SQLite)

# Check static files
ls server/.static/  # Linux/Mac
dir server\.static\  # Windows
```

### Access Your Game

After `evennia start`, visit:

- **Homepage**: http://localhost:4001/
- **Wiki**: http://localhost:4001/wiki/
- **Webclient**: http://localhost:4001/webclient/
- **Admin**: http://localhost:4001/admin/
- **Telnet**: localhost:4000

## 🔧 Manual Installation (If Installer Fails)

If the installer doesn't work, run these commands manually:

**Linux/Mac:**
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
cd PyReach
evennia migrate
evennia collectstatic --noinput
evennia seed_wiki  # optional
evennia start
```

**Windows:**
```bash
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
cd PyReach
evennia migrate
evennia collectstatic --noinput
evennia seed_wiki  # optional
evennia start
```

## ⚙️ Configuration

### Before First Start (Optional)

Edit `PyReach/server/conf/settings.py`:

```python
# Change game name (appears on website and wiki)
SERVERNAME = "My Game Name"

# Adjust default width
CLIENT_DEFAULT_WIDTH = 80

# Add/remove installed apps
INSTALLED_APPS += [
    # Your custom apps
]
```

### After First Start

1. Log in to admin: http://localhost:4001/admin/
2. Configure game settings
3. Create wiki content
4. Set up permissions
5. Build your world!

## 🗄️ Database Options

### SQLite (Default - Development)

No configuration needed. Database file created automatically at:
- `PyReach/server/evennia.db3`

**Pros:** Easy, no setup
**Cons:** Limited concurrency, not for production

### PostgreSQL (Recommended - Production)

Create `PyReach/server/conf/secret_settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pyreach_db',
        'USER': 'pyreach_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Then run:
```bash
evennia migrate
```

## 📦 Dependencies Installed

Core packages:
- `evennia` (4.5.0+) - MUD framework
- `django` (4.x) - Web framework
- `twisted` (23.x) - Networking
- `markdown` (3.x) - Markdown processing
- `Pillow` (10.x+) - Image handling

Development tools:
- `black` - Code formatter
- `isort` - Import sorter

Optional:
- `psycopg2-binary` - PostgreSQL driver
- `python-dateutil` - Date utilities
- `pytz` - Timezone support

## 🚨 Common Issues

### "evennia: command not found"

**Solution:**
```bash
# Make sure virtual environment is activated
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
```

### "secret_settings.py file not found"

**This is normal!** The message appears but doesn't cause errors.

Create the file if you need to override settings:
```bash
touch PyReach/server/conf/secret_settings.py
```

### Migration Errors

If migrations fail:
```bash
cd PyReach
evennia migrate --fake-initial
```

### Static Files Not Loading

```bash
cd PyReach
evennia collectstatic --noinput --clear
evennia reload
```

### Port Already in Use

Change ports in `settings.py`:
```python
TELNET_PORTS = [4000]  # Change to different port
WEBSERVER_PORTS = [(4001, 4005)]  # Change to different ports
```

## 📚 Next Steps

After installation:

1. **Start the server**: `evennia start`
2. **Create superuser**: Prompted on first start
3. **Visit the website**: http://localhost:4001/
4. **Explore the wiki**: http://localhost:4001/wiki/
5. **Read the docs**: Check all .md files

## 🎓 Learning Resources

**In the repository:**
- `README.md` - Project overview
- `QUICKSTART.md` - 5-minute guide
- `DEPLOYMENT.md` - Production setup
- `CONTRIBUTING.md` - Developer guide

**Online:**
- Evennia Docs: https://www.evennia.com/docs/
- Evennia Discord: https://discord.gg/AJJpcRUhtF
- Django Docs: https://docs.djangoproject.com/

---

**Installation complete! Time to build your world.** 🦇✨

