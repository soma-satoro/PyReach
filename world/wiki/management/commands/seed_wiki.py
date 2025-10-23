"""
Management command to seed initial wiki content.
Usage: evennia seed_wiki
"""

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings
from world.wiki.models import WikiCategory, WikiPage


class Command(BaseCommand):
    help = 'Seeds the wiki with initial categories and sample pages'

    def handle(self, *args, **options):
        User = get_user_model()
        
        # Get or create system user
        system_user, _ = User.objects.get_or_create(
            username='System',
            defaults={'is_staff': True, 'is_superuser': False}
        )
        
        # Get game name from settings
        game_name = getattr(settings, 'SERVERNAME', 'Exordium')

        self.stdout.write('Creating wiki categories...')
        
        # Create main categories
        categories_data = [
            {
                'name': 'Setting',
                'description': 'Information about the game world, history, and setting',
                'icon': 'fa-globe',
                'order': 0
            },
            {
                'name': 'Rules',
                'description': 'Game rules, mechanics, and systems',
                'icon': 'fa-book',
                'order': 1
            },
            {
                'name': 'Factions',
                'description': 'Organizations, groups, and factions in the world',
                'icon': 'fa-users',
                'order': 2
            },
            {
                'name': 'Characters',
                'description': 'Character creation, development, and guidelines',
                'icon': 'fa-user',
                'order': 3
            },
            {
                'name': 'Lore',
                'description': 'Deep lore, mythology, and world-building details',
                'icon': 'fa-scroll',
                'order': 4
            },
            {
                'name': 'Locations',
                'description': 'Places, cities, and regions in the game world',
                'icon': 'fa-map-marked-alt',
                'order': 5
            },
            {
                'name': 'News & Updates',
                'description': 'Announcements, updates, and game news',
                'icon': 'fa-newspaper',
                'order': 6
            },
        ]

        categories = {}
        for cat_data in categories_data:
            category, created = WikiCategory.objects.get_or_create(
                name=cat_data['name'],
                defaults={
                    'description': cat_data['description'],
                    'icon': cat_data['icon'],
                    'order': cat_data['order']
                }
            )
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(self.style.SUCCESS(f'  ✓ Created category: {category.name}'))
            else:
                self.stdout.write(f'  - Category already exists: {category.name}')

        self.stdout.write('\nCreating sample wiki pages...')
        
        # Create sample pages
        pages_data = [
            {
                'title': f'Welcome to {game_name}',
                'category': 'News & Updates',
                'content': f'''# Welcome to {game_name}

Welcome to the {game_name} wiki! This is your comprehensive guide to our dark and mysterious world.

## What is {game_name}?

{game_name} is a text-based multiplayer roleplaying game set in a gothic-punk universe where shadows hold secrets and power comes at a price.

## Getting Started

- **Read the Rules**: Check out our game rules and policies
- **Create a Character**: Learn about character creation and development
- **Explore the Setting**: Discover the world, its history, and its denizens
- **Join the Community**: Connect with other players and storytellers

## Recent Updates

This wiki is constantly being updated with new information, lore, and content. Check back regularly for new pages and updates!

## Contributing

Staff members can create and edit wiki pages. If you have suggestions for new content or spot any errors, please contact a staff member.

---

*May the shadows guide your path.*
''',
                'summary': f'Welcome page introducing new players to {game_name} and the wiki system',
                'featured': True,
                'published': True,
            },
            {
                'title': 'Character Creation Guide',
                'category': 'Characters',
                'content': f'''# Character Creation Guide

Creating a character in {game_name} is an exciting journey. This guide will walk you through the process.

## Step 1: Concept

Start with a strong character concept. Ask yourself:
- Who is your character?
- What drives them?
- What is their background?
- What secrets do they hide?

## Step 2: Template Selection

Choose a character template that fits your concept:
- **Mortal**: Regular humans navigating a supernatural world
- **Vampire**: Undead predators of the night
- **Werewolf**: Shapeshifters protecting or exploiting the wild
- **Mage**: Wielders of reality-bending magic
- **Changeling**: Fae-touched beings straddling two worlds

## Step 3: Attributes & Skills

Distribute points among your character's:
- Physical attributes (Strength, Dexterity, Stamina)
- Social attributes (Presence, Manipulation, Composure)
- Mental attributes (Intelligence, Wits, Resolve)
- Skills and abilities

## Step 4: Background

Flesh out your character's history, relationships, and motivations. A rich background makes for engaging roleplay!

## Step 5: Submit

Submit your character application for staff review. We're here to help bring your vision to life!

## Need Help?

Contact a staff member if you have questions during character creation.
''',
                'summary': f'Complete guide to creating characters in {game_name}',
                'tags': 'character, creation, guide, getting started',
                'published': True,
            },
            {
                'title': 'The City of Shadows',
                'category': 'Locations',
                'content': f'''# The City of Shadows

The primary setting for {game_name} is a sprawling metropolis known colloquially as the City of Shadows, though its official name has been lost to time and mythology.

## Geography

The city spreads across both sides of the Dark River, connected by ancient bridges and modern tunnels. Districts range from glittering corporate towers to decrepit industrial zones where the desperate and supernatural lurk.

## Key Districts

### The Gothic Quarter
Historic heart of the city, featuring:
- Ancient cathedrals and churches
- Gothic architecture dating back centuries
- Hidden crypts and underground passages
- Vampire havens and elysiums

### The Neon District
Modern entertainment and vice, including:
- Nightclubs and bars
- Underground fight clubs
- Black markets
- Neutral meeting grounds

### The Industrial Wastes
Abandoned factories and warehouses:
- Werewolf territory
- Homeless encampments
- Secret meeting places
- Hidden laboratories

### The Heights
Wealthy residential and corporate zones:
- Penthouses and luxury apartments
- Corporate headquarters
- High security
- Mage sanctums

## The Underworld

Beneath the city lies a vast network of:
- Sewer systems
- Old subway tunnels
- Ancient catacombs
- Secret sanctuaries

Many supernatural beings make their homes in these hidden depths, away from mortal eyes.

## Getting Around

Transportation includes:
- Public transit (buses, metro)
- Private vehicles
- Rooftop parkour for the agile
- Secret supernatural methods
''',
                'summary': 'Overview of the primary game setting and its key locations',
                'tags': 'setting, location, city, geography',
                'featured': True,
                'published': True,
            },
            {
                'title': 'Basic Rules',
                'category': 'Rules',
                'content': f'''# Basic Rules

Welcome to the {game_name} rules guide. Please read and understand these before playing.

## Core Principles

1. **Respect**: Treat all players and staff with respect
2. **Consent**: Obtain consent for mature or potentially triggering content
3. **Immersion**: Stay in character in IC areas
4. **Fairness**: Play fair and don't metagame or powergame

## Roleplay Guidelines

### IC vs OOC
- **IC (In Character)**: Your character's actions and words
- **OOC (Out of Character)**: You as a player

Keep IC and OOC separate. IC actions have IC consequences.

### Consent and Boundaries
- Respect player boundaries
- Discuss mature themes beforehand
- Use safety tools (X-card, fade-to-black)

### Power Gaming
Don't:
- Auto-hit other characters
- Ignore damage or consequences
- Declare outcomes without rolls
- Use OOC knowledge IC (metagaming)

## Dice System

We use Chronicles of Darkness 2nd Edition mechanics:
- Roll attribute + skill
- 8+ is a success
- 10 counts as two successes
- Dramatic failure on no successes and a 1

## Character Death

Character death is possible but should be meaningful:
- Always requires consent for PvP death
- NPCs may kill without consent in dangerous situations
- Death should advance story, not just happen randomly

## Getting Help

Questions? Contact staff:
- Use the +jobs system
- Page a staff member
- Ask in the OOC channel

---

*Remember: The goal is collaborative storytelling and fun!*
''',
                'summary': f'Core rules and guidelines for playing in {game_name}',
                'tags': 'rules, guidelines, policies, getting started',
                'featured': True,
                'published': True,
            },
            {
                'title': 'Staff Guidelines',
                'category': 'Rules',
                'content': f'''# Staff Guidelines

**Staff Only Information**

This page contains guidelines and information for {game_name} staff members.

## Storyteller Duties

- Run engaging scenes and plots
- Respond to +jobs promptly
- Maintain game balance
- Foster inclusive environment

## Character Approval

When reviewing applications:
- Check for rule compliance
- Ensure concept fits setting
- Verify stat allocation
- Review background for hooks

## Conflict Resolution

Handle disputes fairly:
- Listen to all sides
- Review logs if available
- Apply rules consistently
- Document decisions

## Wiki Maintenance

Staff should help maintain the wiki:
- Create new lore pages
- Update existing content
- Organize categories
- Feature important pages

---

*With great power comes great responsibility.*
''',
                'summary': f'Guidelines and procedures for {game_name} staff members',
                'tags': 'staff, admin, guidelines',
                'staff_only': True,
                'published': True,
            },
        ]

        for page_data in pages_data:
            category = categories.get(page_data['category'])
            if not category:
                self.stdout.write(self.style.WARNING(f'  ! Category not found for page: {page_data["title"]}'))
                continue
            
            page, created = WikiPage.objects.get_or_create(
                title=page_data['title'],
                defaults={
                    'content': page_data['content'],
                    'summary': page_data.get('summary', ''),
                    'category': category,
                    'tags': page_data.get('tags', ''),
                    'published': page_data.get('published', True),
                    'staff_only': page_data.get('staff_only', False),
                    'featured': page_data.get('featured', False),
                    'created_by': system_user,
                    'updated_by': system_user,
                }
            )
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'  ✓ Created page: {page.title}'))
            else:
                self.stdout.write(f'  - Page already exists: {page.title}')

        self.stdout.write(self.style.SUCCESS('\n✓ Wiki seeding complete!'))
        self.stdout.write('\nYou can now access the wiki at: http://your-server:4001/wiki/')
        self.stdout.write('To edit content, log in as a staff member.')

