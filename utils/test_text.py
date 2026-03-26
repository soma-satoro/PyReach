"""
Test module for text processing utilities.

Run this to verify that special character substitutions work correctly.
"""

from .text import process_special_characters


def test_special_character_processing():
    """Test various scenarios for special character processing."""
    
    test_cases = [
        # Basic newline
        ("Line 1%rLine 2", "Line 1\nLine 2"),
        
        # Paragraph break
        ("Paragraph 1%r%rParagraph 2", "Paragraph 1\n\nParagraph 2"),
        
        # Tab indentation
        ("Normal text%tIndented text", "Normal text     Indented text"),
        
        # Mixed usage
        ("First line%rSecond line%r%rNew paragraph%tIndented", 
         "First line\nSecond line\n\nNew paragraph     Indented"),
        
        # Multiple tabs
        ("Text%t%tDouble indented", "Text          Double indented"),
        
        # Multiple paragraph breaks
        ("One%r%rTwo%r%rThree", "One\n\nTwo\n\nThree"),
        
        # Empty string
        ("", ""),
        
        # No substitutions
        ("Plain text with no substitutions", "Plain text with no substitutions"),
        
        # Edge case - %r followed by %r%r
        ("Line%r%r%rNext", "Line\n\n\nNext"),
    ]
    
    print("Testing special character processing...")
    
    for i, (input_text, expected) in enumerate(test_cases):
        result = process_special_characters(input_text)
        
        if result == expected:
            print(f"OK Test {i+1} passed")
        else:
            print(f"X Test {i+1} failed")
            print(f"  Input: {repr(input_text)}")
            print(f"  Expected: {repr(expected)}")
            print(f"  Got: {repr(result)}")
    
    print("Testing complete!")


if __name__ == "__main__":
    test_special_character_processing() 