# Git Setup Guide for PyReach

Complete guide to setting up version control for your PyReach installation.

## Initial Git Setup

### 1. Initialize Git Repository

If you haven't already initialized git:

```bash
cd /path/to/pyreach  # or c:\exordium on Windows
git init
```

### 2. Configure Git

```bash
# Set your name and email
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Optional: Set default branch name
git config init.defaultBranch main
```

### 3. Add Files

The `.gitignore` file is already configured to exclude:
- Virtual environment (`env/`)
- Database files (`*.db3`)
- Log files (`*.log`)
- Python cache (`__pycache__/`)
- Secret settings (`secret_settings.py`)
- Generated files (`.static/`, `media/`)

**Add all files:**

```bash
git add .
git commit -m "Initial commit: PyReach with wiki system"
```

## Remote Repository Setup

### Option 1: GitHub

1. Create a new repository on GitHub
2. **Don't** initialize with README (we already have one)
3. Connect your local repo:

```bash
git remote add origin https://github.com/yourusername/pyreach.git
git branch -M main
git push -u origin main
```

### Option 2: GitLab

```bash
git remote add origin https://gitlab.com/yourusername/pyreach.git
git branch -M main
git push -u origin main
```

### Option 3: Self-Hosted (Gitea, Gogs, etc.)

```bash
git remote add origin https://your-git-server.com/yourusername/pyreach.git
git branch -M main
git push -u origin main
```

## Branch Strategy

### Recommended Workflow

**main** - Stable, production-ready code
**develop** - Development branch
**feature/*** - Feature branches
**hotfix/*** - Emergency fixes

### Creating Feature Branches

```bash
# Start a new feature
git checkout main
git pull
git checkout -b feature/new-vampire-powers

# Work on your feature
# ... make changes ...

# Commit changes
git add .
git commit -m "feat: Add vampire feeding mechanics"

# Push to remote
git push origin feature/new-vampire-powers

# Create Pull Request on GitHub/GitLab
```

## Daily Workflow

### Making Changes

```bash
# Check status
git status

# See what changed
git diff

# Stage specific files
git add PyReach/commands/vampire_commands.py
git add PyReach/world/wiki/pages/vampires.md

# Or stage everything
git add .

# Commit with message
git commit -m "fix: Correct vitae spending calculation"

# Push to remote
git push
```

### Pulling Updates

```bash
# Pull latest changes from main
git checkout main
git pull origin main

# Update your feature branch
git checkout feature/your-feature
git merge main

# Or use rebase (cleaner history)
git rebase main
```

## Deployment Workflow

### Development → Production

```bash
# On development server
git add .
git commit -m "feat: Add new wiki pages"
git push origin main

# On production server
cd /home/pyreach/pyreach
git pull origin main
source env/bin/activate
cd PyReach
evennia migrate
evennia collectstatic --noinput
evennia reload
```

### Using Tags for Releases

```bash
# Tag a release
git tag -a v1.1.0 -m "Release v1.1.0: Wiki system"
git push origin v1.1.0

# List tags
git tag

# Checkout a specific version
git checkout v1.1.0
```

## Important Files

### Tracked by Git

✅ **Application Code:**
- `PyReach/commands/` - Game commands
- `PyReach/typeclasses/` - Object classes
- `PyReach/world/` - Game world and systems
- `PyReach/web/` - Web interface

✅ **Configuration Templates:**
- `PyReach/server/conf/settings.py` - Base settings
- `PyReach/server/conf/*.py` - Other config files

✅ **Documentation:**
- `*.md` files - All documentation
- `requirements.txt` - Dependencies

✅ **Static Assets:**
- `PyReach/web/static/` - CSS, JS, images
- `PyReach/web/templates/` - HTML templates

### NOT Tracked by Git (.gitignore)

❌ **Environment:**
- `env/` - Virtual environment

❌ **Runtime Data:**
- `PyReach/server/evennia.db3` - Database
- `PyReach/server/logs/*.log` - Log files
- `PyReach/server/.static/` - Collected static files
- `PyReach/server/media/` - Uploaded files

❌ **Secrets:**
- `PyReach/server/conf/secret_settings.py` - Sensitive config

❌ **Cache:**
- `__pycache__/` - Python bytecode
- `*.pyc` - Compiled Python

## Secret Settings Management

### For Production

Create `PyReach/server/conf/secret_settings.py` on your server (not in git):

```python
# secret_settings.py (DO NOT COMMIT!)

SECRET_KEY = 'your-production-secret-key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pyreach_prod',
        'USER': 'pyreach_user',
        'PASSWORD': 'secure_password_here',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

EMAIL_HOST_PASSWORD = 'your_email_password'

# Any other sensitive settings
```

### Environment-Specific Config

You can use environment variables:

```python
# In secret_settings.py
import os

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
```

## Collaborative Development

### Multi-Developer Setup

**Developer 1:**
```bash
git clone <repo-url>
./install.sh
# Work on feature A
git checkout -b feature/combat-system
# ... make changes ...
git push origin feature/combat-system
```

**Developer 2:**
```bash
git clone <repo-url>
./install.sh
# Work on feature B
git checkout -b feature/wiki-content
# ... make changes ...
git push origin feature/wiki-content
```

**Merge conflicts:**
```bash
# Pull latest main
git checkout main
git pull

# Merge main into your feature
git checkout feature/your-feature
git merge main

# Resolve any conflicts
# Edit conflicted files
git add .
git commit -m "Merge main into feature branch"
```

## Best Practices

### Commit Often

- Small, focused commits
- Clear commit messages
- One logical change per commit

### Pull Regularly

```bash
# At least daily
git pull origin main
```

### Don't Commit

- Database files
- Log files
- Secret keys/passwords
- Virtual environments
- Generated files
- Personal notes

### Do Commit

- Source code
- Templates and static files
- Documentation
- Tests
- Configuration templates (not secrets!)

## Backup Strategy

### What to Backup

1. **Git Repository** - Your code (already safe if pushed to remote)
2. **Database** - Use pg_dump for PostgreSQL
3. **Media Files** - Uploaded images, files
4. **Secret Settings** - Keep encrypted backup

### Backup Script

```bash
#!/bin/bash
# backup.sh

# Backup database
pg_dump pyreach_db | gzip > backup_$(date +%Y%m%d).sql.gz

# Backup media
tar -czf media_$(date +%Y%m%d).tar.gz PyReach/server/media/

# Backup secret settings (encrypted)
gpg -c PyReach/server/conf/secret_settings.py
```

## Emergency Recovery

### Restore from Git

```bash
# Clone fresh copy
git clone <repo-url> pyreach-recovery
cd pyreach-recovery

# Install
./install.sh

# Restore database from backup
gunzip -c backup_YYYYMMDD.sql.gz | psql -U pyreach_user pyreach_db

# Restore media files
tar -xzf media_YYYYMMDD.tar.gz

# Restore secret settings
gpg -d secret_settings.py.gpg > PyReach/server/conf/secret_settings.py

# Start
cd PyReach
../env/bin/evennia start
```

## Git Hosting Recommendations

### Public Repository

**Pros:**
- Free hosting on GitHub/GitLab
- Community contributions
- Visibility for your game

**Cons:**
- Code is public
- Sensitive data must be managed carefully
- Game secrets might be spoiled

### Private Repository

**Pros:**
- Code stays private
- Better for game secrets
- Control who can see code

**Cons:**
- May require paid plan
- Fewer contributions
- Need to manage access

## Quick Reference

### Common Git Commands

```bash
# Status and info
git status                    # Check what changed
git log                       # View commit history
git diff                      # See changes

# Branching
git branch                    # List branches
git checkout -b new-branch    # Create and switch to branch
git checkout main             # Switch to main
git branch -d old-branch      # Delete branch

# Committing
git add .                     # Stage all changes
git add file.py               # Stage specific file
git commit -m "message"       # Commit with message
git commit --amend            # Modify last commit

# Remote operations
git push                      # Push to remote
git pull                      # Pull from remote
git fetch                     # Fetch without merging
git clone <url>               # Clone repository

# Undoing changes
git checkout -- file.py       # Discard changes to file
git reset HEAD file.py        # Unstage file
git reset --hard HEAD         # Discard all local changes
git revert <commit>           # Create new commit undoing changes
```

---

**Your PyReach git package is ready!** 🎉

Initialize git, commit your code, and push to your preferred hosting platform!

