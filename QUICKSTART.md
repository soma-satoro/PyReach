# PyReach Quick Start Guide

Get PyReach up and running in minutes!

## 🚀 Installation (5 minutes)

### Linux/Mac

```bash
# Clone repository
git clone <your-repo-url> pyreach
cd pyreach

# Run installation script
chmod +x install.sh
./install.sh

# Start Evennia
cd PyReach
../env/bin/evennia start
```

### Windows

```bash
# Clone repository
git clone <your-repo-url> pyreach
cd pyreach

# Run installation script
install.bat

# Start Evennia
cd PyReach
..\env\Scripts\evennia start
```

## 🌐 Access Your Game

Once Evennia starts, access your game:

- **Homepage**: http://localhost:4001/
- **Wiki**: http://localhost:4001/wiki/
- **Play in Browser**: http://localhost:4001/webclient/
- **Admin Panel**: http://localhost:4001/admin/
- **Telnet**: localhost:4000

## 🎮 First Steps

### 1. Create Your First Character (2 minutes)

1. Go to http://localhost:4001/webclient/
2. If you created a superuser during install:
   - Login with those credentials
3. If not:
   - Click "Register" to create an account
   - Or type `create <username> <password>` to register via telnet
4. Type `charcreate <name>` to create your first character
5. Start playing!

### 2. Set Up the Wiki (5 minutes)

1. Log in to the admin panel: http://localhost:4001/admin/
2. Or run the seed command:
   ```bash
   cd PyReach
   ../env/bin/evennia seed_wiki  # Linux/Mac
   ..\env\Scripts\evennia seed_wiki  # Windows
   ```
3. Visit http://localhost:4001/wiki/
4. Create your first wiki page!

### 3. Customize Your Game (10 minutes)

Edit `PyReach/server/conf/settings.py`:

```python
# Change game name
SERVERNAME = "My Awesome Game"

# Adjust settings as needed
CLIENT_DEFAULT_WIDTH = 80
```

Then reload:
```bash
cd PyReach
../env/bin/evennia reload  # Linux/Mac
..\env\Scripts\evennia reload  # Windows
```

## 📝 Essential Commands

### Server Management

```bash
evennia start     # Start the server
evennia stop      # Stop the server
evennia restart   # Restart the server
evennia reload    # Reload code (keeps players connected)
evennia status    # Check if running
```

### Development

```bash
evennia migrate          # Run database migrations
evennia makemigrations   # Create new migrations
evennia collectstatic    # Collect CSS/JS files
evennia shell            # Django shell
evennia test             # Run tests
```

### In-Game Commands (as superuser)

```
@reload          - Reload server code
@py              - Execute Python code
@objects         - List all objects
@accounts        - List all accounts
help             - Show help system
look             - Look at current location
```

## 🎨 Wiki Quick Start

### Create a Category

1. Log in as staff
2. Go to http://localhost:4001/wiki/category/create/
3. Fill in:
   - **Name**: "Setting" (or "Rules", "Factions", etc.)
   - **Icon**: `fa-globe` (or `fa-book`, `fa-users`, etc.)
   - **Order**: 0 (lower = displayed first)
4. Click "Create Category"

### Create a Page

1. Click "New Page" in wiki navigation
2. Fill in:
   - **Title**: Your page title
   - **Category**: Select from dropdown
   - **Content**: Write using Markdown
   - **Featured**: Check to show on wiki home
3. Click "Preview" to see how it looks
4. Click "Create Page"

### Markdown Basics

```markdown
# Heading 1
## Heading 2

**Bold text**
*Italic text*

- Bullet list
1. Numbered list

[Link](http://example.com)
```

## 🔐 Permissions

### Grant Wiki Editing

**Via Admin Panel:**
1. Go to http://localhost:4001/admin/auth/user/
2. Select user
3. Add permission: "wiki | wiki page | Can edit wiki pages"
4. Save

**Via Evennia Shell:**
```bash
evennia shell
```
```python
from django.contrib.auth.models import User, Permission
user = User.objects.get(username='playername')
perm = Permission.objects.get(codename='can_edit_wiki')
user.user_permissions.add(perm)
user.save()
```

## 🛠️ Troubleshooting

### Server Won't Start

```bash
# Check for errors
cd PyReach
../env/bin/evennia status
tail -50 server/logs/server.log

# Clear cache
find . -name "*.pyc" -delete
find . -type d -name "__pycache__" -delete

# Try again
../env/bin/evennia start
```

### CSS Not Loading

```bash
cd PyReach
../env/bin/evennia collectstatic --noinput
../env/bin/evennia reload
```

### Database Errors

```bash
cd PyReach
../env/bin/evennia migrate
```

### Wiki Not Working

```bash
cd PyReach
../env/bin/evennia migrate wiki
../env/bin/evennia collectstatic --noinput
../env/bin/evennia restart
```

## 📚 Documentation

- **README.md** - Project overview
- **DEPLOYMENT.md** - Production deployment guide
- **CONTRIBUTING.md** - Developer guidelines
- **CHANGELOG.md** - Version history
- **WIKI_INSTALLATION_SUMMARY.md** - Wiki setup
- **WEBSITE_THEME_GUIDE.md** - Theme customization

## 🎯 Next Steps

After getting started:

1. **Customize Settings** - Edit `settings.py` for your game
2. **Create Wiki Content** - Build your game's lore
3. **Build Your World** - Create rooms and areas
4. **Configure Systems** - Set up templates, factions, etc.
5. **Invite Players** - Share your game!

## 💡 Tips

- **Start Small**: Get the basics working before adding complexity
- **Test Often**: `evennia reload` to test changes quickly
- **Use the Wiki**: Document your world as you build it
- **Read Evennia Docs**: https://www.evennia.com/docs/
- **Join Discord**: Get help from the Evennia community

## 🎉 You're Ready!

PyReach is now installed and ready to use. Start building your gothic-punk MUD and create an amazing world for your players!

---

**Need help?** Check the documentation or visit the Evennia Discord: https://discord.gg/AJJpcRUhtF

*May the shadows guide your path.* 🦇✨

