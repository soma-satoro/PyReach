"""
Formatting utility functions for consistent display across the game.

All formatting functions respect ROOM_THEME_COLORS from ServerConfig when set via
+config/theme. Theme colors: header/footer borders, header text, dividers.
"""

from evennia.utils.ansi import ANSIString


def get_theme_colors():
    """
    Get theme colors from server config (ROOM_THEME_COLORS) or defaults.
    
    Returns:
        tuple: (header_color, text_color, divider_color) - single-letter ANSI codes
    """
    try:
        from evennia.server.models import ServerConfig
        theme_colors = ServerConfig.objects.conf("ROOM_THEME_COLORS")
        if theme_colors:
            colors = theme_colors.split(",")
            if len(colors) >= 3:
                return colors[0].strip(), colors[1].strip(), colors[2].strip()
    except Exception:
        pass
    return 'g', 'g', 'g'


def header(text, width=78, char="-", use_theme=True):
    """
    Create a centered header line.
    
    Args:
        text (str): The header text
        width (int): Total width of the header
        char (str): Character for borders (default "-", use "=" for heavier style)
        use_theme (bool): If True, use ROOM_THEME_COLORS from config
        
    Returns:
        str: Formatted header string
    """
    if use_theme:
        header_color, text_color, _ = get_theme_colors()
        border = f"|{header_color}"
        text_style = f"|{text_color}"
    else:
        border = "|b"
        text_style = "|w"
    
    # Strip existing ANSI codes for length calculation
    clean_text = ANSIString(text).clean()
    text_length = len(clean_text)
    
    # Calculate padding
    padding = (width - text_length - 4) // 2  # -4 for "< >" decorations
    
    return f"{border}{char * padding}< {text_style}{text}|n {border}>{char * (width - padding - text_length - 4)}|n"


def footer(width=78, char="-", use_theme=True):
    """
    Create a footer line.
    
    Args:
        width (int): Total width of the footer
        char (str): Character to use (default "-", use "=" for heavier border)
        use_theme (bool): If True, use ROOM_THEME_COLORS from config
        
    Returns:
        str: Formatted footer string
    """
    if use_theme:
        header_color, _, _ = get_theme_colors()
        return f"|{header_color}{char * width}|n"
    return f"|b{char * width}|n"


def section_header(text, width=78, use_theme=True):
    """
    Create a section sub-header line (e.g. "----> Field Name <----").
    Uses same color scheme as header(): border/arrows in header_color, text in text_color.
    
    Args:
        text (str): The section title
        width (int): Total width
        use_theme (bool): If True, use ROOM_THEME_COLORS from config
        
    Returns:
        str: Formatted section header string
    """
    if use_theme:
        header_color, text_color, _ = get_theme_colors()
        border = f"|{header_color}"
        text_style = f"|{text_color}"
    else:
        border = "|b"
        text_style = "|w"
    
    clean_text = ANSIString(text).clean()
    # Format: "----> text <" + dashes; match header: borders in header_color, text in text_color
    dashes = width - len(clean_text) - 8
    if dashes < 0:
        dashes = 0
    return f"{border}----> {text_style}{text}|n{border} <{'-' * dashes}|n"


def divider(width=78, char="-", use_theme=True):
    """
    Create a divider line.
    
    Args:
        width (int): Total width of the divider
        char (str): Character to use for the divider
        use_theme (bool): If True, use ROOM_THEME_COLORS from config
        
    Returns:
        str: Formatted divider string
    """
    if use_theme:
        _, _, divider_color = get_theme_colors()
        return f"|{divider_color}{char * width}|n"
    return f"|b{char * width}|n"


def sheet_section_header(section_name, width=78, use_theme=True):
    """
    Create a sheet-style section header: <----- SECTION NAME ----->
    Used by +sheet and template sheets (geist, mage, demon, deviant).
    
    Args:
        section_name (str): Section title (ANSI codes are stripped, theme text color applied)
        width (int): Total width
        use_theme (bool): If True, use ROOM_THEME_COLORS
        
    Returns:
        str: Formatted section header
    """
    if use_theme:
        _, text_color, divider_color = get_theme_colors()
    else:
        text_color, divider_color = "w", "g"
    
    clean_name = ANSIString(section_name).clean()
    name_length = len(clean_name)
    available_dash_space = width - name_length - 4
    left_dashes = available_dash_space // 2
    right_dashes = available_dash_space - left_dashes
    
    return f"|{divider_color}<{'-' * left_dashes}|n |{text_color}{clean_name}|n |{divider_color}{'-' * right_dashes}>|n"


def format_stat(name, value, width=40):
    """
    Format a stat name and value for display.
    
    Args:
        name (str): Stat name
        value: Stat value
        width (int): Total width for the stat line
        
    Returns:
        str: Formatted stat string
    """
    dots = "." * (width - len(name) - len(str(value)))
    return f"{name}{dots}{value}"
