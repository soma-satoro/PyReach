"""
Demon: The Descent Bio Questions

These questions help define a Demon's relationships and vulnerabilities.
They should be answered as part of character creation and displayed in +bio.
"""

DEMON_BIO_QUESTIONS = [
    {
        "key": "shared_self",
        "question": "Who did you share part of yourself with when you first Fell?",
        "description": "The first person you revealed your true nature to, or who helped you establish your first cover."
    },
    {
        "key": "suspects",
        "question": "Who doesn't know, but suspects you're not human?",
        "description": "Someone who has noticed inconsistencies or strange behavior but hasn't confronted you."
    },
    {
        "key": "leverage",
        "question": "Who could give you up to the angels right now, if they really wanted to?",
        "description": "Someone who has dangerous knowledge about you or could expose your true nature."
    },
    {
        "key": "trust",
        "question": "Who would you trust the truest part of yourself with if you absolutely had to?",
        "description": "The person you would reveal your demonic form to if you had no other choice."
    },
    {
        "key": "smoke_mirrors",
        "question": "Who thinks they have something on you, when all they really have is smoke and mirrors?",
        "description": "Someone who believes they have leverage over you, but you've actually deceived them."
    }
]


def get_demon_questions():
    """Return the list of Demon bio questions."""
    return DEMON_BIO_QUESTIONS


def get_question_by_key(key):
    """Get a specific question by its key."""
    for question in DEMON_BIO_QUESTIONS:
        if question["key"] == key:
            return question
    return None


def format_demon_questions_display(character):
    """Format demon questions for display in +bio."""
    if not hasattr(character.db, 'demon_questions'):
        return None
    
    output = []
    output.append("|wDemon Relationships:|n")
    output.append("")
    
    for question_data in DEMON_BIO_QUESTIONS:
        key = question_data["key"]
        question = question_data["question"]
        answer = character.db.demon_questions.get(key, "<not answered>")
        
        output.append(f"|c• {question}|n")
        output.append(f"  {answer}")
        output.append("")
    
    return "\n".join(output)
