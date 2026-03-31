import secrets
from typing import List, Tuple, Literal, Set
from enum import Enum

class RollType(Enum):
    """Types of dice rolls in Chronicles of Darkness."""
    NORMAL = "normal"      # Standard roll
    EIGHT_AGAIN = "8-again"  # Roll again on 8 or higher
    NINE_AGAIN = "9-again"   # Roll again on 9 or higher
    TEN_AGAIN = "10-again"   # Roll again on 10
    ROTE = "rote"         # Reroll all failed dice once
    REFLEXIVE = "reflexive" # Reflexive action (no action cost)
    DAMAGE = "damage"      # Damage roll (no wound penalties)

def roll_dice(dice_pool: int, difficulty: int = 8, roll_types: Set[RollType] = None) -> Tuple[List[int], int, int]:
    """
    Roll dice for Chronicles of Darkness 2nd Edition.

    Args:
        dice_pool (int): The number of dice to roll.
        difficulty (int): The difficulty of the roll (default 8 for CoD).
        roll_types (Set[RollType]): Set of roll types to apply (can combine multiple types).

    Returns:
        Tuple[List[int], int, int]: A tuple containing:
            - List of individual die results (including again rolls)
            - Number of successes
            - Number of ones (potential botches)
    """
    if roll_types is None:
        roll_types = {RollType.NORMAL}

    all_rolls = []
    successes = 0
    ones = 0

    # Handle chance die case (when dice pool is 0 or negative)
    if dice_pool <= 0:
        roll = secrets.randbelow(10) + 1
        all_rolls.append(roll)
        if roll >= difficulty:
            successes = 1
        elif roll == 1:
            ones = 1
        return all_rolls, successes, ones

    # Function to handle a single die roll with again rules
    def roll_with_again(again_threshold: int) -> List[int]:
        rolls = []
        roll = secrets.randbelow(10) + 1
        rolls.append(roll)
        
        # Handle again rule
        while roll >= again_threshold:
            roll = secrets.randbelow(10) + 1
            rolls.append(roll)
            
        return rolls

    # Determine again threshold based on roll types
    again_threshold = 10  # Default to 10-again
    if RollType.EIGHT_AGAIN in roll_types:
        again_threshold = 8
    elif RollType.NINE_AGAIN in roll_types:
        again_threshold = 9
    elif RollType.TEN_AGAIN in roll_types:
        again_threshold = 10

    # Roll the initial dice pool
    initial_rolls = []
    for _ in range(dice_pool):
        rolls = roll_with_again(again_threshold)
        initial_rolls.append(rolls)
        all_rolls.extend(rolls)
        
        # Count successes and ones from initial rolls
        for roll in rolls:
            if roll >= difficulty:
                successes += 1
            if roll == 1:
                ones += 1

    # Handle rote action - reroll all failed dice once
    if RollType.ROTE in roll_types:
        rote_rolls = []
        for rolls in initial_rolls:
            # If none of the rolls were successes, reroll once
            if not any(roll >= difficulty for roll in rolls):
                roll = secrets.randbelow(10) + 1
                rote_rolls.append(roll)
                all_rolls.append(roll)
                if roll >= difficulty:
                    successes += 1
                if roll == 1:
                    ones += 1

    return all_rolls, successes, ones

def interpret_roll_results(successes: int, ones: int, rolls: List[int] = None, diff: int = 8, 
                         roll_types: Set[RollType] = None, dice_pool: int = None, modifier: int = 0) -> str:
    """
    Interpret the results of a dice roll for Chronicles of Darkness.
    
    Args:
        successes (int): Number of successes
        ones (int): Number of ones rolled
        rolls (List[int]): List of all dice rolls (including again rolls)
        diff (int): Difficulty of the roll (default 8 for CoD)
        roll_types (Set[RollType]): Set of roll types applied
        dice_pool (int): Original dice pool size (before modifiers)
        modifier (int): Modifier applied to the roll
        
    Returns:
        str: Formatted message describing the roll results
    """
    if roll_types is None:
        roll_types = {RollType.NORMAL}

    # Format success count with color
    if successes == 0:
        success_string = f"|w{successes}|n"
    elif successes > 0:
        success_string = f"|g{successes}|n"  # Green for successes
    else:
        success_string = f"|r{successes}|n"

    # Add roll types to message
    roll_type_str = ""
    if roll_types != {RollType.NORMAL}:
        type_descriptions = []
        if RollType.EIGHT_AGAIN in roll_types:
            type_descriptions.append("8-again")
        if RollType.NINE_AGAIN in roll_types:
            type_descriptions.append("9-again")
        if RollType.TEN_AGAIN in roll_types:
            type_descriptions.append("10-again")
        if RollType.ROTE in roll_types:
            type_descriptions.append("rote")
        if RollType.REFLEXIVE in roll_types:
            type_descriptions.append("reflexive")
        if RollType.DAMAGE in roll_types:
            type_descriptions.append("damage")
        if type_descriptions:
            roll_type_str = f" ({', '.join(type_descriptions)})"

    msg = f"|w(|n{success_string}|w)|n{roll_type_str}"
    
    # Add Success/Successes text - dramatic failure only on chance dice
    if successes == 0 and ones >= 1 and dice_pool is not None and dice_pool + modifier <= 0:
        msg += f"|r Dramatic Failure!|n"
    elif successes >= 5:
        msg += f"|g Exceptional Success!|n"
    elif successes > 0:
        msg += " Success"
    else:
        msg += " Failure"
    
    # Format dice results with color
    if rolls:
        msg += " |w(|n"
        colored_rolls = []
        
        # Sort the rolls but keep track of their original positions
        roll_info = [(i, roll) for i, roll in enumerate(rolls)]
        roll_info.sort(key=lambda x: (-x[1], x[0]))  # Sort by value (descending) then position
        
        for i, (orig_pos, roll) in enumerate(roll_info):
            if roll == 1:
                # Ones are always red
                colored_rolls.append(f"|r1|n")
            elif roll >= diff:
                # Regular successes are green
                colored_rolls.append(f"|g{roll}|n")
            else:
                # Regular non-successes are white
                colored_rolls.append(f"|w{roll}|n")
        
        msg += " ".join(colored_rolls)
        msg += "|w)|n"
    
    return msg

def roll_to_job_display(successes: int, ones: int, rolls: List[int], dice_pool: int, 
                       roll_types: Set[RollType], modifier: int = 0, 
                       stat_name: str = None, skill_name: str = None, 
                       stat_value: int = None, skill_value: int = None,
                       character_name: str = None, wound_penalty: int = 0) -> str:
    """
    Create a single-line formatted dice roll display.
    
    Args:
        successes (int): Number of successes
        ones (int): Number of ones rolled
        rolls (List[int]): List of all dice rolls
        dice_pool (int): Original dice pool size
        roll_types (Set[RollType]): Set of roll types applied
        modifier (int): Modifier applied to the roll
        stat_name (str): Name of the stat rolled (if applicable)
        skill_name (str): Name of the skill rolled (if applicable)
        stat_value (int): Value of the stat (if applicable)
        skill_value (int): Value of the skill (if applicable)
        character_name (str): Name of the character making the roll
        wound_penalty (int): Wound penalty from health damage
        
    Returns:
        str: Single-line formatted roll result
    """
    # Determine the roll description
    final_pool = dice_pool + modifier + wound_penalty
    
    if stat_name and skill_name:
        modifier_parts = []
        if modifier != 0:
            modifier_parts.append(f"{modifier:+d}")
        if wound_penalty != 0:
            modifier_parts.append(f"{wound_penalty:+d} (wound)")
        
        if modifier_parts:
            modifier_str = " " + " ".join(modifier_parts)
            roll_desc = f"{stat_name.title()} + {skill_name.title()}{modifier_str}"
        else:
            roll_desc = f"{stat_name.title()} + {skill_name.title()}"
    elif stat_name:
        modifier_parts = []
        if modifier != 0:
            modifier_parts.append(f"{modifier:+d}")
        if wound_penalty != 0:
            modifier_parts.append(f"{wound_penalty:+d} (wound)")

        if modifier_parts:
            modifier_str = " " + " ".join(modifier_parts)
            roll_desc = f"{stat_name.title()}{modifier_str}"
        else:
            roll_desc = f"{stat_name.title()}"
    else:
        roll_desc = f"{final_pool} dice"
        if wound_penalty != 0:
            roll_desc += f" (includes {wound_penalty:+d} wound penalty)"
    
    # Add chance die indicator
    if final_pool <= 0:
        roll_desc += " |y(Chance Die)|n"
    
    # Format the dice results
    colored_rolls = []
    for roll in sorted(rolls, reverse=True):
        if roll == 1:
            colored_rolls.append(f"|r{roll}|n")
        elif roll >= 8:  # Success
            colored_rolls.append(f"|g{roll}|n")
        else:  # Failure
            colored_rolls.append(f"|w{roll}|n")
    
    dice_display = "(" + " ".join(colored_rolls) + ")"
    
    # Success interpretation
    if successes == 0 and ones >= 1 and final_pool <= 0:
        # Dramatic failure only on chance dice
        result = f"|R{successes} successes (Dramatic Failure)|n"
    elif successes >= 5:
        result = f"|g{successes} successes (Exceptional Success)|n"
    elif successes > 0:
        result = f"|g{successes} successes|n"
    else:
        result = f"|w{successes} successes|n"
    
    # Build the complete message
    name_part = character_name if character_name else "Someone"
    return f"|yROLL>|n {name_part}: {roll_desc} -> {result}. {dice_display}"

def roll_to_room_display(successes: int, ones: int, dice_pool: int, 
                        roll_types: Set[RollType], modifier: int = 0, 
                        stat_name: str = None, skill_name: str = None,
                        character_name: str = None, wound_penalty: int = 0) -> str:
    """
    Create a single-line formatted dice roll display for room observers (without dice details).
    
    Args:
        successes (int): Number of successes
        ones (int): Number of ones rolled
        dice_pool (int): Original dice pool size
        roll_types (Set[RollType]): Set of roll types applied
        modifier (int): Modifier applied to the roll
        stat_name (str): Name of the stat rolled (if applicable)
        skill_name (str): Name of the skill rolled (if applicable)
        character_name (str): Name of the character making the roll
        
    Returns:
        str: Single-line formatted roll result without dice details
    """
    # Determine the roll description
    final_pool = dice_pool + modifier + wound_penalty
    
    if stat_name and skill_name:
        modifier_parts = []
        if modifier != 0:
            modifier_parts.append(f"{modifier:+d}")
        if wound_penalty != 0:
            modifier_parts.append(f"{wound_penalty:+d} (wound)")
        
        if modifier_parts:
            modifier_str = " " + " ".join(modifier_parts)
            roll_desc = f"{stat_name.title()} + {skill_name.title()}{modifier_str}"
        else:
            roll_desc = f"{stat_name.title()} + {skill_name.title()}"
    elif stat_name:
        modifier_parts = []
        if modifier != 0:
            modifier_parts.append(f"{modifier:+d}")
        if wound_penalty != 0:
            modifier_parts.append(f"{wound_penalty:+d} (wound)")

        if modifier_parts:
            modifier_str = " " + " ".join(modifier_parts)
            roll_desc = f"{stat_name.title()}{modifier_str}"
        else:
            roll_desc = f"{stat_name.title()}"
    else:
        roll_desc = f"{final_pool} dice"
        if wound_penalty != 0:
            roll_desc += f" (includes {wound_penalty:+d} wound penalty)"
    
    # Add chance die indicator
    if final_pool <= 0:
        roll_desc += " |y(Chance Die)|n"
    
    # Success interpretation
    if successes == 0 and ones >= 1 and final_pool <= 0:
        # Dramatic failure only on chance dice
        result = f"|R{successes} successes (Dramatic Failure)|n"
    elif successes >= 5:
        result = f"|g{successes} successes (Exceptional Success)|n"
    elif successes > 0:
        result = f"|g{successes} successes|n"
    else:
        result = f"|w{successes} successes|n"
    
    # Build the complete message
    name_part = character_name if character_name else "Someone"
    return f"|yROLL>|n {name_part}: {roll_desc} -> {result}."

def format_roll_display(successes: int, ones: int, rolls: List[int], dice_pool: int, 
                       roll_types: Set[RollType], modifier: int = 0, 
                       stat_name: str = None, skill_name: str = None, 
                       stat_value: int = None, skill_value: int = None,
                       wound_penalty: int = 0) -> str:
    """
    Create a beautifully formatted display box for dice roll results (expansive format for job rolls).
    
    Args:
        successes (int): Number of successes
        ones (int): Number of ones rolled
        rolls (List[int]): List of all dice rolls
        dice_pool (int): Original dice pool size
        roll_types (Set[RollType]): Set of roll types applied
        modifier (int): Modifier applied to the roll
        stat_name (str): Name of the stat rolled (if applicable)
        skill_name (str): Name of the skill rolled (if applicable)
        stat_value (int): Value of the stat (if applicable)
        skill_value (int): Value of the skill (if applicable)
        
    Returns:
        str: Formatted display box
    """
    from evennia.utils.ansi import ANSIString
    
    # Box formatting constants
    width = 69  # Adjusted to match the example
    
    def format_header(title):
        title = f" {title} "
        left_width = (width - len(title) - 4) // 2
        right_width = width - left_width - len(title) - 4
        return f"{'=' * left_width}< {title} >{'=' * right_width}"
    
    def format_footer():
        return "=" * width
    
    def format_divider(title):
        title_with_spaces = f" {title} "
        dashes_needed = width - len(title_with_spaces)
        left_dashes = dashes_needed // 2
        right_dashes = dashes_needed - left_dashes
        return f"{'-' * left_dashes}{title_with_spaces}{'-' * right_dashes}"
    
    def format_line(label, value, label_width=20):
        return f" {label:<{label_width}} : {value}"
    
    # Start building the output
    output = []
    
    # Header
    output.append(format_header("DICE ROLL RESULTS"))
    
    # Roll Information Section
    output.append(format_divider("Roll Information"))
    
    # Determine roll description
    final_pool = dice_pool + modifier + wound_penalty
    if stat_name and skill_name:
        modifier_parts = []
        if modifier != 0:
            modifier_parts.append(f"{modifier:+d}")
        if wound_penalty != 0:
            modifier_parts.append(f"{wound_penalty:+d} (wound)")
        
        if modifier_parts:
            modifier_str = " " + " ".join(modifier_parts)
            roll_desc = f"|g{stat_name.title()}|n + |g{skill_name.title()}|n{modifier_str} (|w{final_pool}|n dice)"
        else:
            roll_desc = f"|g{stat_name.title()}|n + |g{skill_name.title()}|n (|w{final_pool}|n dice)"
    elif stat_name:
        modifier_parts = []
        if modifier != 0:
            modifier_parts.append(f"{modifier:+d}")
        if wound_penalty != 0:
            modifier_parts.append(f"{wound_penalty:+d} (wound)")

        if modifier_parts:
            modifier_str = " " + " ".join(modifier_parts)
            roll_desc = f"|g{stat_name.title()}|n{modifier_str} (|w{final_pool}|n dice)"
        else:
            roll_desc = f"|g{stat_name.title()}|n (|w{final_pool}|n dice)"
    else:
        roll_desc = f"|g{final_pool}|n dice"
        if wound_penalty != 0:
            roll_desc += f" (includes {wound_penalty:+d} wound penalty)"
    
    output.append(format_line("Roll", roll_desc))
    
    # Roll types
    roll_type_descriptions = []
    if RollType.EIGHT_AGAIN in roll_types:
        roll_type_descriptions.append("|g8-again|n")
    elif RollType.NINE_AGAIN in roll_types:
        roll_type_descriptions.append("|g9-again|n")
    elif RollType.TEN_AGAIN in roll_types:
        roll_type_descriptions.append("|g10-again|n")
    
    if RollType.ROTE in roll_types:
        roll_type_descriptions.append("|yRote Action|n")
    if RollType.REFLEXIVE in roll_types:
        roll_type_descriptions.append("|cReflexive|n")
    
    # Only show roll type if it's not normal
    if roll_type_descriptions:
        output.append(format_line("Roll Type", ", ".join(roll_type_descriptions)))
    
    # Results Section
    output.append(format_divider("Results"))
    
    # Success count with result interpretation on same line
    success_color = "|w"
    if successes == 0:
        success_color = "|r"
    elif successes >= 5:
        success_color = "|g"
    elif successes > 0:
        success_color = "|g"
    
    # Interpretation
    if successes == 0 and ones >= 1 and dice_pool + modifier + wound_penalty <= 0:
        interpretation = "|R[DRAMATIC FAILURE]|n"
    elif successes >= 5:
        interpretation = "|G[EXCEPTIONAL SUCCESS]|n"
    elif successes > 0:
        interpretation = "|g[SUCCESS]|n"
    else:
        interpretation = "|r[FAILURE]|n"
    
    output.append(format_line("Successes", f"{success_color}{successes}|n {interpretation}"))
    
    # Dice Results
    if rolls:
        # Sort and color the dice
        colored_rolls = []
        for roll in sorted(rolls, reverse=True):
            if roll == 1:
                colored_rolls.append(f"|r{roll}|n")
            elif roll >= 8:  # Success
                colored_rolls.append(f"|g{roll}|n")
            else:  # Failure
                colored_rolls.append(f"|w{roll}|n")
        
        dice_display = " ".join(colored_rolls)
        output.append(format_line("Dice Rolled", dice_display))
    
    # Footer
    output.append(format_footer())
    
    # Special message for exceptional success (separate from the box)
    if successes >= 5:
        output.append("")
        output.append("|Y|[bExceptional Success achieved! You may add a condition.|n|Y]|n")
        output.append("|yUse: |w+condition/add <condition_name>|n")
    
    return "\n".join(output)