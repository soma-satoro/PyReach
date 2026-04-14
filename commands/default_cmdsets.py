"""
Command sets

All commands in the game must be grouped in a cmdset.  A given command
can be part of any number of cmdsets and cmdsets can be added/removed
and merged onto entities at runtime.

To create new commands to populate the cmdset, see
`commands/command.py`.

This module wraps the default command sets of Evennia; overloads them
to add/remove commands from the default lineup. You can create your
own cmdsets by inheriting from them or directly from `evennia.CmdSet`.

"""

from evennia import default_cmds

# from mux_compatibility import TinyMuxCmdSet
# from mux_extra_commands import TinyMuxExtendedCmdSet
from .dice_commands import CmdRoll
from .experience import CmdExperience
from .conditions import CmdCondition
from .tilts import CmdTilt
from .CmdSheet import CmdSheet
from .stats import CmdStat, CmdRecalc
from .aspirations import CmdAspiration
from .social import CmdSocial
from .combat import CmdCombat, CmdEquippedGear, CmdCombatHelp, CmdInitiative
from .integrity import CmdIntegrity
from .equipment import CmdEquipment, CmdBuyConfig, CmdBuy, CmdAddResources
from .groups import CmdGroups, CmdRoster, CmdGroupMerit, CmdTotem
from .npc import CmdNPC
from .CmdHealth import CmdHealth
from .template_admin import CmdTemplate
from .admin import CmdConfigOOCIC, CmdApprove, CmdUnapprove, CmdFixGroupTypes
from .building import (CmdAreaManage, CmdRoomSetup, CmdPlaces, CmdRoomInfo, CmdMap, CmdTempRoom)
from .admin_area_init import CmdInitAreaManager
from .mystery_commands import CmdMystery
from .storyteller_admin import CmdStoryteller
from .jobs.jobs_commands import CmdJobs
from commands.commonmux.commonmux_cmdset import CommonMuxCmdSet
from .lookup import CmdLookup
from .voting import CmdVote, CmdRecommend, CmdVoteAdmin
from .test_xp_integration import CmdTestXP
from .CmdLegacy import CmdLegacy
from .ooc_ic_commands import CmdGo, CmdJoin, CmdSummon, CmdReturn
from .coords import CmdCoords
from .hangouts import CmdHangouts
from .bbs.bbs_cmdset import BBSCmdSet
from commands.commonmux.CmdPage import CmdPage
from .shapeshifting import CmdShift, CmdForm
from .character_submit import CmdSubmit
from .reality_commands import CmdMien, CmdMask, CmdReach, CmdLocus, CmdHedge
from .pledges import CmdPledge
from .bio import CmdBio
from .cover import CmdCover
from .demon import CmdDemon
from .census import CmdCensus

# Custom help command that escapes ANSI codes in help text
from .help_custom import CmdHelp
from evennia.contrib.game_systems import mail

class CharacterCmdSet(default_cmds.CharacterCmdSet):
    """
    The `CharacterCmdSet` contains general in-game commands like `look`,
    `get`, etc available on in-game Character objects. It is merged with
    the `AccountCmdSet` when an Account puppets a Character.
    """

    key = "DefaultCharacter"

    def at_cmdset_creation(self):
        """
        Populates the cmdset
        """
        super().at_cmdset_creation()
        #
        # any commands you add below will overload the default ones.
        #
        command_groups = (
            # Core commands
            (CmdRoll, CmdExperience, CmdCondition, CmdTilt, CmdJobs),
            # Sheet management and stat views
            (CmdSheet, CmdHealth),
            # Character management
            (CmdStat, CmdRecalc, CmdAspiration, CmdIntegrity, CmdLookup, CmdLegacy, CmdSubmit, CmdBio, CmdCensus),
            # Shapeshifting (Werewolf)
            (CmdShift, CmdForm),
            # Demon systems
            (CmdCover, CmdDemon),
            # Reality systems (Changeling, Werewolf, Mage)
            (CmdMien, CmdMask, CmdReach, CmdLocus, CmdHedge, CmdPledge),
            # Voting and recommendations
            (CmdVote, CmdRecommend, CmdVoteAdmin),
            # Equipment commands
            (CmdEquipment, CmdBuyConfig, CmdBuy, CmdAddResources),
            # Testing (remove after verification)
            (CmdTestXP,),
            # Social and investigation
            (CmdSocial, CmdMystery, CmdGroups, CmdRoster, CmdGroupMerit, CmdTotem),
            # Combat
            (CmdCombat, CmdInitiative, CmdEquippedGear, CmdCombatHelp),
            # NPCs
            (CmdNPC,),
            # Admin commands
            (CmdTemplate, CmdInitAreaManager, CmdStoryteller, CmdConfigOOCIC, CmdSummon, CmdReturn, CmdApprove, CmdUnapprove, CmdFixGroupTypes),
            # Building commands (areas, rooms, places, mapping)
            (CmdAreaManage, CmdRoomSetup, CmdRoomInfo, CmdPlaces, CmdMap, CmdTempRoom),
            # OOC/IC movement commands
            (CmdGo, CmdJoin, CmdCoords),
            # Hangout commands
            (CmdHangouts,),
            # Custom help command with ANSI stripping to prevent color codes from breaking help text
            (CmdHelp,),
        )
        for group in command_groups:
            for command_cls in group:
                self.add(command_cls())
        
        # CommonMux custom commands
        self.add(CommonMuxCmdSet())
        
        # Melteth BBS commands
        self.add(BBSCmdSet())

        # TinyMUX commands
        # self.add(TinyMuxCmdSet())
        # self.add(TinyMuxExtendedCmdSet())

class AccountCmdSet(default_cmds.AccountCmdSet):
    """
    This is the cmdset available to the Account at all times. It is
    combined with the `CharacterCmdSet` when the Account puppets a
    Character. It holds game-account-specific commands, channel
    commands, etc.
    """

    key = "DefaultAccount"

    def at_cmdset_creation(self):
        """
        Populates the cmdset
        """
        super().at_cmdset_creation()
        #
        # any commands you add below will overload the default ones.
        #
        self.add(mail.CmdMail())
        # Override default page command with our custom one
        self.add(CmdPage())

class UnloggedinCmdSet(default_cmds.UnloggedinCmdSet):
    """
    Command set available to the Session before being logged in.  This
    holds commands like creating a new account, logging in, etc.
    """

    key = "DefaultUnloggedin"

    def at_cmdset_creation(self):
        """
        Populates the cmdset
        """
        super().at_cmdset_creation()
        #
        # any commands you add below will overload the default ones.
        #


class SessionCmdSet(default_cmds.SessionCmdSet):
    """
    This cmdset is made available on Session level once logged in. It
    is empty by default.
    """

    key = "DefaultSession"

    def at_cmdset_creation(self):
        """
        This is the only method defined in a cmdset, called during
        its creation. It should populate the set with command instances.

        As and example we just add the empty base `Command` object.
        It prints some info.
        """
        super().at_cmdset_creation()
        #
        # any commands you add below will overload the default ones.
        #
