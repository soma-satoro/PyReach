"""
Promethean: The Created - Elpides and Torments

Elpis (Hope) represents what the Promethean is learning about humanity.
Torment represents the dark side of the Promethean's nature.
"""

# Dictionary of Elpides with their descriptions
ELPIDES = {
    "courage": {
        "name": "Courage",
        "description": "Courage isn't lack of fear so much as the ability to act despite fear. Seeing weak and fragile humans put fear aside to stand up to what terrifies them is inspiring, even to other humans.",
        "witness": "Someone fighting through fear to accomplish something.",
        "act": "The Promethean risking her life, her loved ones, or her Pilgrimage to accomplish something."
    },
    "drive": {
        "name": "Drive",
        "description": "Someone with drive makes the impossible possible. When she has a goal in mind, she never stops for anything short of accomplishing her goals, crushing her enemies, or setting things right. The only thing she can't do is fail.",
        "witness": "Someone continuing onwards when all reason and common sense says she should stop.",
        "act": "Much the same as witnessing — the bar for 'impossible' is raised much higher for Prometheans though, and it's encouraged that this be a suitably awesome moment if the player wants to reach for it."
    },
    "empathy": {
        "name": "Empathy",
        "description": "More than merely understanding that other people feel, having Empathy as Elpis means one day being able to sympathize — to feel what someone feels, to know what it's like. That's something pretty far off for most Created.",
        "witness": "A doctor consoling a terminal patient. Overhearing two friends talking about something serious. An event that shows these people have a connection.",
        "act": "Not just saying 'I feel for you' — that's mimicry, not empathy. To act on her Elpis, the Promethean must understand what the other person is going through, relate it to her own events, and follow through."
    },
    "fear": {
        "name": "Fear",
        "description": "Fear is a natural response to things — not just a human response, but a living response all the same. The Created usually know their limits, but that's not the same as fear.",
        "witness": "Being scared or startled doesn't do the trick. Terror is what really draws forth the fear response — dreadful anticipation.",
        "act": "Everyone gets scared. Prometheans in particular know about dread and anxiety. To truly master fear, a Promethean fear for her life, her Pilgrimage, or the life of another."
    },
    "fury": {
        "name": "Fury",
        "description": "For too many people, anger comes easily, but someone with Fury as her Elpis likely doesn't know what it's like to feel true hatred. Luckily, Disquiet gives plenty of examples to learn from.",
        "witness": "The Promethean sees someone lashing out in anger in a completely unrestrained fashion.",
        "act": "The Promethean feels unrelenting fury at someone or something, whether it is justified or not."
    },
    "inspiration": {
        "name": "Inspiration",
        "description": "Humans create. They see the natural state of the world and they seek to alter it — for convenience, for utility, or for beauty. Inspiration is seeing or experiencing something and being moved to action.",
        "witness": "The Promethean might act as a muse, leading people to create stories, art, or to make some sort of change in their lives.",
        "act": "The Promethean takes inspiration from her circumstances, from a human being, or from a throngmate and creates something."
    },
    "joy": {
        "name": "Joy",
        "description": "The high point of the human condition, Joy is about making what came before it worthwhile, giving things a reason, and being able to look back on even her darkest hour and say 'This was worth it' because in that moment, everything is perfect.",
        "witness": "Find someone having a great day and find out why. This can quickly be spoiled by Disquiet, so it takes a light touch.",
        "act": "Unlike other Elpides, the act for this Elpis means bringing someone else joy, true unadulterated happiness. If a Promethean acting on this Elpis only has ten minutes with someone, she'd better make this the greatest ten minutes of their lives."
    },
    "love": {
        "name": "Love",
        "description": "A connection deeper than any other, Love is regarded as a remarkable power in nearly every human society for good reason.",
        "witness": "The Promethean has to look at two people that are together, know they love each other, and most importantly, know why — witnessing some act of affection that's not phoned in or obligated.",
        "act": "Building a connection to someone strong enough to be called 'love' is almost impossible thanks to Disquiet, but there's nothing that says it has to be requited love. The Promethean just has to have someone she cares about above all else, someone she'd die for. Sometimes it comes to that."
    },
    "sorrow": {
        "name": "Sorrow",
        "description": "Sorrow has no happy ending, or great meaning, or justification. It's something going wrong, and accepting that it's gone wrong. Reflecting on the thing that's put one in such a sorry state, and using it to move forward.",
        "witness": "Not just someone in despair, but someone reflecting on that turmoil and examining what went wrong and why. Since this is usually an internal process, speaking with someone to learn their story is usually a must.",
        "act": "This most easily comes in the aftermath of Torment. For the Promethean, it's about self-awareness, understanding, and moving on. She must know why she's so upset and how to avoid it in the future."
    },
    "pain": {
        "name": "Pain",
        "description": "In some very specific cases, pain is good. It's necessary to sacrifice to achieve something, and sacrifice hurts. A lot of things hurt, but they're for the best. Understanding and accepting that pain isn't always a thing to be avoided is critical to these Prometheans.",
        "witness": "Unfortunately, no small amount of humanity is willing to inflict pain on others, but this is about sacrifice — the party being hurt has to be willing to take that pain for some greater good.",
        "act": "A Promethean must know true agony and know it furthers some cause that matters to her. Leaving a loved one to stave off Disquiet or withstanding torture to protect someone are both examples of fulfilling the Pain Elpis. Torment doesn't count for the purposes of this Elpis, even if she intentionally induces it."
    }
}

# Dictionary of Torments with their descriptions
TORMENTS = {
    "alienated": {
        "name": "Alienated",
        "description": "This Promethean feels like the eternal Other. No matter how much she's learned or how close to the New Dawn she may be, she always feels like she doesn't belong with anyone.",
        "act": "The Promethean expresses discomfort at being in a group of people and causes a problem as a result."
    },
    "awkward": {
        "name": "Awkward",
        "description": "Even for Prometheans, someone with the Awkward torment is an oddball. She has trouble integrating into any conversation, even among her fellow Created, and her trains of thought often produce strange or off-putting ideas.",
        "act": "Accomplishing some task in a strange or backwards fashion. This does not mean the Awkward Promethean doesn't complete whatever task she may have set out to do, just that she does it in a strange way."
    },
    "dejection": {
        "name": "Dejection",
        "description": "What's the point? Nothing you do is good enough. Everything is mediocre at best.",
        "act": "Finding a way to accomplish something that doesn't require your involvement. After all, if you got involved, it would only end in tears."
    },
    "logical": {
        "name": "Logical",
        "description": "The Promethean doesn't understand the unreasonable. She is far from emotionless; she simply doesn't understand anything that isn't rational and logical.",
        "act": "Doing something logically sound that disregards the emotions of others."
    },
    "merciless": {
        "name": "Merciless",
        "description": "Prometheans often have trouble with right and wrong. To them, mercy is an alien concept.",
        "act": "When opposed by someone, neutralize them with excessive force. The Promethean doesn't necessarily have to kill or even fight. It could be anything, from punching someone out for spilling a coffee, to screaming at the top of her lungs at someone who is five minutes late to a meeting."
    },
    "methodical": {
        "name": "Methodical",
        "description": "Found most often in Prometheans that value plans and structure, everything must be done her way with no deviations.",
        "act": "Insist that everyone involved in a plan follow the directions to the letter, with no room for improvisation or last-minute changes."
    },
    "obsession": {
        "name": "Obsession",
        "description": "The dark mirror of Drive, Obsessed Prometheans are focused on one thing, and one thing only. An accomplishment they bring about, an enemy that must be destroyed. They hunt this goal with no regard for anything, even their life.",
        "act": "Do something that puts yourself or your Throng in danger, but furthers the goal you obsess over."
    },
    "paranoia": {
        "name": "Paranoia",
        "description": "They're all out to get you. Nobody's on your side. When they say you're their friend? That's a lie.",
        "act": "Withholding crucial information, hiding or covering up something that would help the targets of your Paranoid delusions."
    },
    "passion": {
        "name": "Passion",
        "description": "The dark side of emotions like love, Passion is emotion overwhelming everything else. It usually leads to bad decisions.",
        "act": "Take an action that brings you closer to what you're passionate about, even if it's dangerous or doesn't make sense."
    },
    "naive": {
        "name": "Naïve",
        "description": "A Naïve Promethean lacks simple concepts like 'personal space' and 'subtlety.' Despite her best efforts, she finds herself constantly upsetting someone or falling for some trick.",
        "act": "The Promethean's lack of understanding of human society causes a setback for her or the throng."
    }
}

# Lists for validation
ALL_ELPIDES = list(ELPIDES.keys())
ALL_TORMENTS = list(TORMENTS.keys())


def get_elpis_info(elpis_name):
    """
    Get information about a specific Elpis.
    
    Args:
        elpis_name (str): Name of the Elpis
        
    Returns:
        dict: Elpis information or None if not found
    """
    return ELPIDES.get(elpis_name.lower())


def get_torment_info(torment_name):
    """
    Get information about a specific Torment.
    
    Args:
        torment_name (str): Name of the Torment
        
    Returns:
        dict: Torment information or None if not found
    """
    return TORMENTS.get(torment_name.lower())

