## Installation

The wiki is integrated into PyReach. To set it up:

### 1. Install Required Python Packages

```bash
cd c:\exordium
.\env\Scripts\activate
pip install markdown Pillow
```

### 2. Run Database Migrations

```bash
cd PyReach
evennia migrate wiki
```

### 3. Collect Static Files

```bash
evennia collectstatic --noinput
```

### 4. Create Superuser (if needed)

```bash
evennia createsuperuser
```

### 5. Restart Evennia

```bash
evennia reload
```

## Usage

### Accessing the Wiki

- **Public Wiki**: `http://your-server:4001/wiki/`
- **Create Page**: `http://your-server:4001/wiki/create/`
- **Admin Interface**: `http://your-server:4001/admin/wiki/`

### Creating Categories

1. Log in as staff
2. Go to `/wiki/category/create/`
3. Fill in:
   - Name (e.g., "Setting", "Factions", "Rules")
   - Description
   - Icon (Font Awesome class like `fa-book`)
   - Order (display priority)
4. Click "Create Category"

### Creating Pages

1. Log in with appropriate permissions
2. Click "New Page" in navigation
3. Fill in the form:
   - **Title**: Page title
   - **Slug**: URL-friendly version (auto-generated)
   - **Category**: Select from dropdown
   - **Content**: Write using Markdown
   - **Tags**: Add comma-separated tags
   - **Publishing Options**: 
     - Published: Make visible to players
     - Staff Only: Restrict to staff
     - Featured: Show on home page
4. Click "Preview" to see how it looks
5. Click "Create Page" to publish

### Markdown Formatting

The wiki supports full Markdown syntax:

```markdown
# Heading 1
## Heading 2
### Heading 3

**Bold text**
*Italic text*

- Bullet list
- Another item

1. Numbered list
2. Second item

[Link text](https://example.com)

> Blockquote for important notes

`inline code`

\`\`\`
Code block
\`\`\`
```

### Permissions

The wiki uses Django's permission system:

- **can_edit_wiki**: Can create and edit wiki pages
- **can_publish_wiki**: Can publish pages

Grant these to users via Django admin:
1. Go to `/admin/auth/user/`
2. Select user
3. Add permissions
4. Save

## Gothic-Punk Theme

The wiki features a dark, dramatic design:

- **Colors**: Deep blacks, rich purples, crimson accents, gold highlights
- **Typography**: 
  - Cinzel for headings (gothic display)
  - Cormorant Garamond for body text (elegant serif)
  - Inter for UI elements (modern sans-serif)
- **Effects**: Glowing shadows, smooth transitions, hover animations
- **Layout**: Clean, modern cards with dramatic borders

### Customizing the Theme

Edit `/web/static/wiki/css/wiki.css` to customize:

```css
:root {
    --color-accent-red: #c41e3a;
    --color-accent-purple: #8b5cf6;
    --color-accent-gold: #d4af37;
    /* ... more variables */
}
```

## Admin Features

### Django Admin

Access comprehensive wiki management at `/admin/wiki/`:

- **Pages**: View, edit, delete all pages
- **Categories**: Manage category hierarchy
- **Revisions**: View page history
- **Images**: Upload and manage images

### Bulk Operations

Use Django admin for bulk actions:
- Publish/unpublish multiple pages
- Change categories in bulk
- Delete multiple pages

## Advanced Features

### Revision History

Every page edit creates a revision:
- View in Django admin: `/admin/wiki/wikirevision/`
- Revisions store: content, author, timestamp, summary
- Can be used to restore previous versions

### Staff-Only Pages

Mark pages as "Staff Only" to hide from regular users:
- Only visible to authenticated staff
- Useful for game master notes, upcoming content
- Still searchable by staff

### Featured Pages

Feature important pages on the wiki home:
- Shows on main wiki page
- Limited to 6 most recent featured pages
- Great for announcements, essential lore

### Search

Full-text search across:
- Page titles
- Content
- Summaries
- Tags

Accessible at `/wiki/search/` or via search bar.

## Troubleshooting

### Static Files Not Loading

```bash
cd PyReach
evennia collectstatic --noinput
evennia reload
```

### Images Not Displaying

Ensure `MEDIA_ROOT` and `MEDIA_URL` are configured in settings.py.

### Permission Errors

Grant wiki permissions via Django admin:
```bash
evennia shell
>>> from django.contrib.auth.models import User, Permission
>>> user = User.objects.get(username='youruser')
>>> perm = Permission.objects.get(codename='can_edit_wiki')
>>> user.user_permissions.add(perm)
>>> user.save()
```

### Migration Errors

```bash
cd PyReach
evennia migrate wiki --fake-initial
```

## File Structure

```
world/wiki/
├── __init__.py
├── admin.py          # Django admin configuration
├── apps.py           # App configuration
├── forms.py          # Page and category forms
├── models.py         # Database models
├── urls.py           # URL routing
├── views.py          # View logic
└── README.md         # This file

web/templates/wiki/
├── base.html         # Base template
├── index.html        # Wiki home page
├── page_detail.html  # Page display
├── page_form.html    # Create/edit page
├── category.html     # Category listing
├── search.html       # Search results
├── all_pages.html    # All pages list
└── *.html           # Other templates

web/static/wiki/
├── css/
│   └── wiki.css     # Gothic-punk styling
└── js/
    └── wiki.js      # Interactive features
```

## Integration with Evennia

The wiki is a standard Django app integrated with Evennia:

- Uses Evennia's user model
- Respects Evennia's permission system
- Follows Evennia's app structure
- Can be extended with Evennia objects

### Linking to In-Game Objects

You can link wiki pages to in-game objects:

```python
from world.wiki.models import WikiPage

# In a typeclass or command:
character.db.wiki_page = "character-name-slug"

# Then in commands:
wiki_slug = character.db.wiki_page
if wiki_slug:
    caller.msg(f"Learn more: http://yourserver:4001/wiki/page/{wiki_slug}/")
```

## Future Enhancements

Potential additions:
- Page templates for common content types
- Version comparison (diff view)
- Comments/discussion on pages
- Page relationships (related pages auto-linking)
- Export to PDF/markdown
- Multi-language support
- Integration with in-game help system
