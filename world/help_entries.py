"""
File-based help entries. These complements command-based help and help entries
added in the database using the `sethelp` command in-game.

Control where Evennia reads these entries with `settings.FILE_HELP_ENTRY_MODULES`,
which is a list of python-paths to modules to read.

A module like this should hold a global `HELP_ENTRY_DICTS` list, containing
dicts that each represent a help entry. If no `HELP_ENTRY_DICTS` variable is
given, all top-level variables that are dicts in the module are read as help
entries.

Each dict is on the form
::

    {'key': <str>,
     'text': <str>}``     # the actual help text. Can contain # subtopic sections
     'category': <str>,   # optional, otherwise settings.DEFAULT_HELP_CATEGORY
     'aliases': <list>,   # optional
     'locks': <str>       # optional, 'view' controls seeing in help index, 'read'
                          #           if the entry can be read. If 'view' is unset,
                          #           'read' is used for the index. If unset, everyone
                          #           can read/view the entry.

"""

HELP_ENTRY_DICTS = [
    {
        "key": "mystery_tutorial",
        "aliases": ["mysterysetup", "build_mystery", "mystery_guide"],
        "category": "Roleplaying Tools",
        "text": """
Mystery Creation Tutorial (Staff + Player Flow)

This tutorial walks through creating a full mystery, adding clues, linking clue chains,
setting discovery methods, and testing the player experience.

------------------------------------------------------------
1) Create the mystery
------------------------------------------------------------
Command:
  +mystery/create <title> = <description>

Example:
  +mystery/create The Empty Haven = Residents vanished from a guarded haven with no signs of entry.

Optional admin setup:
  +mystery/edit <id>/category = supernatural
  +mystery/edit <id>/diff = 3
  +mystery/status <id> = active

------------------------------------------------------------
2) Add your first clues
------------------------------------------------------------
Command:
  +mystery/addclue <mystery_id> = <name>/<description>

Examples:
  +mystery/addclue 12 = Disturbed Warding Chalk/A protective circle was erased from the inside.
  +mystery/addclue 12 = Missing Ledger Pages/Three pages were cut cleanly from a haven ledger.
  +mystery/addclue 12 = Witness Statement/A ghoul saw someone leave before dawn.

------------------------------------------------------------
3) Set clue types and methods
------------------------------------------------------------
Use clue type for defaults, or explicit methods for full control.

Type command:
  +mystery/cluetype <mystery_id>/<clue_id> = <academic|occult|physical|hidden|social|general>

Method command:
  +mystery/methods <mystery_id>/<clue_id> = <examine,search,interview,research,occult>

Examples:
  +mystery/cluetype 12/clue_0 = occult
  +mystery/methods 12/clue_1 = research,search
  +mystery/methods 12/clue_2 = interview

------------------------------------------------------------
4) Create clue chains (progression)
------------------------------------------------------------
Require earlier clues before later clues become available.

Command:
  +mystery/prereq <mystery_id>/<clue_id> = <prereq_clue_ids>

Example:
  +mystery/prereq 12/clue_2 = clue_0,clue_1

Optional "leads to" metadata:
  +mystery/leads 12/clue_0 = clue_2
  +mystery/leads 12/clue_1 = clue_2

------------------------------------------------------------
5) Add access rules (optional)
------------------------------------------------------------
Open access:
  +mystery/access 12 = open

Template-restricted:
  +mystery/access 12 = template:vampire

Faction/splat details:
  +mystery/access 12 = clan:mekhet
  +mystery/access 12 = order:guardians_of_the_veil

------------------------------------------------------------
6) Add skill gates (optional)
------------------------------------------------------------
Simple skill roll condition:
  +mystery/skillroll <mystery_id>/<clue_id> = <skill>/<attribute>/<difficulty>

Example:
  +mystery/skillroll 12/clue_1 = academics/intelligence/3

------------------------------------------------------------
7) Test as a player
------------------------------------------------------------
Player discovery loop:
  +mystery
  +mystery/info 12
  +mystery/search
  +mystery/examine <object>
  +mystery/interview <character>
  +mystery/research <topic>
  +mystery/occult <topic>
  +mystery/progress

Room visibility:
Discovered clues relevant to the current room are shown in room look output under:
  Uncovered Leads Here

------------------------------------------------------------
8) Staff diagnostics and corrections
------------------------------------------------------------
See mystery internals:
  +mystery/view 12
  +mystery/discovered 12
  +mystery/staffprogress 12

Grant/revoke clues for testing:
  +mystery/grant <character> = 12/clue_0
  +mystery/revoke <character> = 12/clue_0

Edit clue details:
  +mystery/editclue 12/clue_0 = desc/New clue description
  +mystery/editclue 12/clue_0 = location/haven_basement,elysium_archive
  +mystery/editclue 12/clue_0 = obj/ledger,chalk_circle
  +mystery/editclue 12/clue_0 = social/maeve,the_hound

------------------------------------------------------------
9) Quick template workflow
------------------------------------------------------------
List templates:
  +mystery/templates

Create from template:
  +mystery/template missing_person = Missing Neonate of the Third Court

Then customize with:
  +mystery/view <id>
  +mystery/edit ...
  +mystery/editclue ...

Tip:
Build 3-5 clues first, set 1-2 prerequisites, test with a player alt, then expand.
""",
    },
]
