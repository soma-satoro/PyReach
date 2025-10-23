# PyReach Deployment Guide

Complete guide for deploying PyReach to a production server.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Server Setup](#server-setup)
- [Installation](#installation)
- [Production Configuration](#production-configuration)
- [Web Server Setup](#web-server-setup)
- [Process Management](#process-management)
- [Security](#security)
- [Backups](#backups)
- [Monitoring](#monitoring)
- [Troubleshooting](#troubleshooting)

## Prerequisites

### Server Requirements

**Minimum:**
- 1 GB RAM
- 10 GB disk space
- Ubuntu 20.04+ or CentOS 8+
- Python 3.11+
- PostgreSQL 13+ (recommended) or SQLite

**Recommended:**
- 2+ GB RAM
- 20+ GB disk space
- Ubuntu 22.04 LTS
- Python 3.11+
- PostgreSQL 15+
- Nginx
- SSL certificate

### Domain Setup

- Domain name pointed to your server IP
- DNS A record configured
- Optional: Subdomain for wiki (wiki.yourgame.com)

## Server Setup

### 1. Update System

```bash
sudo apt update
sudo apt upgrade -y
```

### 2. Install Dependencies

```bash
# Essential packages
sudo apt install -y python3.11 python3.11-venv python3-pip git

# PostgreSQL
sudo apt install -y postgresql postgresql-contrib libpq-dev

# Build dependencies
sudo apt install -y build-essential python3.11-dev

# Optional: for image processing
sudo apt install -y libjpeg-dev libpng-dev
```

### 3. Create Game User

```bash
sudo adduser pyreach
sudo usermod -aG sudo pyreach
sudo su - pyreach
```

## Installation

### 1. Clone Repository

```bash
cd /home/pyreach
git clone <your-repo-url> pyreach
cd pyreach
```

### 2. Run Installation Script

```bash
chmod +x install.sh
./install.sh
```

This will:
- Create virtual environment
- Install all dependencies
- Run database migrations
- Create superuser
- Collect static files
- Optionally seed wiki

### 3. Configure Database

#### PostgreSQL Setup

```bash
# Switch to postgres user
sudo -u postgres psql

# In PostgreSQL prompt:
CREATE DATABASE pyreach_db;
CREATE USER pyreach_user WITH PASSWORD 'your_secure_password';
ALTER ROLE pyreach_user SET client_encoding TO 'utf8';
ALTER ROLE pyreach_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE pyreach_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE pyreach_db TO pyreach_user;
\q
```

#### Configure Django

Edit `PyReach/server/conf/secret_settings.py`:

```python
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pyreach_db',
        'USER': 'pyreach_user',
        'PASSWORD': 'your_secure_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Security
SECRET_KEY = 'your-very-long-random-secret-key-here'
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com', 'your.server.ip']
```

## Production Configuration

### Settings Checklist

Edit `PyReach/server/conf/settings.py` or `secret_settings.py`:

```python
# Server name
SERVERNAME = "Your Game Name"

# Security
DEBUG = False
SECRET_KEY = 'generate-a-long-random-string'
ALLOWED_HOSTS = ['yourdomain.com', 'your.ip.address']

# Database (PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pyreach_db',
        'USER': 'pyreach_user',
        'PASSWORD': 'secure_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Email (for password resets, notifications)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yourdomain.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'noreply@yourdomain.com'
EMAIL_HOST_PASSWORD = 'email_password'
DEFAULT_FROM_EMAIL = 'PyReach <noreply@yourdomain.com>'

# Static and media files
STATIC_ROOT = '/home/pyreach/pyreach/PyReach/server/.static'
MEDIA_ROOT = '/home/pyreach/pyreach/PyReach/server/media'
MEDIA_URL = '/media/'
```

### Generate Secret Key

```bash
python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Web Server Setup

### Nginx Configuration

Create `/etc/nginx/sites-available/pyreach`:

```nginx
upstream evennia {
    server 127.0.0.1:4005;
}

server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    
    # Redirect HTTP to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;
    
    # SSL Configuration
    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    
    # Security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;
    
    # Static files
    location /static/ {
        alias /home/pyreach/pyreach/PyReach/server/.static/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
    
    # Media files
    location /media/ {
        alias /home/pyreach/pyreach/PyReach/server/media/;
        expires 7d;
    }
    
    # WebSocket for webclient
    location /ws {
        proxy_pass http://127.0.0.1:4002;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_read_timeout 86400;
    }
    
    # Main web interface
    location / {
        proxy_pass http://evennia;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable the site:
```bash
sudo ln -s /etc/nginx/sites-available/pyreach /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### SSL Certificate (Let's Encrypt)

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

## Process Management

### Systemd Service

Create `/etc/systemd/system/pyreach.service`:

```ini
[Unit]
Description=PyReach Evennia MUD
After=network.target postgresql.service
Requires=postgresql.service

[Service]
Type=forking
User=pyreach
Group=pyreach
WorkingDirectory=/home/pyreach/pyreach/PyReach
Environment="PATH=/home/pyreach/pyreach/env/bin"
ExecStart=/home/pyreach/pyreach/env/bin/evennia start
ExecStop=/home/pyreach/pyreach/env/bin/evennia stop
ExecReload=/home/pyreach/pyreach/env/bin/evennia reload
Restart=on-failure
RestartSec=10
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable pyreach
sudo systemctl start pyreach
sudo systemctl status pyreach
```

### Service Management

```bash
# Start
sudo systemctl start pyreach

# Stop
sudo systemctl stop pyreach

# Restart
sudo systemctl restart pyreach

# Reload (keeps connections)
sudo systemctl reload pyreach

# View logs
sudo journalctl -u pyreach -f

# Check status
sudo systemctl status pyreach
```

## Security

### Firewall Setup

```bash
# Allow SSH
sudo ufw allow 22/tcp

# Allow HTTP/HTTPS
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# Allow Telnet (optional, can restrict to VPN)
sudo ufw allow 4000/tcp

# Enable firewall
sudo ufw enable
```

### Security Hardening

1. **Change default ports** (edit settings.py):
   ```python
   TELNET_PORTS = [your_custom_port]
   ```

2. **Restrict admin access** (nginx config):
   ```nginx
   location /admin/ {
       allow your.ip.address;
       deny all;
       proxy_pass http://evennia;
   }
   ```

3. **Enable fail2ban**:
   ```bash
   sudo apt install fail2ban
   ```

4. **Regular updates**:
   ```bash
   sudo apt update && sudo apt upgrade
   ```

## Backups

### Database Backup Script

Create `/home/pyreach/backup_database.sh`:

```bash
#!/bin/bash
# PyReach Database Backup Script

BACKUP_DIR="/home/pyreach/backups"
DATE=$(date +%Y%m%d_%H%M%S)
DB_NAME="pyreach_db"
DB_USER="pyreach_user"

# Create backup directory
mkdir -p $BACKUP_DIR

# Backup database
pg_dump -U $DB_USER $DB_NAME | gzip > $BACKUP_DIR/pyreach_$DATE.sql.gz

# Keep only last 30 days
find $BACKUP_DIR -name "pyreach_*.sql.gz" -mtime +30 -delete

echo "Backup completed: pyreach_$DATE.sql.gz"
```

Make executable and add to cron:
```bash
chmod +x /home/pyreach/backup_database.sh

# Add to crontab (daily at 3 AM)
crontab -e
# Add line:
0 3 * * * /home/pyreach/backup_database.sh
```

### Restore from Backup

```bash
# Stop Evennia
sudo systemctl stop pyreach

# Restore database
gunzip -c /home/pyreach/backups/pyreach_YYYYMMDD_HHMMSS.sql.gz | psql -U pyreach_user pyreach_db

# Start Evennia
sudo systemctl start pyreach
```

## Monitoring

### Log Monitoring

**Server logs:**
```bash
# Real-time
tail -f /home/pyreach/pyreach/PyReach/server/logs/server.log

# Last 100 lines
tail -100 /home/pyreach/pyreach/PyReach/server/logs/server.log

# Search for errors
grep ERROR /home/pyreach/pyreach/PyReach/server/logs/server.log
```

**System logs:**
```bash
sudo journalctl -u pyreach -f
```

### Performance Monitoring

**Check processes:**
```bash
ps aux | grep evennia
```

**Check memory:**
```bash
free -h
```

**Check disk:**
```bash
df -h
```

## Updates and Maintenance

### Updating PyReach

```bash
cd /home/pyreach/pyreach

# Backup first!
./backup_database.sh

# Pull latest changes
git pull origin main

# Activate venv
source env/bin/activate

# Update dependencies
pip install -r requirements.txt --upgrade

# Run new migrations
cd PyReach
evennia migrate

# Collect static files
evennia collectstatic --noinput

# Reload server
sudo systemctl reload pyreach
```

### Routine Maintenance

**Weekly:**
- Check logs for errors
- Monitor database size
- Review player feedback
- Update wiki content

**Monthly:**
- Update system packages
- Review and rotate logs
- Test backups
- Security audit

## Troubleshooting

### Server Won't Start

```bash
# Check logs
sudo journalctl -u pyreach -n 50

# Check port conflicts
sudo netstat -tulpn | grep :4000
sudo netstat -tulpn | grep :4001

# Check permissions
ls -la /home/pyreach/pyreach/PyReach

# Try manual start
cd /home/pyreach/pyreach/PyReach
source ../env/bin/activate
evennia start
```

### Database Issues

```bash
# Check PostgreSQL
sudo systemctl status postgresql

# Check connections
sudo -u postgres psql -c "\l"

# Test connection
psql -U pyreach_user -d pyreach_db -h localhost
```

### Performance Issues

```bash
# Check memory usage
top

# Check database size
sudo -u postgres psql -c "SELECT pg_size_pretty(pg_database_size('pyreach_db'));"

# Optimize database
cd /home/pyreach/pyreach/PyReach
evennia dbshell
# In psql: VACUUM ANALYZE;
```

### 500 Errors

```bash
# Check server log
tail -100 /home/pyreach/pyreach/PyReach/server/logs/server.log | grep -A 20 "ERROR\|Traceback"

# Check file permissions
ls -la /home/pyreach/pyreach/PyReach/server/.static/

# Collect static again
cd /home/pyreach/pyreach/PyReach
evennia collectstatic --noinput
```

## Scaling

### For High Traffic

**Database:**
- Use PostgreSQL connection pooling
- Add database indexes
- Configure query optimization

**Caching:**
- Install Redis
- Enable Django caching
- Cache wiki pages

**Load Balancing:**
- Multiple Evennia instances
- Nginx load balancing
- Shared database and Redis

## Monitoring Tools

### Optional Monitoring

**Prometheus + Grafana:**
- Monitor server metrics
- Track player counts
- Database performance

**Uptime monitoring:**
- UptimeRobot
- Pingdom
- StatusCake

## Support

### Getting Help

- **Evennia Discord**: https://discord.gg/AJJpcRUhtF
- **Documentation**: Check all .md files in the repository
- **GitHub Issues**: For bug reports and questions

### Emergency Contacts

Document your emergency procedures:
- Backup admin account credentials
- Database access information
- Server access details
- Escalation procedures

---

**Deployment Checklist:**

- [ ] Server provisioned and updated
- [ ] PostgreSQL installed and configured
- [ ] PyReach installed via script
- [ ] Secret settings configured
- [ ] Database migrated
- [ ] Static files collected
- [ ] Superuser created
- [ ] Systemd service configured
- [ ] Nginx installed and configured
- [ ] SSL certificate obtained
- [ ] Firewall configured
- [ ] Backup script installed and tested
- [ ] Monitoring configured
- [ ] Documentation updated
- [ ] Game tested end-to-end

Good luck with your deployment! 🚀

