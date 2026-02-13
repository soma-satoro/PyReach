# Complete Command Reference

**Version:** Chronicles of Darkness 2nd Edition  
**Last Updated:** October 2025

**IMPORTANT NOTE:** All character-targeting commands support **both character names and aliases** and search **globally** by default (you can target any character anywhere in the game world).

---

## Table of Contents

1. [Character Creation & Development](#character-creation--development)
2. [Communication Commands](#communication-commands)
3. [Roleplaying Tools](#roleplaying-tools)
4. [Combat System](#combat-system)
5. [Game Systems](#game-systems)
6. [Group & Organization Commands](#group--organization-commands)
7. [Mystery & Investigation](#mystery--investigation)
8. [Information & Reference](#information--reference)
9. [Building & World Management](#building--world-management)
10. [Staff & Admin Commands](#staff--admin-commands)
11. [Jobs & Request System](#jobs--request-system)
12. [Bulletin Board System](#bulletin-board-system)

---

## Character Creation & Development

### `+sheet` (aliases: `sheet`)
Display your character sheet with all stats, merits, and current status.
- **Usage:**
  - `+sheet` - View your own sheet
  - `+sheet <character>` - View another character's sheet (if permitted)
- **Switches:**
  - `/full` - Show complete detailed sheet
  - `/compact` - Show condensed version
  - `/legacy` - Show legacy mode sheet (if enabled)
  - `/show` - Show your sheet to the room
  - `/show <player>` - Show your sheet to specific player (requires them online)
- **Notes:**
  - Supports character aliases
  - **Works on offline characters** - view any character's sheet anytime
  - Only `/show` switch requires target to be online

### `+stat` (aliases: `+stats`)
Set and manage character statistics including attributes, skills, merits, and more.
- **Usage:**
  - `+stat <stat>=<value>` - Set a stat on yourself
  - `+stat <name>/<stat>=<value>` - Set stat on someone else (staff only)
  - `+stat/list [name]` - List all stats
  - `+stat/remove <stat>` - Remove a stat
- **Examples:**
  - `+stat strength=3`
  - `+stat wits=4`
  - `+stat brawl=2`
- **Notes:**
  - Supports character aliases
  - **Works on offline characters** - staff can modify stats anytime

### `+recalc` (aliases: `recalc`)
Recalculate derived statistics (health, willpower, defense, etc.) based on current stats.
- **Usage:** `+recalc [character]`

### `+xp` (aliases: `+experience`)
Manage experience points, beats, and character advancement.
- **Usage:**
  - `+xp` - Show current XP and beats
  - `+xp/beat <source>` - Add a beat
  - `+xp/spend <stat>=<dots>` - Spend XP on advancement
  - `+xp/buy <merit>=[dots]` - Purchase a merit
  - `+xp/costs` - Show XP costs
  - `+xp/list merits [category]` - List available merits
  - `+xp/info <merit>` - Show merit details
- **Beat Sources:** dramatic_failure, exceptional_success, conditions, aspirations, story, scene, session, roleplay

### `+aspiration` (aliases: `+asp`)
Manage character aspirations (goals that drive story and earn beats).
- **Usage:**
  - `+aspiration/list` - Show your aspirations
  - `+aspiration/add <number> <description>` - Add/update aspiration
  - `+aspiration/remove <number>` - Remove aspiration
  - `+aspiration/fulfill <number>` - Fulfill aspiration and earn beat

### `+health`
Manage character health track and damage.
- **Usage:**
  - `+health` - View your health
  - `+health <character>` - View another's health (staff)
  - `+health/damage <type> <amount>` - Apply damage (bashing, lethal, aggravated)
  - `+health/heal <type> <amount>` - Heal damage
  - `+health/set <health string>` - Set exact health track

### `+integrity`
Manage character Integrity stat and breaking points.
- **Usage:**
  - `+integrity` - View your integrity
  - `+integrity/check <level>` - Make breaking point roll
  - `+integrity/set <value>` - Set integrity (staff only)

### `+legacy`
Toggle between Chronicles of Darkness 2e and Legacy (oWoD) mode.
- **Usage:**
  - `+legacy` - Check current mode
  - `+legacy/on` - Enable legacy mode
  - `+legacy/off` - Disable legacy mode
  - `+legacy/info` - Show mode differences

---

## Communication Commands

### `page` (aliases: `tell`, `p`)
Send private messages to other players.
- **Usage:**
  - `page <character>=<message>` - Send a page
  - `page <char1>,<char2>=<message>` - Page multiple people
  - `page <number>` - View last N pages
  - `page/last` - View last page sent
  - `page/idle <message>` - Set idle message
- **Notes:** 
  - Supports character aliases (e.g., `page Lys=Hello` finds Lysander)
  - **Requires target to be online** - offline characters cannot receive pages

### `+txt` (aliases: `+text`, `+sms`)
Send in-character text messages between characters.
- **Usage:**
  - `+txt <character>=<message>` - Send text
  - `+txt/pic <character>=<description>` - Send picture
  - `+txt/opt-in` - Enable texting system
  - `+txt/opt-out` - Disable texting system
  - `+txt <number>` - View text history
- **Notes:**
  - Supports character aliases
  - **Requires target to be online** to receive messages
  - Characters must opt-in to use the texting system

### `+watch`
Track login/logout of friends.
- **Usage:**
  - `+watch` - Show who you're watching that's connected
  - `+watch/add <character>` - Add to watch list
  - `+watch/del <character>` - Remove from watch list
  - `+watch/who` - Show full watch list with status
  - `+watch/on` - Turn watch notifications on
  - `+watch/off` - Turn watch notifications off
  - `+watch/hide` - Hide yourself from watch
  - `+watch/unhide` - Unhide from watch

### `say` (aliases: `'`, `"`)
Speak in-character to your current location.
- **Usage:** `say <message>` or `"<message>`

### `pose` (aliases: `:`, `emote`)
Perform an action/emote in your current location.
- **Usage:** 
  - `pose <action>` or `:<action>`
  - `:s <action>` - No-space pose

### `+emit`
Emit text to the room (no name prepended).
- **Usage:** `+emit <text>`

### `+ooc`
Out-of-character channel communication.
- **Usage:**
  - `+ooc <message>` - Send OOC message
  - `+ooc/on` - Join OOC channel
  - `+ooc/off` - Leave OOC channel

### `+finger`
Display OOC information about a character.
- **Usage:**
  - `+finger <character>` - View someone's finger
  - `+finger me` - View your own finger
  - `+finger/set <attribute>=<value>` - Set finger info
- **Attributes:** email, position, age, fame, app-age, plan, rp-prefs, themesong, quote, off-hours, temperament, vacation, url
- **Notes:**
  - Supports character aliases
  - **Works on offline characters** - view info anytime
  - Shows online/idle time if character is logged in

### `+alts` (aliases: `alts`)
Manage character alts (declare alternate characters).
- **Usage:**
  - `+alts` - Show your alts
  - `+alts <character>` - View someone's public alts
  - `+alts/add <character>` - Request to add as alt
  - `+alts/confirm <code>` - Confirm alt request
  - `+alts/del <character>` - Remove alt
  - `+alts/pending` - View pending requests

### `alias`
Set a short name that others can use to refer to you in ALL character-targeting commands.
- **Usage:**
  - `alias me=<text>` - Set your alias (2-15 alphanumeric characters)
  - `alias/remove` - Remove your alias
  - `alias <character>` - View someone's alias
- **Example:** `alias me=Lys` (others can now use "Lys" instead of "Lysander" in all commands)
- **Supported In:** page, +finger, +txt, +watch, +stat, +sheet, +combat, +mystery, +group, +condition, +tilt, +social, +note, and all other character-targeting commands
- **Features:** Case-insensitive, globally searchable, validated for uniqueness

### `+who`
See who is currently online.
- **Usage:** `+who`
- **Shows:** Character names, templates, idle times

---

## Roleplaying Tools

### `+roll` (aliases: `roll`)
Roll dice using Chronicles of Darkness mechanics.
- **Usage:**
  - `+roll <stat> + <skill>` - Roll stat + skill
  - `+roll <number>` - Roll number of dice
  - `+roll <stat> + <skill> +/- <modifier>` - With modifier
- **Switches:**
  - `/8` - 8-again
  - `/9` - 9-again
  - `/10` - 10-again
  - `/rote` - Rote quality (reroll failures)
  - `/reflex` - Reflexive action
  - `/damage` - Damage roll
  - `/job` - Roll to job
- **Examples:**
  - `+roll/8 Strength + Weaponry`
  - `+roll/9/rote Wits + Investigation + 2`
  - `+roll/job Manipulation + Persuasion=123`

### `+pool` (aliases: `pool`)
Calculate dice pool for a given action.
- **Usage:** `+pool <stat> + <skill> [+ modifier]`
- **Example:** `+pool Strength + Brawl + 2`

### `+social`
Manage social maneuvering mechanics (doors, leverage, impressions).
- **Usage:**
  - `+social/impression <target> <level>` - Set impression
  - `+social/doors <target>` - Check doors
  - `+social/leverage <target> <type> <description>` - Add leverage
  - `+social/roll <target> <goal>` - Make social roll
- **Impression Levels:** perfect, excellent, good, average, hostile
- **Leverage Types:** soft (favors, bribes), hard (threats, blackmail)

### `+note` (aliases: `+notes`)
Manage character notes and long-form narrative content.
- **Usage:**
  - `+note` - List all your notes
  - `+note <title>` - View a specific note
  - `+note <title>/<category>=<text>` - Create note
  - `+note/edit <title>=<new text>` - Edit note
  - `+note/delete <title>` - Delete note
  - `+note/show <title>` - Show note to room
  - `+note/show <title>=<player>` - Show note to specific player
- **Staff Commands:**
  - `+note <player>` - View player's notes
  - `+note/approve <character>=<title>` - Approve note
  - `+note/unapprove <character>=<title>` - Unapprove note

### `+hangouts` (aliases: `hangout`, `hangouts`)
Find and travel to designated RP locations.
- **Usage:**
  - `+hangouts` - List all available hangout locations
  - `+hangouts <name>` - Move to a specific hangout
  - `+hangouts/return` - Return to previous location
  - `+hangouts/public` - List only public hangouts
  - `+hangouts/groups` - List only group hangouts

### `+shortdesc`
Set your character's short description.
- **Usage:** `+shortdesc <description>`
- **Example:** `+shortdesc A tall, imposing figure with piercing eyes`

### `+language`
Speak in different languages.
- **Usage:**
  - `+language` - List languages you know
  - `+language <language>=<message>` - Speak in language
  - `+language/set <language>` - Set default language

---

## Combat System

### `+combat` (aliases: `+fight`, `+init`)
Main combat system commands.
- **Usage:**
  - `+combat/start` - Start combat in current location
  - `+combat/join [team]` - Join combat
  - `+combat/leave` - Leave combat
  - `+combat/next` - Advance to next turn
  - `+combat/init` - Roll initiative
  - `+combat/status` - View combat status
  - `+combat/end` - End combat (staff)
- **Attack Commands:**
  - `+combat/attack <target> [weapon]` - Make attack
  - `+combat/dodge <attacker>` - Dodge action
  - `+combat/parry <attacker>` - Parry action
  - `+combat/allout <target>` - All-out attack
  - `+combat/called <target> <penalty>` - Called shot
- **Combat Actions:**
  - `+combat/aim [target]` - Aim action
  - `+combat/defend` - Total defense
  - `+combat/move` - Move action
  - `+combat/ready <weapon>` - Ready weapon
- **Important:**
  - **LOCAL ONLY:** Combat targets must be in the same room
  - **ONLINE ONLY:** Combat targets must be currently logged in
  - Supports character aliases for targeting
  - Cannot attack characters in other locations or offline players

### `+condition`
Manage conditions on characters.
- **Usage:**
  - `+condition/list [character]` - List conditions
  - `+condition/add <character>=<condition>` - Add condition
  - `+condition/remove <character>=<condition>` - Remove condition
  - `+condition/help <condition>` - Show condition info

### `+tilt` (aliases: `+tilts`)
Manage combat tilts (temporary combat conditions).
- **Usage:**
  - `+tilt/list [character]` - List tilts
  - `+tilt/add <character>=<tilt>` - Add tilt
  - `+tilt/remove <character>=<tilt>` - Remove tilt
  - `+tilt/env/add <tilt>` - Add environmental tilt
  - `+tilt/env/remove <tilt>` - Remove environmental tilt
  - `+tilt/advance` - Advance all tilts by one turn

### `+weapons` (aliases: `+weaponlist`)
List available weapons and their statistics.
- **Usage:** `+weapons [filter]`

### `+gear` (aliases: `+equipped`)
View equipped weapons and armor.
- **Usage:** `+gear [character]`

### `+chelp` (aliases: `+combathelp`)
Display combat system help and reference.
- **Usage:** `+chelp [topic]`

---

## Game Systems

### `+condition` (see Combat System section)

### `+tilt` (see Combat System section)

### `+shapeshifting`
Manage shapeshifting forms (for applicable splats).
- **Usage:**
  - `+shift <form>` - Change form
  - `+shift/list` - List available forms
  - `+shift/info <form>` - Show form details

### `+equipment`
Manage character equipment and possessions.
- **Usage:**
  - `+equipment` - List your equipment
  - `+equipment/add <item>=<description>` - Add item
  - `+equipment/remove <item>` - Remove item
  - `+equipment/view <item>` - View item details

### `+voting`
Participate in game votes and polls.
- **Usage:**
  - `+voting` - List active votes
  - `+voting/cast <vote id>=<choice>` - Cast vote
  - `+voting/results <vote id>` - View results (if closed)

---

## Group & Organization Commands

### `+group` (aliases: `+groups`)
Create and manage player groups and organizations.
- **Usage:**
  - `+groups` - List all public groups
  - `+group <id>` - View group details
  - `+group/join <id>` - Request to join group
  - `+group/leave <id>` - Leave group
  - `+group/members <id>` - List members
  - `+group/info <id>` - Detailed group information
- **Staff Commands:**
  - `+group/create <name>` - Create group
  - `+group/destroy <id>` - Destroy group
  - `+group/add <id>=<character>` - Add member
  - `+group/remove <id>=<character>` - Remove member
  - `+group/promote <id>=<character>` - Promote to leader
  - `+group/type <id>=<type>` - Set group type

### `+roster`
View group rosters and active members.
- **Usage:** `+roster <group>`

### `+groupmerit` (aliases: `+gmerit`)
Manage group merits and shared resources.
- **Usage:**
  - `+groupmerit <group>` - View group merits
  - `+groupmerit/add <group>=<merit>` - Add merit (staff)
  - `+groupmerit/remove <group>=<merit>` - Remove merit (staff)

### `+totem`
Manage pack totems (Werewolf: The Forsaken).
- **Usage:**
  - `+totem <pack>` - View pack totem
  - `+totem/set <pack>=<totem>` - Set totem (staff)

---

## Mystery & Investigation

### `+mystery` (aliases: `+investigation`, `+inv`, `+mysteries`)
Unified mystery and investigation system for players and staff.
- **Player Commands:**
  - `+mystery` - List active mysteries
  - `+mystery <id>` - View mystery details
  - `+mystery/progress [id]` - Show investigation progress
  - `+mystery/examine <object>` - Examine object for clues
  - `+mystery/search` - Search area for clues
- **Staff Commands:**
  - `+mystery/create <title>` - Create new mystery
  - `+mystery/edit <id>/<field>=<value>` - Edit mystery
  - `+mystery/delete <id>` - Delete mystery
  - `+mystery/addclue <id>/<clue>=<description>` - Add clue
  - `+mystery/grant <char>=<id>/<clue>` - Grant clue to character
  - `+mystery/revoke <char>=<id>/<clue>` - Revoke clue
  - `+mystery/discoveries <id> [char]` - View discoveries

---

## Information & Reference

### `+who` (see Communication Commands)

### `+finger` (see Communication Commands)

### `+staff`
List and manage staff members.
- **Usage:**
  - `+staff` - List all staff
  - `+staff/duty` - Toggle duty status (staff)
  - `+staff/dark` - Toggle visibility (staff)
- **Admin Commands:**
  - `+staff/position <account>=<position>` - Set position
  - `+staff/add <account>` - Add staff
  - `+staff/remove <account>` - Remove staff

### `+storyteller` (aliases: `+st`, `+storytellers`)
Manage storyteller flags and permissions.
- **Usage:**
  - `+storyteller/list` - List storytellers
  - `+storyteller/check [char]` - Check ST status
  - `+storyteller/info` - Show ST permissions
- **Admin Commands:**
  - `+storyteller/add <character>` - Grant ST flag
  - `+storyteller/remove <character>` - Remove ST flag

### `+stwho` (aliases: `+storytellerwho`)
List online storytellers.
- **Usage:** `+stwho`

### `+weather`
Display current weather and time information.
- **Usage:** `+weather`

### `+lookup`
Look up rules, merit information, and game mechanics.
- **Usage:**
  - `+lookup <term>` - Search for rules
  - `+lookup/merit <merit>` - Look up merit
  - `+lookup/condition <condition>` - Look up condition

---

## Building & World Management

### `@dig`
Create new rooms and locations.
- **Usage:** `@dig <roomname>[;<alias>]`

### `@open`
Create exits between rooms.
- **Usage:** `@open <exitname>[;<alias>]=<destination>`

### `@desc`
Set descriptions on objects, rooms, and characters.
- **Usage:** `@desc <object>=<description>`

### `@set`
Set attributes and properties on objects.
- **Usage:** `@set <object>/<attribute>=<value>`

### `@create`
Create new objects.
- **Usage:** `@create <objectname>`

### `@destroy`
Destroy objects (use with caution).
- **Usage:** `@destroy <object>`

### `+npc`
Create and manage NPCs.
- **Usage:**
  - `+npc/create <name>` - Create NPC
  - `+npc/set <npc>/<stat>=<value>` - Set NPC stats
  - `+npc/list` - List your NPCs
  - `+npc/delete <npc>` - Delete NPC

---

## Staff & Admin Commands

### `+admin`
Administrative commands for game management.
- **Usage:** Various admin functions (restricted to admin+)

### `+template`
Manage character templates and splats.
- **Usage:**
  - `+template <character>=<template>` - Set template
  - `+template/list` - List available templates

### `+area`
Manage game areas and zones.
- **Usage:**
  - `+area/create <name>` - Create area
  - `+area/set <area>/<attribute>=<value>` - Set area properties

---

## Jobs & Request System

### `+jobs` (aliases: `+requests`, `+request`, `+job`, `+myjobs`, `myjobs`, `myjob`)
Request and jobs management system.
- **Player Commands:**
  - `+jobs` - List your jobs
  - `+jobs/open` - List open jobs
  - `+jobs/create <queue>=<title>/<description>` - Create new job
  - `+jobs <id>` - View specific job
  - `+jobs/comment <id>=<comment>` - Add comment to job
  - `+jobs/close <id>` - Close your job (if resolved)
- **Staff Commands:**
  - `+jobs/all` - List all jobs
  - `+jobs/queue <queue>` - List jobs in queue
  - `+jobs/assign <id>=<staff>` - Assign job
  - `+jobs/status <id>=<status>` - Change status
  - `+jobs/priority <id>=<priority>` - Set priority
  - `+jobs/tag <id>=<tag>` - Add tag
  - `+jobs/approve <id>` - Approve job
  - `+jobs/deny <id>=<reason>` - Deny job
- **Common Queues:** BUILD, BUG, CHARGEN, EQUIP, PLOT, ADMIN, IDEA

---

## Bulletin Board System

### `+bbs` (aliases: `bbs`, `@bbs`, `bb`, `+bb`)
Bulletin board system for announcements and discussions.
- **Usage:**
  - `+bbs` - List all boards
  - `+bbs <board>` - List posts on board
  - `+bbs <board>/<post>` - Read specific post
  - `+bbs/post <board>/<title>=<message>` - Create new post
  - `+bbs/reply <board>/<post>=<message>` - Reply to post
  - `+bbs/delete <board>/<post>` - Delete your post
  - `+bbs/edit <board>/<post>=<new message>` - Edit your post
  - `+bbs/subscribe <board>` - Subscribe to board
  - `+bbs/unsubscribe <board>` - Unsubscribe from board
  - `+bbs/search <board>=<text>` - Search posts
- **Staff Commands:**
  - `+bbs/create <name>` - Create new board
  - `+bbs/remove <board>/<post>` - Remove any post
  - `+bbs/lock <board>` - Lock board
  - `+bbs/unlock <board>` - Unlock board

### `+bbpost` (aliases: `bbpost`)
Quick post to BBS.
- **Usage:** `+bbpost <board>/<title>=<message>`

### `+bbread` (aliases: `bbread`)
Quick read from BBS.
- **Usage:** `+bbread <board>/<post>`

---

## Special Commands

### `look` (aliases: `l`)
Look at your surroundings or specific objects.
- **Usage:** 
  - `look` - Look at room
  - `look <object>` - Look at object
  - `look <character>` - Look at character

### `inventory` (aliases: `i`, `inv`)
View your inventory.
- **Usage:** `inventory`

### `get` (aliases: `take`)
Pick up objects.
- **Usage:** `get <object>`

### `drop`
Drop objects from inventory.
- **Usage:** `drop <object>`

### `give`
Give objects to others.
- **Usage:** `give <object> to <character>`

### `@password`
Change your account password.
- **Usage:** `@password <old password>=<new password>`

### `help`
Access the help system.
- **Usage:** 
  - `help` - List help categories
  - `help <topic>` - Get help on topic
  - `help <command>` - Get help on command

---

## Important Notes

### Global Search & Alias Support

**Global Character Targeting:**
- All character-targeting commands search the entire game world by default
- You can target any character anywhere, not just in your current location
- Commands work on both **online and offline characters** (except communication commands)
- No need to be in the same room to use commands like `+finger`, `+stat`, `+sheet`, etc.
- Communication commands (`page`, `+txt`) require the target to be online to receive messages

**Alias System:**
- Players can set short aliases with `alias me=<name>`
- All 71+ character-targeting commands support aliases
- Aliases work exactly like character names in every command
- Case-insensitive matching (finds "lys", "Lys", "LYS")
- Globally unique (no two characters can have the same alias)

**Examples:**
```
alias me=Lys                    # Set your alias
page Lys=Hello!                 # Works with alias (if Lys is online)
+finger Lys                     # Works with alias (offline ok, global)
+stat Lys/strength=3            # Staff can use aliases (offline ok, global)
+sheet Lys                      # View sheet (offline ok, global)
+combat/attack Lys              # Works in combat (MUST be same room + online)
+mystery/grant Lys=1/clue0      # Grant clue (offline ok, global)
+note/approve Lys=Title         # Approve note (offline ok, global)
```

**Commands Requiring Target Online:**
- `page`, `tell` - Sending messages
- `+txt` - Text messaging
- `+sheet/show <player>` - Showing sheet to specific player
- `+note/show <title>=<player>` - Showing note to specific player
- **All combat commands** - Combat requires online, same-room targets

**Commands Requiring Same Location:**
- **All combat commands** - Must be in same room to fight
- Most roleplay commands (`say`, `pose`, `emote`)
- Room-specific interactions

**Commands Working Offline (Global Search):**
- `+finger` - View character info
- `+stat` - Set/view stats (staff)
- `+sheet` - View character sheet  
- `+mystery/grant` - Grant clues
- `+group/add` - Add to groups
- `+condition`, `+tilt` - Manage status (staff)
- `+note/approve` - Approve notes (staff)
- Most admin and staff commands

### Permission System

- **Player Commands:** Available to all players
- **Storyteller Commands:** Require storyteller flag (`+storyteller/add`)
- **Staff Commands:** Require builder/staff permissions
- **Admin Commands:** Require admin permissions
- Each command's help text indicates permission requirements

### Legacy Mode

Some features change when Legacy Mode is enabled:
- **Disabled in Legacy:** Aspirations, modern Conditions system, Tilts
- **Enabled in Legacy:** Virtue/Vice only, Changing Breeds support
- **Toggle:** `+legacy/on` or `+legacy/off`
- **Check Status:** `+legacy`

### Help System

- Use `help` to see all help categories
- Use `help <command>` for detailed command help
- Use `+lookup <term>` to search game mechanics
- All commands have detailed help text with examples

---

## Quick Reference Card

### Essential Commands
```
+sheet              - View character sheet
+roll <dice>        - Roll dice
page <char>=<msg>   - Send private message
say <text>          - Speak in room
pose <action>       - Perform action
+who               - See who's online
+xp                - View/manage experience
+jobs              - View/create jobs
+bbs               - Access bulletin boards
look               - Look around
inventory          - Check inventory
help <topic>       - Get help
```

### Combat Quick Reference
```
+combat/start      - Start combat
+combat/join       - Join combat
+combat/attack <target> - Attack (same room + online only)
+combat/dodge      - Dodge
+combat/next       - Next turn
+combat/status     - Combat status
```

**Important:** All combat targets must be in the same room and online.

### Social Quick Reference  
```
page <char>=<msg>  - Private message
+txt <char>=<msg>  - IC text message
+watch/add <char>  - Watch friend
+finger <char>     - View OOC info
+alts              - View/manage alts
alias me=<name>    - Set your alias
```

---

*For detailed help on any command, use: `help <command>`*
