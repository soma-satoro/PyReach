"""
This is the base stat dictionary for Chronicles of Darkness, it contains everything that would be considered
a 'mortal' stat, and is used to create basic characters before applying a supernatural template.
"""

from world.cofd.stat_types import Anchor, Stat, Advantage, Pool

"""
Attribute Dictionary

The attribute dictionary is comprised of the following elements:

- name: The name of the attribute.
- min_value: The minimum value of the attribute.
- max_value: The maximum value of the attribute.
- temp_value: Certain things can increase or decrease an attribute value temporarily, this is what the character typeclass calls to update the attribute value.
- description: A description of the attribute.
- att_type: The type of attribute (power, finesse, resistance).
"""

attribute_dictionary = {
    "strength": Stat(name="strength", min_value=1, max_value=5, temp_value=0, description="Your character's muscular definition and capacity to deliver force. It affects many physical tasks, including most actions in a fight.", att_type="power"),
    "dexterity": Stat(name="dexterity", min_value=1, max_value=5, temp_value=0, description="Your character's speed, agility, and coordination. It provides balance, reactions, and aim.", att_type="finesse"),
    "stamina": Stat(name="stamina", min_value=1, max_value=5, temp_value=0, description="Your character's general health and sturdiness. It determines how much punishment your character's body can handle before it gives up.", att_type="resistance"),
    "presence": Stat(name="presence", min_value=1, max_value=5, temp_value=0, description="Your character's assertiveness, gravitas, and raw appeal. It gives your character a strong bearing that changes moods and minds.", att_type="power"),
    "manipulation": Stat(name="manipulation", min_value=1, max_value=5, temp_value=0, description="Your character's ability to make others cooperate. It's how smoothly they speak, and how much people can read into their intentions.", att_type="finesse"),
    "composure": Stat(name="composure", min_value=1, max_value=5, temp_value=0, description="Your character's poise and grace under fire. It's their dignity and ability to remain unfazed when harrowed.", att_type="resistance"),
    "intelligence": Stat(name="intelligence", min_value=1, max_value=5, temp_value=0, description="Your character's capacity for logic, reasoning, and learning. It represents book smarts and analytical thinking.", att_type="power"),
    "wits": Stat(name="wits", min_value=1, max_value=5, temp_value=0, description="Your character's cunning, perception, and ability to think on their feet. It represents quick thinking and situational awareness.", att_type="finesse"),
    "resolve": Stat(name="resolve", min_value=1, max_value=5, temp_value=0, description="Your character's determination, focus, and emotional fortitude. It represents mental stamina and willpower.", att_type="resistance"),
}

"""
# Skill Dictionary

The skill dictionary is comprised of the following elements:

- name: The name of the skill.
- min_value: The minimum value of the skill.
- max_value: The maximum value of the skill.
- temp_value: Certain things can increase or decrease a skill value temporarily, this is what the character typeclass calls to update the skill value.
- description: A description of the skill.
- skill_type: The type of skill (mental, physical, social).
- unskilled: The dice penalty applied to the skill when the character has no training in it.
"""

skill_dictionary = {
    # Mental Skills
    "academics": Stat(name="academics", min_value=0, max_value=5, temp_value=0, description="A broad Skill representing your character's higher education and knowledge of the arts and humanities. It covers language, history, law, economics, and related fields.", skill_type="mental", unskilled=-3),
    "computer": Stat(name="computer", min_value=0, max_value=5, temp_value=0, description="Your character's advanced ability with computing. The Computer Skill allows your character to program computers, crack into systems, diagnose major problems, and investigate data.", skill_type="mental", unskilled=-3),
    "crafts": Stat(name="crafts", min_value=0, max_value=5, temp_value=0, description="Your character's knack with creating and repairing things. From creating works of art to fixing an automobile, Crafts is the Skill to use.", skill_type="mental", unskilled=-3),
    "investigation": Stat(name="investigation", min_value=0, max_value=5, temp_value=0, description="Your character's skill with solving mysteries and putting together puzzles. It reflects the ability to draw conclusions, find meaning out of confusion, and use lateral thinking.", skill_type="mental", unskilled=-3),
    "medicine": Stat(name="medicine", min_value=0, max_value=5, temp_value=0, description="Your character's knowledge of the human body and how to fix it and keep it in working order. Characters with Medicine can make efforts to stem life-threatening wounds and illnesses.", skill_type="mental", unskilled=-3),
    "occult": Stat(name="occult", min_value=0, max_value=5, temp_value=0, description="Your character's knowledge of things hidden in the dark, legends and lore. While the supernatural is unpredictable and often unique, the Occult Skill allows your character to pick out facts from rumor.", skill_type="mental", unskilled=-3),
    "politics": Stat(name="politics", min_value=0, max_value=5, temp_value=0, description="A general knowledge of political structures and methodologies. More practically, it shows your character's ability to navigate those systems and make them work the way they intend.", skill_type="mental", unskilled=-3),
    "science": Stat(name="science", min_value=0, max_value=5, temp_value=0, description="Your character's knowledge and understanding of the physical and natural sciences, such as biology, chemistry, geology, meteorology, and physics.", skill_type="mental", unskilled=-3),
    # Physical Skills
    "athletics": Stat(name="athletics", min_value=0, max_value=5, temp_value=0, description="A broad category of physical training and ability. It covers sports and basic physical tasks such as running, jumping, dodging threats, and climbing. It also determines a character's ability with thrown weapons.", skill_type="physical", unskilled=-1),
    "brawl": Stat(name="brawl", min_value=0, max_value=5, temp_value=0, description="Your character's ability to tussle and fight without weapons. This includes old-fashioned bar brawls as well as complex martial arts.", skill_type="physical", unskilled=-1),
    "drive": Stat(name="drive", min_value=0, max_value=5, temp_value=0, description="The skill to control and maneuver automobiles, motorcycles, boats, and even airplanes. Drive relates to moments of high stress, such as a high-speed chase or trying to elude a tail.", skill_type="physical", unskilled=-1),
    "firearms": Stat(name="firearms", min_value=0, max_value=5, temp_value=0, description="Your character's ability to identify, maintain, and otherwise use guns. This Skill covers everything from small pistols, to shotguns, to assault rifles, and anything else related.", skill_type="physical", unskilled=-1),
    "larceny": Stat(name="larceny", min_value=0, max_value=5, temp_value=0, description="Covers intrusion, lockpicking, theft, pickpocketing, and other (generally considered) criminal activities. This Skill is typically learned on the streets, outside of formal methods.", skill_type="physical", unskilled=-1),
    "stealth": Stat(name="stealth", min_value=0, max_value=5, temp_value=0, description="Your character's ability to move unnoticed and unheard or blend into a crowd. Every character approaches Stealth differently; some use distraction, some disguise, while some are just hard to keep an eye on.", skill_type="physical", unskilled=-1),
    "survival": Stat(name="survival", min_value=0, max_value=5, temp_value=0, description="Your character's ability to 'live off the land.' This means finding shelter, finding food, and otherwise procuring the necessities for existence in either a rural or urban environment.", skill_type="physical", unskilled=-1),
    "weaponry": Stat(name="weaponry", min_value=0, max_value=5, temp_value=0, description="The ability to fight with hand-to-hand weapons: from swords, to knives, to baseball bats, to chainsaws. If the intent is to strike another and harm them, Weaponry is the right Skill.", skill_type="physical", unskilled=-1),
    # Social Skills
    "animal_ken": Stat(name="animal_ken", min_value=0, max_value=5, temp_value=0, description="Your character's ability to train and understand animals. With Animal Ken, your character can cow beasts or rile them to violence under the right circumstances.", skill_type="social", unskilled=-1),
    "empathy": Stat(name="empathy", min_value=0, max_value=5, temp_value=0, description="Your character's ability to read and understand others' feelings and motivations. This helps discern moods or read deceptive behavior in discussion.", skill_type="social", unskilled=-1),
    "expression": Stat(name="expression", min_value=0, max_value=5, temp_value=0, description="Your character's ability to communicate. This Skill covers written and spoken forms of communication, journalism, acting, music, and dance.", skill_type="social", unskilled=-1),
    "intimidation": Stat(name="intimidation", min_value=0, max_value=5, temp_value=0, description="Your character's ability to influence others' behavior through threats and fear. It could mean direct physical threats, interrogation, or veiled implications of things to come.", skill_type="social", unskilled=-1),
    "persuasion": Stat(name="persuasion", min_value=0, max_value=5, temp_value=0, description="Your character's ability to change minds and influence behaviors through logic, fast-talking, or appealing to desire. It relies on the force of your character's personality to sway the listener.", skill_type="social", unskilled=-1),
    "socialize": Stat(name="socialize", min_value=0, max_value=5, temp_value=0, description="Your character's ability to present themselves well and interact with groups of people. It reflects proper etiquette, customs, sensitivity, and warmth.", skill_type="social", unskilled=-1),
    "streetwise": Stat(name="streetwise", min_value=0, max_value=5, temp_value=0, description="Your character's knowledge of life on the streets. It tells them how to navigate the city, how to get information from unlikely sources, and where they'll be (relatively) safe.", skill_type="social", unskilled=-1),
    "subterfuge": Stat(name="subterfuge", min_value=0, max_value=5, temp_value=0, description="The ability to deceive. With Subterfuge, your character can lie convincingly, project hidden messages in what they say, hide motivations, and notice deception in others.", skill_type="social", unskilled=-1),
}

# Merits are linked to their own specific dictionaries based on merit type and affiliation to supernatural templates

# Merit Types:
# - Physical
# - Social
# - Mental
# - Supernatural
# - Fighting
# - Style

# The above are considered 'mortal' or generic merits that are accessible to any character. Below are supernatural merits that are specific to a particular supernatural template.

# - Changeling
# - Werewolf
# - Vampire
# - Mage
# - Demon
# - Geist
# - Hunter
# - Promethean
# - Beast
# - Renegade
# - Minor-Template (psychics, possessed, etc. any traditional "mortal+" template)

"""
Advantages are any stat that is derived from calculating attributes together.
"""

advantage_dictionary = {
    "integrity": Advantage(name="integrity", min_value=0, max_value=10, temp_value=0, description="", adv_base="7"),
    "size": Advantage(name="size", min_value=0, max_value=10, temp_value=0, description="", adv_base="5"),
    "speed": Advantage(name="speed", min_value=0, max_value=25, temp_value=0, description="", adv_base="strength + dexterity + 5"),
    "health": Advantage(name="health", min_value=0, max_value=20, temp_value=0, description="", adv_base="size + stamina"),
    "power": Advantage(name="power", min_value=0, max_value=30, temp_value=0, description="", adv_base="strength + presence + manipulation"),
    "finesse": Advantage(name="finesse", min_value=0, max_value=30, temp_value=0, description="", adv_base="dexterity + presence + manipulation"),
    "resistance": Advantage(name="resistance", min_value=0, max_value=30, temp_value=0, description="", adv_base="stamina + presence + composure"),
}

"""
Pools are any stat that is can be spent or regained and are used as a resource.
All pools are included here, including ones that are explicitly for supernatural templates.

- health: The amount of health a character has. Derived from size and stamina.
- willpower: The amount of willpower a character has. Derived from resolve and composure.

- essence: The amount of essence a character has. Derived from Primal Urge stat.
  - Primal Urge 1: 10
  - Primal Urge 2: 11
  - Primal Urge 3: 12
  - Primal Urge 4: 13
  - Primal Urge 5: 15
  - Primal Urge 6: 20
  - Primal Urge 7: 25
  - Primal Urge 8: 30
  - Primal Urge 9: 50
  - Primal Urge 10: 75
- blood: The amount of blood a vampire character has. Based on Blood Potency stat.
  - Blood Potency 0: Stamina
  - Blood Potency 1: 10
  - Blood Potency 2: 11
  - Blood Potency 3: 12
  - Blood Potency 4: 13
  - Blood Potency 5: 15
  - Blood Potency 6: 20
  - Blood Potency 7: 25
  - Blood Potency 8: 30
  - Blood Potency 9: 50
  - Blood Potency 10: 75
- glamour: The amount of glamour a changeling character has. Based on Wyrd stat.
  - Wyrd 1: 10
  - Wyrd 2: 11
  - Wyrd 3: 12
  - Wyrd 4: 13
  - Wyrd 5: 15
  - Wyrd 6: 20
  - Wyrd 7: 25
  - Wyrd 8: 30
  - Wyrd 9: 50
  - Wyrd 10: 75
- mana: The amount of mana a mage character has. Derived from Gnosis stat.
  - Gnosis 1: 10
  - Gnosis 2: 11
  - Gnosis 3: 12
  - Gnosis 4: 13
  - Gnosis 5: 15
  - Gnosis 6: 20
  - Gnosis 7: 25
  - Gnosis 8: 30
  - Gnosis 9: 50
  - Gnosis 10: 75
- plasm: The amount of plasm a Geist character has. Based on Synergy stat.
  - Synergy 1: 10
  - Synergy 2: 11
  - Synergy 3: 12
  - Synergy 4: 13
  - Synergy 5: 15
  - Synergy 6: 20
  - Synergy 7: 25
  - Synergy 8: 30
  - Synergy 9: 50
  - Synergy 10: 75
"""

# Pools are the resources that a character can spend or regain.
pool_dictionary = {
    "health": Pool(name="health", min_value=0, max_value=20, temp_value=0, description=""),
    "willpower": Pool(name="willpower", min_value=0, max_value=10, temp_value=0, description=""),
    "essence": Pool(name="essence", min_value=0, max_value=50, temp_value=0, description=""),
    "blood": Pool(name="blood", min_value=0, max_value=50, temp_value=0, description=""),
    "glamour": Pool(name="glamour", min_value=0, max_value=75, temp_value=0, description=""),
    "mana": Pool(name="mana", min_value=0, max_value=50, temp_value=0, description=""),
    "plasm": Pool(name="plasm", min_value=0, max_value=50, temp_value=0, description=""),
}

# Anchors are the core of the character, they are the foundation of the
# character and are used to determine the character's base personality and archetypes.

anchor_dictionary = {
    "virtue": Anchor(name="virtue", min_value=0, max_value=10, temp_value=0, description=""),
    "vice": Anchor(name="vice", min_value=0, max_value=10, temp_value=0, description=""),
    "thread": Anchor(name="thread", min_value=0, max_value=10, temp_value=0, description=""),
    "root": Anchor(name="root", min_value=0, max_value=10, temp_value=0, description=""),
    "mask": Anchor(name="mask", min_value=0, max_value=10, temp_value=0, description=""),
    "dirge": Anchor(name="dirge", min_value=0, max_value=10, temp_value=0, description=""),
    "bloom": Anchor(name="bloom", min_value=0, max_value=10, temp_value=0, description=""),
    "elpis": Anchor(name="elpis", min_value=0, max_value=10, temp_value=0, description=""),
    "torment": Anchor(name="torment", min_value=0, max_value=10, temp_value=0, description=""),
}
