from world.cofd.stat_types import Merit

# Hunter-Specific Merits
hunter_merits = [
    # Core Hunter Merits
    Merit(
        name="Back Road Atlas",
        min_value=1,
        max_value=1,
        description="Navigate through urban routes with a +2 to evade an enemy's notice, and gain the Edge in Chases outside of main streets",
        merit_type="mental",
        prerequisite="wits:2,[drive:2,athletics:2]"
    ),
    Merit(
        name="Cover Tracks",
        min_value=1,
        max_value=1,
        description="Wipe all traces of movement and interaction, rolling Intelligence + Survival or Stealth vs. Intelligence + Investigation",
        merit_type="physical",
        prerequisite="[survival:2,stealth:2]"
    ),
    Merit(
        name="Custom Gear Broker",
        min_value=1,
        max_value=3,
        description="Trade any equipment for any other equipment of equal or lesser cost once per chapter. Once per story, treat any merit as one higher when obtaining custom gear",
        merit_type="social",
        prerequisite="socialize:2"
    ),
    Merit(
        name="Face in the Crowd",
        min_value=2,
        max_value=2,
        description="Blend into crowds with a +3 to evade or tail a target, and a -3 to opponents attempting to spot you",
        merit_type="social",
        prerequisite="no_striking_looks"
    ),
    Merit(
        name="Force Multiplier",
        min_value=2,
        max_value=2,
        description="May treat non-Hunters (including supernaturals) as Hunters when using tactics. Requires leading the action yourself and risking more willpower for each participant",
        merit_type="social",
        prerequisite="hunter"
    ),
    Merit(
        name="Gut Feeling",
        min_value=2,
        max_value=2,
        description="Understand when something unnatural is going on with an investigation. Become Obsessed during occult investigations, but roll with +2 on Occult rolls",
        merit_type="mental",
        prerequisite="occult:2"
    ),
    Merit(
        name="Last Stand",
        min_value=2,
        max_value=2,
        description="Once a chapter, Roll Wits + Resolve or Stamina to take one action without penalties",
        merit_type="physical",
        prerequisite="[resolve:3,stamina:3]"
    ),
    Merit(
        name="Lucky Charm",
        min_value=1,
        max_value=1,
        description="While holding the charm, roll Resolve + Composure at the start of a scene. Success suppresses the effects of negative mental Conditions. This action can be taken once per chapter",
        merit_type="supernatural",
        prerequisite="resolve:1,[occult:1,academics:1]"
    ),
    Merit(
        name="Masked Scent",
        min_value=1,
        max_value=1,
        description="Using something to alter or cover scent, roll Wits + Survival or Streetwise to gain the Edge and +1 to all rolls in a chase while being tracked by scent",
        merit_type="physical",
        prerequisite="[survival:2,streetwise:2]"
    ),
    Merit(
        name="Natural Tinkerer",
        min_value=2,
        max_value=2,
        description="Ignore penalties for improvised equipment and materials, with potentially adjusted equipment costs",
        merit_type="mental",
        prerequisite="wits:3,crafts:3"
    ),
    Merit(
        name="Robust Health",
        min_value=2,
        max_value=2,
        description="Substitute Intelligence or Dexterity + Survival for Medicine rolls to heal yourself",
        merit_type="physical",
        prerequisite="survival:3"
    ),
    Merit(
        name="Seance Devotee",
        min_value=1,
        max_value=5,
        description="Know a person per dot of the merit who is willing to help conduct a seance with you",
        merit_type="social",
        prerequisite="occult:2"
    ),
    Merit(
        name="Tactical Insight",
        min_value=2,
        max_value=2,
        description="Roll Wits + Survival or Streetwise to choose when to act in initiative once per chapter. Dodge freely on an exceptional success",
        merit_type="mental",
        prerequisite="wits:3,[survival:2,streetwise:2]"
    ),
    Merit(
        name="Tight Lipped",
        min_value=2,
        max_value=2,
        description="Gain +2 to resist mundane interrogations",
        merit_type="social",
        prerequisite="resolve:2"
    ),
    Merit(
        name="Touchstone",
        min_value=1,
        max_value=5,
        description="Gain an additional touchstone per dot",
        merit_type="social",
        prerequisite="hunter"
    ),
    # Safe Place Features for Hunters
    Merit(
        name="Anathema",
        min_value=1,
        max_value=1,
        description="The Safe Place is warded against monsters with a specific power, prompting a Wits + Resolve - Safe Place roll on any attempt to break through, becoming Immobilized or Stunned on failure.",
        merit_type="supernatural",
        prerequisite="safe_place:1"
    ),
    Merit(
        name="Arsenal",
        min_value=1,
        max_value=1,
        description="Rolls to clean, fix, or improvise equipment gain +2.",
        merit_type="mental",
        prerequisite="safe_place:1"
    ),
    Merit(
        name="Concealed",
        min_value=1,
        max_value=1,
        description="Attempts to find the Safe Place through any means are penalised by -2.",
        merit_type="social",
        prerequisite="safe_place:1"
    ),
    Merit(
        name="Escape Hatch",
        min_value=1,
        max_value=1,
        description="The hunter(s) may roll Dexterity + Athletics or Survival to reach the secret exit without suffering any damage from the environment.",
        merit_type="physical",
        prerequisite="safe_place:1"
    ),
    Merit(
        name="Infirmary",
        min_value=1,
        max_value=1,
        description="Medicine rolls here are improved by +2 for any invested hunter with dots in the skill, and the space may substitute for a hospital for the purposes of injury and recovery.",
        merit_type="mental",
        prerequisite="safe_place:1"
    ),
    Merit(
        name="Home Security System",
        min_value=1,
        max_value=1,
        description="The Safe Place is outfitted with a defense system, penalising attempts to break in by Safe Place dots.",
        merit_type="social",
        prerequisite="safe_place:1"
    ),
]

# Create dictionary for easy lookup
hunter_merits_dict = {merit.name.lower().replace(" ", "_").replace("(", "").replace(")", ""): merit for merit in hunter_merits}

