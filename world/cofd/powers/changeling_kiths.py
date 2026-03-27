"""
Changeling Kith Data for Chronicles of Darkness 2nd Edition.

Kith data including skills, descriptions, blessings, and sources.
Based on Changeling: The Lost 2nd Edition core book, Kith & Kin, and Dark Eras 2.
"""

ALL_KITHS = {
'artist': {'name': 'Artist',
          'skill': 'Crafts',
          'description': 'Artists are not just the painters, the sculptors, the architects, or the '
                         'composers. They are, in a very real way, their art. True Fae rarely '
                         'abduct established artists to make Artist changelings. Novices, amateurs, '
                         "and struggling small-timers might all become Artists. The Gentry don't "
                         'care about the initial quality. What they want is an Artist trained to '
                         'create things solely for them. As part of their durance, Artists often '
                         "develop physical characteristics of their chosen medium. A sculptor's "
                         'skin might become gray and flinty, whereas a painter might have splashes '
                         'of random, vivid colors in their hair. In Arcadia, a prison of their own '
                         'frenzied activity held them. Stopping to rest might mean punishment, '
                         'often in the form of being forced to destroy their own half-finished '
                         "piece, or watching their Keeper do so because it wasn't perfect. As such, "
                         'many Artists are usually extremely protective of their works in progress, '
                         'never letting them see the light of day until they are absolutely '
                         'flawless.',
          'blessing': 'Choose either Crafts or Expression. When the Artist uses a Specialty for art '
                      'with that Skill, achieving three successes counts as an exceptional success. '
                      'Tools of the Trade: A good Artist is never without her tools. She can spend '
                      'a point of Glamour for her player to gain bonus dice equal to her Wyrd, to a '
                      'maximum of +5, on a Crafts or Expression roll with one of her Specialties '
                      'pertaining to creating art. All the necessary implements of her craft '
                      'manifest around her for a scene.',
          'book': 'CTL 2e 51'},
 'bright_one': {'name': 'Bright One',
               'skill': 'Socialize',
               'description': "Few things turn a True Fae's head more than genuine passion. It "
                              "doesn't matter what that passion is for -- the arts, the sciences, a "
                              "political movement, a lover, it's all the same to the Gentry. They "
                              'see it as a fire, burning in the soul and setting the creature who '
                              'feels it alight. Humans the Others take because of this passion '
                              'usually become Bright Ones. The True Fae rarely take a Bright One by '
                              'force. They go to lengths to ensnare this prey through her passion. '
                              "Once in Arcadia, the Keeper turns the changeling's passions up to a "
                              'fever pitch, subjecting her to nightmare after nightmare centered on '
                              'the things she loves, and punishing her if she shows any emotion. '
                              'She becomes a Bright One when the built-up rage and anguish explode '
                              'out of her in a flood of light and fury. Subtlety is not an option '
                              'for these changelings -- their mien radiates a soft glow always.',
               'blessing': 'When the Bright One uses Socialize to be the center of attention, '
                           'achieving three successes counts as an exceptional success. Flare: A '
                           'Bright One always has a visible glow, even in the darkest of rooms, '
                           'though the Mask normally prevents mortals from seeing it. She can spend '
                           'a point of Glamour to turn this glow up to a dazzling brilliance that '
                           'blinds her enemies for one turn; the Mask does not obscure this light. '
                           'Each turn the Bright One uses this blessing, each enemy that can see '
                           'her takes a point of bashing damage and rolls at a -2 on all Physical '
                           'and Mental actions that turn.',
               'book': 'CTL 2e 52'},
 'chatelaine': {'name': 'Chatelaine',
               'skill': 'Empathy',
               'description': 'Chatelaines are the perfect servants. Taken to Arcadia by Gentry '
                              'with a taste for the finer things in life, these changelings are '
                              'butlers, stewards, housekeepers, and domestic workers of all '
                              'stripes. Their Keepers choose them for their attention to detail, '
                              'throwing them into their durance with no training and the full '
                              'expectation that they will provide exactly what the Fair Ones want, '
                              'when they want it. Rare is the Gentry who keeps just one Chatelaine. '
                              'A new changeling in a Fae household is expected to learn from the '
                              'older, more established servants. Keepers rarely have to punish '
                              'their Chatelaines directly; a simple sign of displeasure is more '
                              'than enough to send the household scrambling to chastise the errant '
                              'changeling. Chatelaines quickly learn to work within a system, using '
                              "others' power to survive while serving a capricious master.",
               'blessing': "When the Chatelaine uses Empathy to determine a target's immediate "
                           'desires, achieving three successes counts as an exceptional success. '
                           'Will That Be All?: Spend a point of Glamour to activate this blessing '
                           'for the scene. With a successful Manipulation + Socialize roll, a '
                           'Chatelaine may use the Social Merits of one other character in the '
                           'scene as though they were her own. When the effect ends, characters act '
                           'as though the target had used the Merits himself.',
               'book': 'CTL 2e 52'},
 'gristlegrinder': {'name': 'Gristlegrinder',
                   'skill': 'Brawl',
                   'description': 'Gristlegrinders are the cannibalistic nightmares of other '
                                  "changelings. Strictly speaking, they don't need the flesh of the "
                                  "Lost to survive -- they're more like living garbage disposals "
                                  'who developed a taste for fae flesh while in Arcadia. Many '
                                  'Gentry keep them around as cooks, guard dogs, and implicit '
                                  'threats to their own slaves. The ones that do generally had some '
                                  'emptiness inside before their captivity, be it grief from a '
                                  'breakup or a death, loss of direction in life after a stressful '
                                  'event, or just burnout. Almost every Gristlegrinder has tasted '
                                  'changeling flesh at some point. Many actually ate their way out '
                                  'of Arcadia, whether by devouring the hobgoblins and nightmares '
                                  'standing in their way, or chewing a hole through the Hedge. The '
                                  "devouring doesn't stop when they leave Arcadia. Their hunger is "
                                  'all-consuming, be it for love, blood, money, or simply more '
                                  'food.',
                   'blessing': 'When the Gristlegrinder uses Brawl to grapple someone with intent '
                               'to eat them, achieving three successes counts as an exceptional '
                               'success. To Serve Man: A Gristlegrinder can make bite attacks that '
                               'deal lethal damage, without needing to grapple a foe first. If she '
                               'holds something or grapples someone of a smaller Size than herself, '
                               'she can swallow it (or them) whole. She spends a point of Glamour '
                               'and her jaw expands to the necessary size. With a successful '
                               'Stamina + Survival roll, she gets the target down with minimal '
                               "effort. A Gristlegrinder's digestive system deals two points of "
                               'lethal damage per turn. Targets attacking the changeling from '
                               'inside her must deal at least five points of lethal damage with a '
                               "single attack to break out, but she can't apply her Defense or "
                               'armor against such attacks.',
                   'book': 'CTL 2e 53'},
 'helldiver': {'name': 'Helldiver',
              'skill': 'Larceny',
              'description': 'Occasionally, the True Fae need to get places that even they cannot '
                             'reach. Sometimes they need a spy or a thief in their byzantine '
                             'intrigues, someone who would go unnoticed and unaffected. When they '
                             'feel like engaging in espionage, the Others create Helldivers. '
                             'Helldivers are unusual among changelings in that their Keepers not '
                             'only expect them to leave Arcadia, but encourage them to do so. This '
                             'does not free them, though. Even in their otherworldly forms, '
                             'still-captive Helldivers have a silver thread attached to their '
                             'person leading back to their Keeper. All Helldivers know the '
                             'excruciating pain of being yanked out of another realm unexpectedly '
                             "to face their Keeper's wrath. Once the thread breaks, the Helldiver "
                             'is free. Whether captive or free, Helldivers are never in one place '
                             'for long. They are always chasing some new rumor of a rare token, '
                             'exploring alien realms, or listening in on conversations they really '
                             'should not. Helldivers are hungry for knowledge. After all, knowledge '
                             'is power.',
              'blessing': 'When the Helldiver uses Larceny in the Hedge, Arcadia, or another '
                          'unearthly realm, achieving three successes counts as an exceptional '
                          'success. Dive: Spend a Glamour point to make a Dexterity + Occult roll. '
                          'On a success, the Helldiver begins to fade into an incorporeal, '
                          'invisible form. It takes a number of turns equal to (10 - her current '
                          'Clarity), to a minimum of one full turn, to completely fade. While '
                          'fading, the Helldiver cannot take any non-reflexive actions or interact '
                          'with objects or people, and attacks with a non-magical component pass '
                          'harmlessly through her. Once she completely fades, she acts like a '
                          'dematerialized Hedge ghost, unable to physically interact with anything '
                          'except other immaterial beings and objects. She can spend as much time '
                          'as she likes Diving, but she still requires basic necessities. To end '
                          'this effect, spend another Glamour point and make another Dexterity + '
                          'Occult roll to fade back into the world at the same rate.',
              'book': 'CTL 2e 53'},
 'hunterheart': {'name': 'Hunterheart',
                'skill': 'Investigation',
                'description': 'If animals have souls, they are not the sort of souls the Gentry '
                               'can grab onto and twist into shapes to serve their otherworldly '
                               'needs. Hunterhearts are the wild animals of Arcadia, the feral eyes '
                               'peeking out from the Hedge. Not all Hunterhearts are Beasts, but '
                               'all spend their durances consumed with the urge to chase, to hunt, '
                               'to kill. The True Fae usually take changelings who become '
                               'Hunterhearts for their mix of ambition and insecurity. A '
                               "Hunterheart's durance is always red of tooth and claw. While this "
                               "kith sees more Beasts than most, its members' behavior hews more to "
                               'the mythic archetypes of such creatures than to any Darwinian '
                               "textbook. True Fae don't care that male lions are whiny layabouts "
                               '-- lions in Faerie are proud, noble hunters. Similarly, wolves are '
                               'mysterious loners, panthers are sleek and sexual, and sharks are '
                               'cunning and dispassionate. What matters most is the chase, the '
                               'fight, and the next meal.',
                'blessing': 'Choose either Investigation or Survival. When the Hunterheart uses the '
                            'chosen Skill to track down creatures from Faerie, achieving three '
                            'successes counts as an exceptional success. Pounce: If the target can '
                            "see the Hunterheart's eyes, the changeling may spend a point of "
                            'Glamour to lock the target in place or cause him to flee in terror. '
                            "The Hunterheart's player rolls Presence + Wyrd as an instant action, "
                            "contested by the target's Composure + Supernatural Tolerance. The "
                            'target gains the Insensate Tilt or the Frightened Condition if the '
                            "Hunterheart is successful, chosen by the target's player. If the "
                            'changeling attacks the frozen or fleeing target, her unarmed attacks '
                            'deal lethal damage.',
                'book': 'CTL 2e 54'},
 'leechfinger': {'name': 'Leechfinger',
                'skill': 'Medicine',
                'description': 'If vampires exist, they cannot become changelings. That is the '
                               'generally held opinion among the Lost. However, the thought of the '
                               'Byronic undead ideal entrances humanity -- mysterious, dreamy-eyed, '
                               'and stealing the life of those around them. The True Fae have '
                               'seized on this dream to create the Leechfinger. The Gentry draw '
                               'Leechfingers from mortals who take. This definition is broad: A '
                               'Leechfinger could have been a manipulative user, a cold contract '
                               'killer, a kind-hearted fundraiser, or a polite financial '
                               'professional. Anyone who builds their identity around taking and '
                               'receiving in some way could make a good Leechfinger. In Faerie, '
                               'they are weapons against the slaves of other Gentry and instruments '
                               "of torture against their own Keeper's troublesome servants. With a "
                               'touch, they steal life and vitality, leaving their victims dazed '
                               'and fatigued. In the mortal world, other changelings know they '
                               'exist. They look at even the kindest Leechfinger with suspicion.',
                'blessing': 'When the Leechfinger uses Medicine to determine the health of a '
                            'potential target, achieving three successes counts as an exceptional '
                            'success. Sap The Vital Spark: If the Leechfinger maintains physical '
                            'contact with a target for a full turn, she may spend a point of '
                            'Glamour to inflict a point of bashing damage. This heals the '
                            'Leechfinger, either downgrading one aggravated wound to lethal, one '
                            'lethal to bashing, or one bashing to fully healed. As long as the '
                            'Leechfinger maintains contact, she can spend a point of Glamour each '
                            'turn to continue the effect. If the target is a changeling, the '
                            'Leechfinger inflicts two points of damage per Glamour instead, and '
                            'thus heals or downgrades two points of damage per turn.',
                'book': 'CTL 2e 55'},
 'mirrorskin': {'name': 'Mirrorskin',
               'skill': 'Stealth',
               'description': 'The True Fae are capricious, ever carried by their whims. Their '
                              'actions seem illogical, their emotions mercurial, and their desires '
                              'nonsensical. Changelings never really know their Keepers. However, '
                              'the True Fae are one thing consistently: themselves. That is how the '
                              'Mirrorskins escaped. In Arcadia, everything is what it is. '
                              'Mirrorskins are anything and everything -- or, at least, they can '
                              'appear to be so. In Arcadia, where appearance is everything, this is '
                              'a huge advantage. True Fae who create Mirrorskins keep a close eye '
                              'on them, using them as spies, showpieces, or sometimes literal '
                              'mirrors. Change and disguise are their weapons, and how they '
                              'escaped. When they twist and turn and lose themselves in the Mask, '
                              'that is when their Keepers lose them, too. In the mortal world, they '
                              'are unmatched in the art of disguise. The sorts of changelings who '
                              'might become Mirrorskins were people pleasers before. They tried to '
                              'be whatever they could to delight those around them, or at least '
                              'avoid negative consequences.',
               'blessing': 'When the Mirrorskin uses Stealth while in disguise, achieving three '
                           'successes counts as an exceptional success. Mercurial Visage: A '
                           'Mirrorskin may mold and shape her appearance like putty, making an '
                           'entirely new Mask out of composite pieces of people she has met or seen '
                           'in photos. Spend a point of Glamour and make a reflexive Wits + '
                           'Subterfuge + Wyrd roll, with no penalties for lacking equipment. For an '
                           'extra point of Glamour, the changeling can build a new composite mien '
                           'as well. Supernatural abilities that would pierce her deception prompt '
                           'a Clash of Wills. This effect lasts indefinitely, but the changeling '
                           'must use it again even to return to her own natural appearance.',
               'book': 'CTL 2e 55'},
 'nightsinger': {'name': 'Nightsinger',
                'skill': 'Expression',
                'description': 'Song is an art almost as old as humanity itself, and something that '
                               'utterly fascinates the True Fae. While they have otherworldly music '
                               'of their own, the Gentry love human songs for the endless depths of '
                               'their emotional expression. Nightsingers are the kith who produce '
                               'many of the magical songs the creatures in fairy tales teach heroes '
                               'or children. Nightsingers were creative types before Faerie stole '
                               'them away, and not just musicians. The True Fae have odd and '
                               'exacting ideas about what makes a good song, so a changeling who '
                               'produces a less-than-satisfactory piece runs the risk of severe '
                               'retribution. Most Nightsingers escape while their Keepers are in '
                               'the throes of exquisite agony from a song sad enough to make a '
                               'stone weep, or doubled over in laughter from a bawdy take on a '
                               'solemn hymn. Nightsingers find that, once they have escaped, their '
                               'songs hold less power in the solid, consistent mortal world. They '
                               'are far from powerless, however. The other Lost quietly fear their '
                               'ability to completely enthrall others with their song.',
                'blessing': 'When the Nightsinger uses Expression to sing or compose a piece of '
                            'music, achieving three successes counts as an exceptional success. '
                            'Siren Song: Spend a point of Glamour and roll Presence + Expression + '
                            'Wyrd as an instant action, contested with Composure + Supernatural '
                            "Tolerance by anyone who hears the Nightsinger's unearthly song. Anyone "
                            'who fails gains the Swooned Condition and is rooted to the spot for as '
                            'long as the Nightsinger continues to sing; the changeling can take a '
                            "victim's hand and lead him along with her, but otherwise he cannot "
                            'move, although he can still apply his Defense against attacks. Jarring '
                            'him out of it requires an opposing power (prompting a Clash of Wills), '
                            'dealing him at least as much damage as his Stamina rating, or making '
                            'it impossible for him to hear the song anymore.',
                'book': 'CTL 2e 56'},
 'notary': {'name': 'Notary',
           'skill': 'Politics',
           'description': 'Not all pledges are signed on paper or carved into stone. Some are '
                          'literally living documents. Notaries are changelings who preside over '
                          "pledges between True Fae and others. A Notary's Keeper writes these "
                          "agreements in the changeling's blood, etches them across her skin, and "
                          'imprints them on her soul. She is both witness and oath, and her Keeper '
                          'closely supervises her, lest its pledge vanish into the Thorns. This '
                          'makes a Notary extremely dangerous in the mortal world. A True Fae will '
                          'stop at nothing to retrieve a lost pledge, sending Huntsmen, loyalists, '
                          'and even other True Fae after escaped Notaries. Many freeholds would not '
                          'bother keeping such ticking time bombs around if they were not so '
                          'incredibly valuable. Notaries escape by finding loopholes in the pledges '
                          'that bind them to the Others and walking right out the front door. In '
                          'Lost courts, they are often viziers, lawyers, mediators, and -- if all '
                          'else fails -- tricksters who outsmart the True Fae into leaving their '
                          'freehold alone for yet another season. A Notary can perfectly recite any '
                          'pledge she officiates.',
           'blessing': 'When the Notary uses Politics to negotiate, read, or interpret a fae '
                       'pledge, achieving three successes counts as an exceptional success. '
                       'Abatement: Once per chapter, a Notary can completely negate the need for '
                       'Glamour in a pledge as long as she is involved in its creation, without a '
                       'roll. Thereafter, the Notary can perfectly recite the pledge as long as it '
                       'lasts.',
           'book': 'CTL 2e 57'},
 'playmate': {'name': 'Playmate',
             'skill': 'Persuasion',
             'description': 'Each member of the Playmate kith is shaped according to the whims of '
                            'the specific True Fae who made her. Every Playmate reflects the '
                            'specific attachment style of his or her Keeper, and every Playmate is '
                            'made to feel needed. Mortals who already felt lost and alone most '
                            'often become members of this kith. Adult children reeling from the '
                            'deaths of parents, new divorcees, and college dropouts are just some '
                            'examples. The True Fae promise structure, connection, and love. It is '
                            'an open secret that most Playmates who now exist in the mortal world '
                            'did not escape. Their Keepers grew bored with them and tossed them '
                            'into the Hedge. Many Playmates blame themselves -- after all, if they '
                            'had been better, would their Keepers not have loved them? Playmates '
                            'occupy an odd spot in changeling society. On the one hand, they were '
                            'let go, not chased, so many Lost view them with suspicion. On the '
                            'other hand, Playmates have an extremely valuable blessing and are '
                            'usually willing to help out wherever possible.',
             'blessing': 'When the Playmate uses Persuasion to make someone like her or her '
                         'friends, achieving three successes counts as an exceptional success. '
                         'Coeur Loyal: A Playmate may touch a wounded character and spend a point '
                         'of Glamour to heal any number of bashing or lethal damage points as an '
                         'instant action. She takes the same amount of mild Clarity damage as '
                         'bashing damage healed, and the same amount of severe Clarity damage as '
                         'lethal damage healed; apply the mild damage first. She cannot heal more '
                         'damage than she has room to take more Clarity damage. It is entirely '
                         'possible for a Playmate to lose herself completely while healing others.',
             'book': 'CTL 2e 57'},
 'snowskin': {'name': 'Snowskin',
             'skill': 'Subterfuge',
             'description': 'Faerie is not all exploding chaos and wild whimsy. Sometimes it is '
                            'cold, still, and quiet, like a snowfall on a winter night. In palaces '
                            'of glittering ice, or at the bottom of freezing oceans filled with all '
                            'manner of unearthly creatures, Keepers enforce a frigid peace at the '
                            'end of an icicle spear. Their servants become Snowskins to better '
                            'survive their chilling durances. Members of this kith have, at the '
                            'very least, an unusually low body temperature. Some develop ice '
                            'crystals in their hair, or constantly fogging breath. Before the Fae '
                            'took them, Snowskins were stable and self-sufficient. Their durances '
                            'sharpened this to a fine point, teaching them not to trust anyone or '
                            'anything other than their own capabilities. It is this total freezing '
                            "of the heart and soul that allows a Snowskin to evade his Keeper's "
                            'tender mercies long enough to escape Arcadia. Bright, expressive souls '
                            'attract the Gentry, not lumps of ice and shadow. Snowskins usually '
                            'escape unnoticed once they force this change of heart. Even once back '
                            'in the mortal world, some never warm up to their fellow Lost, and '
                            'those who do form extremely strong attachments to those they let in.',
             'blessing': 'When the Snowskin attempts to use Subterfuge to hide her feelings from '
                         'others, achieving three successes counts as an exceptional success. Heart '
                         "of Ice: A Snowskin's derision is more vicious than a howling blizzard. "
                         'When she attempts to shut someone down in front of an audience, spend a '
                         'point of Glamour and roll Presence + Intimidation + Wyrd, contested by '
                         "the target's Composure + Supernatural Tolerance. If the Snowskin "
                         'succeeds, her target gains the Shaken Condition and suffers a -2 on all '
                         'Social rolls involving other changelings until the Condition resolves, as '
                         'her contempt freezes him out of society.',
             'book': 'CTL 2e 58'},
 'absinthial': {'name': 'Absinthial',
               'skill': 'Crafts',
               'description': 'Absinthials brewed fae absinthe for the Gentry, using their own '
                              "dreams as ingredients. Most escaped during their Keepers' fits of "
                              'intoxicated ecstasy. Fickle, perfectionistic, and creative, they '
                              'insist on doing things their way and do not take criticism lying '
                              'down. Some continue brewing in the mortal world; others settle for '
                              'rendering people paralyzed by their presence alone.',
               'blessing': 'When crafting anything consumable with fae ingredients using Crafts, '
                           "three successes count as an exceptional success. Green Fairy's Curse: "
                           'Once per scene, spend a Glamour and touch a target. Roll Presence + '
                           'Crafts + Wyrd contested by Composure + Wyrd; success inflicts the '
                           'Insensate Tilt. When the Insensate effect ends, the target suffers the '
                           'Confused Condition. Does not work on True Fae or Huntsmen.',
               'book': 'Kith 88'},
 'climacteric': {'name': 'Climacteric',
                'skill': 'Investigation',
                'description': 'Climacterics served as living timepieces and stage managers in '
                               "Arcadia, pulling down nights and raising suns at their Keepers' "
                               'command. They represent both immense value and incredible danger '
                               'for freeholds -- their blessing allows near-complete battlefield '
                               'control, but its use serves as a beacon to Huntsmen. Many quietly '
                               'keep to themselves, taking joy in strategy games and long-term '
                               'planning.',
                'blessing': 'When attempting to identify patterns with Investigation, three '
                            'successes count as an exceptional success. En Prise: Whenever a '
                            'Climacteric is present when anyone rolls Initiative, she may spend a '
                            'Glamour to choose one character to automatically act at the top of the '
                            'Initiative order without a roll. She cannot choose herself.',
                'book': 'Kith 88'},
 'concubus': {'name': 'Concubus',
             'skill': 'Empathy',
             'description': 'Concubi spent their nights with their Keepers as nocturnal companions, '
                            'plunging into shared madness with alien minds while enduring desperate '
                            'stretches of daytime isolation. Few other changelings have experienced '
                            'what passes for Gentry dreams. Some miss the role enough to return; '
                            'others find work as therapists, courtesans, and oneiropomps for the '
                            'Lost.',
             'blessing': 'When breaking into a Bastion with Empathy, three successes count as an '
                         'exceptional success. Valerian and Violence: When a Concubus gains the '
                         'Dream Infiltrator Condition by sleeping next to the target for six hours, '
                         'she can remove one non-persistent mental or psychosomatic Condition as a '
                         'paradigm shift costing three successes. Resolving a Persistent Condition '
                         'requires three consecutive six-hour shifts, the Dream Intruder Condition, '
                         'and performing both subtle and paradigm shifts inside the Bastion.',
             'book': 'Kith 89'},
 'draconic': {'name': 'Draconic',
             'skill': 'Brawl/Weaponry',
             'description': 'Draconic changelings are modeled on the mythic beasts of Faerie -- '
                            'thick horns, scales, heavy leathery wings. They find themselves too '
                            'big for the mortal world: too loud, too present, too much. Some build '
                            "hoards; others join motleys and fuss over their people's well-being. "
                            'Once settled, Draconics guard their people and things with unmatched '
                            'ferocity.',
             'blessing': 'Choose either Brawl or Weaponry. When the Draconic defends a person, '
                         'place, or thing she cares about with that Skill, three successes count as '
                         'an exceptional success. None Dare Resist: Spend an extra Glamour while '
                         'scouring her Mask and make a display of dominance to inflict Frightened '
                         'on all opponents who can perceive her. Additionally, spend a Glamour as a '
                         'reflexive action to fly for turns equal to Wyrd at Speed 60; aerial '
                         'charges gain +2 to the attack roll.',
             'book': 'Kith 90'},
 'flowering': {'name': 'Flowering',
              'skill': 'Socialize',
              'description': "Flowering changelings blossomed among Arcadia's strange flora, "
                             'trained by their durances to make others look good. Many find it '
                             'difficult to readjust to being their own masters. Their hypnotic '
                             'scent creates dependency in those around them -- some abuse this '
                             "power, some try to act in the freehold's interest, and others seclude "
                             'themselves to avoid unduly influencing anyone.',
              'blessing': 'When convincing someone they need her with Socialize, three successes '
                          'count as an exceptional success. Seductive Fragrance: Spend a Glamour '
                          'and roll Presence + Empathy. For the scene, anyone in her presence '
                          'contests with Composure + Wyrd; those who fail suffer the Leveraged '
                          'Condition regarding the Flowering. Spend another Glamour during the '
                          'scene to also inflict Frightened, Reckless, or Swooned on a Leveraged '
                          'target.',
              'book': 'Kith 90'},
 'ghostheart': {'name': 'Ghostheart',
               'skill': 'Perception',
               'description': 'Ghosthearts disposed of the dead in Faerie -- burying, burning, '
                              'sinking, or cooking them. Shunned by other changelings, they found '
                              'companionship among the unquiet dead, and it was often these ghosts '
                              'who led them to escape. Other Lost find them creepy at best, but a '
                              'Ghostheart has many ephemeral friends happy to harass anyone who '
                              'hurts her.',
               'blessing': 'When making a perception roll with Wits + Composure to see manifest '
                           'ghosts or other ghostly Twilight entities (including Helldivers), three '
                           'successes count as an exceptional success. Friends in Strange Places: '
                           'Start play with three extra dots of Retainers representing ghosts, each '
                           "with one chosen Numen (other than Clarity Drain, Entrap, and Keeper's "
                           'Calling). May buy more Allies dots for additional ghosts.',
               'book': 'Kith 91'},
 'moonborn': {'name': 'Moonborn',
             'skill': 'Empathy/Intimidation',
             'description': 'Moonborn were kept in constant Bedlam, run through thousands of '
                            'emotions in quick succession until they had no basis for comparison. '
                            'Every piece of stable emotional footing they have was fought for. Some '
                            'help new Lost find their feet; a few exist outside freeholds entirely, '
                            'inflicting on others the same chaos that was carved into them.',
             'blessing': "Choose Empathy or Intimidation. When changing someone's emotional state "
                         'with the chosen Skill, three successes count as an exceptional success. '
                         'Full Moon Catharsis: Once per chapter, spend a Glamour and roll '
                         'Manipulation + Expression to Incite Bedlam in up to Wyrd targets, '
                         'contested by Composure + Wyrd. Inflict one of the following on all who '
                         'fail: Competitive, Frightened, Reckless, Lethargic, or Wanton.',
             'book': 'Kith 92'},
 'uttervoice': {'name': 'Uttervoice',
               'skill': 'Intimidation',
               'description': 'Uttervoices come from frustrated creatives whose blocked feelings '
                              'were shaped into a weapon. Instead of a masterpiece, their voice '
                              'became a claymore. Some refuse to speak above a whisper; others take '
                              'care to remind people what weight their voice carries. When your '
                              'primary communication contains violence, relating to others gets '
                              'complicated.',
               'blessing': 'When using their voice to Intimidate, three successes count as an '
                           'exceptional success. Scream of Agony: Spend a Glamour and scream -- '
                           'roll Presence + Wyrd contested by Composure + Wyrd for everyone who '
                           "hears. Failure inflicts one bashing; the Uttervoice's exceptional "
                           'success upgrades it to lethal. Can scream each turn until out of '
                           'Glamour. Ignores Durability below 2, shatters glass. Accidentally '
                           'activates on Presence rolls affecting supernatural phenomena that '
                           'benefit from 8-again.',
               'book': 'Kith 92'},
 'delver': {'name': 'Delver',
           'skill': 'Investigation',
           'description': "Delvers mined Arcadia's depths in near-solitude, pushed to find the next "
                          'gemstone or raise lost treasures. Most lost their voices in some lonely '
                          'tunnel. They communicate through coded tapping vibrations carried '
                          'through the earth. After escape, they form tight communities and often '
                          'find professional success through patience and persistence.',
           'blessing': 'When making Investigation rolls to find what was lost or hidden, three '
                       'successes count as an exceptional success. Tappingspeak: Spend a Glamour to '
                       'send encrypted tapped messages through earth-connected surfaces to declared '
                       'recipients within Wyrd miles. Recipients understand innately. Other Delvers '
                       'may intercept; non-Delvers need supernatural means to decode. Spend a '
                       'Glamour and roll Investigation to decode intercepted messages.',
           'book': 'Kith 93'},
 'glimmerwisp': {'name': 'Glimmerwisp',
                'skill': 'Persuasion',
                'description': "Glimmerwisps threw protective fogs over the Gentry's atrocities, "
                               'hiding their worst excesses from other changelings. The Gentry '
                               "didn't need them to do this -- they just enjoyed having a servant "
                               'whose job was covering up cruelty. Escaping is easy enough: just '
                               'breeze through the Hedge. In the mortal world, some use the skill '
                               'for triage and crisis response; others keep hiding things that '
                               'should be confronted.',
                'blessing': 'When using Persuasion to redirect attention away from something '
                            'horrible or wonderful, three successes count as an exceptional '
                            'success. Concealing Mist: Spend a Glamour to fill a room (or open '
                            'space up to 10 yards) with perfumed mist. Roll Manipulation + '
                            'Persuasion + Wyrd, contested by Resolve + Composure. Those who lose '
                            'cannot see the wrongdoing of anyone else within the mist. Lasts until '
                            'end of scene.',
                'book': 'Kith 94'},
 'gremlin': {'name': 'Gremlin',
            'skill': 'Crafts',
            'description': 'Gremlins feel the push and pull of perfection and obsession, with the '
                           'same outlet: destruction. Miss a stitch? Rip out the whole thread. One '
                           'wrong line of code? Delete the file. Before Arcadia, they were '
                           'engineers, editors, sculptors, chefs -- brilliant workaholics. The '
                           'Gentry promised them workshops and glory, then tore their work apart '
                           'with even more gusto.',
            'blessing': 'When making a Crafts roll to fix a broken or flawed item, three successes '
                        'count as an exceptional success. Nightmare at 20,000 Feet: Once per scene, '
                        'spend a Glamour to turn an extended action into an instant action, as long '
                        'as something needs to be torn down or destroyed as part of the process.',
            'book': 'Kith 94'},
 'manikin': {'name': 'Manikin',
            'skill': 'Socialize',
            'description': 'Manikins are living canvases: runway models, animatronic creatures, '
                           'scarecrows, caryatids supporting a roof. Often at the bottom of the '
                           'pecking order among servants. Many Gentry keep a wide variety and dump '
                           'them when moving on to the next project. Manikins know how to present '
                           'themselves and fit into any situation without drawing the wrong kind of '
                           'attention.',
            'blessing': 'When using Socialize to fit into any situation, three successes count as '
                        'an exceptional success. Gold From Straw: Spend a Glamour and roll Presence '
                        "+ Crafts to hide an object's flaws for a scene. Gain successes (up to +5) "
                        'as bonus on social rolls. When used to adjust an impression in Social '
                        'maneuvering, the impression level raises an extra step. Does not actually '
                        'improve quality -- only how it is perceived.',
            'book': 'Kith 95'},
 'oculus': {'name': 'Oculus',
           'skill': 'Persuasion',
           'description': 'Oculi are not clairvoyant, but they have a gift for making people see '
                          'things their way. In Arcadia they mediated negotiations between Gentry, '
                          'but also put down uprisings among slaves. The first thing they learn is '
                          "that everyone has a price, even people who think they don't. Expert "
                          'bargainers, they rarely abandon negotiations no matter how poorly things '
                          'are going.',
           'blessing': 'When using Persuasion to get someone to consider her point of view, three '
                       'successes count as an exceptional success. Amaurosis Fugax: Spend a Glamour '
                       'and roll Presence + Persuasion + Wyrd contested by Resolve + Wyrd to '
                       'obscure all paths save hers. Whether via literal clouded vision or mental '
                       "block, the Oculus guides her target's destination.",
           'book': 'Kith 95'},
 'polychromatic': {'name': 'Polychromatic',
                  'skill': 'Empathy',
                  'description': 'Polychromatics were kept around by Keepers for their soothing '
                                 'display of shifting colors, sometimes used as emotional '
                                 'modulators at large gatherings. Their wonder lies in their '
                                 'incredible inoffensiveness -- safe beauty that demands nothing of '
                                 "others. Some just walked out of Arcadia's front gates, flashing "
                                 'signals of safety. They make excellent mediators and crisis '
                                 'counselors.',
                  'blessing': 'When using Empathy to soothe nerves or temper, three successes count '
                              'as an exceptional success. Prismatic Heart: Once per chapter, spend '
                              'a Glamour to cause a bright display of light and color. All other '
                              'characters must spend Willpower or suffer the Swooned Condition. '
                              'Swooned characters take an additional -2 on rolls to resist the '
                              "Polychromatic's Empathy for the rest of the scene.",
                  'book': 'Kith 96'},
 'veneficus': {'name': 'Veneficus',
              'skill': 'Survival',
              'description': 'Venefici toiled in Gentry kitchens or gathered ingredients in '
                             'Arcadian woods. They can look at two identical plants and know which '
                             'heals and which kills. Before abduction, they believed in the healing '
                             'power of food -- instead of saying sorry, they bought coffee; instead '
                             'of saying I love you, they baked a cake. They can just have more of '
                             'an effect now.',
              'blessing': 'When making a Survival roll to identify Goblin fruits, three successes '
                          'count as an exceptional success. Waste Not, Want Not: Spend a Glamour to '
                          'reflexively make a toxic plant edible, or vice versa.',
              'book': 'Kith 97'},
 'witchtooth': {'name': 'Witchtooth',
               'skill': 'Intimidation',
               'description': 'Witchtooths are the keepers of wild and abandoned places -- forests, '
                              'coves, salt flats, empty housing projects. Modeled on figures like '
                              'Baba Yaga and Black Annis, though the old stories got it wrong. They '
                              'prize freedom above all and harvest Glamour through scaring '
                              'travelers. Despite stereotypes, they form strong attachments and '
                              'serve as tough teachers to those they judge worthy.',
               'blessing': 'When targeting a mortal with Intimidation, three successes count as an '
                           'exceptional success. Nibble, Nibble, Little Mouse: Spend a Glamour and '
                           'roll Resolve + Intimidation to reshape the land within one square mile '
                           'to look how she wants. Lasts for turns equal to Wyrd and imposes -1 on '
                           'Survival rolls in the area.',
               'book': 'Kith 97'},
 'bricoleur': {'name': 'Bricoleur',
              'skill': 'Crafts/Expression',
              'description': 'Bricoleurs trade in symbolism and see potential links between '
                             'unrelated things. Their durance was transmutative -- they realized '
                             'language is not a rule and used it to escape. They think in crooked '
                             'lines, which can make them hard to befriend. Many become overly '
                             'enamored of their own cleverness, but they are valuable allies who '
                             'think well on their feet.',
              'blessing': 'Choose a Crafts or Expression specialty at character creation. When '
                          'rolling that skill and specialty, three successes count as an '
                          'exceptional success. Creatio Ex Nihilo: Spend a Glamour and roll Wits + '
                          'Persuasion to change a core truth about herself (hair color, age, etc.) '
                          'for days equal to Wyrd. Requires a thematically appropriate item. '
                          'Everyone else believes the change. The same transformation happens '
                          'permanently to her fetch.',
              'book': 'Kith 98'},
 'cloakskin': {'name': 'Cloakskin',
              'skill': 'Social',
              'description': 'Cloakskins are invisible to mortal eyes under their Mask -- only '
                             'their shadow remains visible, even in direct sunlight. Many were '
                             'wallflowers before abduction. Being unseen gets old fast, and most '
                             'cannot return to their old lives. They tend to be nomadic, turning to '
                             'the internet for social connection where no one needs to see your '
                             'face.',
              'blessing': 'The Cloakskin receives +1 bonus die to all Social rolls. Now You See Me: '
                          'Spend a Glamour and roll Presence + Stealth + Wyrd to make the mien '
                          'disappear from sight for one scene. Others can hear, touch, and smell '
                          'the Cloakskin but not see her; cameras will not record her. Sight-based '
                          'Perception rolls fail; other senses suffer -3.',
              'book': 'Kith 98'},
 'doppelganger': {'name': 'Doppelganger',
                 'skill': 'Empathy',
                 'description': "Doppelgangers don't look exactly like someone, but they can look "
                                'just enough like them to keep everyone off-kilter. A crooked '
                                "smile, a familiar voice, a grandmother's perfume -- they use "
                                'subtle recognition cues to their advantage. Before abduction, they '
                                'believed that if they just changed one thing, someone would '
                                'finally love them.',
                 'blessing': "When using Empathy to gain someone's confidence, three successes "
                             "count as an exceptional success. Sea-Witch's Bargain: Spend a Glamour "
                             'and roll Presence + Empathy + Wyrd contested by Resolve + Wyrd to '
                             'steal a physical or auditory trait as part of her Mask for days equal '
                             'to Wyrd. The target loses the trait until it expires or they complete '
                             'an assigned task to win it back early.',
                 'book': 'Kith 99'},
 'lethipomp': {'name': 'Lethipomp',
              'skill': 'Empathy',
              'description': 'Lethipomps do not feel pain, anxiety, or much of anything at all. '
                             'Their Keepers gave them water from a river of forgetting, and many '
                             "simply walked out of Arcadia knowing they wouldn't die afraid. They "
                             'can pull emotion out of memories like poison from a wound, offering '
                             'relief from guilt and sorrow -- but the cost is letting memories '
                             'fade.',
              'blessing': 'When using Empathy to guess a secret, three successes count as an '
                          'exceptional success. Waters of Lethe: Spend a Glamour and roll Composure '
                          "+ Empathy + Wyrd (contested) to absorb emotions from a target's known "
                          'memory. The target suffers Lethargic for 24 hours. The Lethipomp suffers '
                          'an appropriate Condition for 12 hours and may Incite Bedlam during that '
                          'time, causing those in range to re-enact the absorbed memory.',
              'book': 'Kith 99'},
 'lullescent': {'name': 'Lullescent',
               'skill': 'Stealth',
               'description': 'Lullescents had their voices removed and were made into listeners -- '
                              'hidden flowers, acoustic mirrors, surveillance fixtures. They spent '
                              'their durance shouting to be heard before realizing there were more '
                              'interesting things to listen to. Their sharp hearing dips into '
                              'ultrasonic and infrasonic ranges. If one is in the freehold, be '
                              'careful with your words.',
               'blessing': 'When using Stealth to eavesdrop, three successes count as an '
                           'exceptional success. Song of Silence: Spend a Glamour to use '
                           'echolocation for measuring distance, navigation, or finding hidden '
                           'objects. A successful Wits + Occult + Wyrd roll also unveils objects '
                           'and beings hidden by magic, requiring a Clash of Wills if the concealer '
                           'is still alive.',
               'book': 'Kith 100'},
 'riddleseeker': {'name': 'Riddleseeker',
                 'skill': 'Investigation',
                 'description': 'Riddleseekers soothed Keepers with new riddles or stood guard over '
                                'treasure, posing questions only two beings knew the answer to. In '
                                'Arcadia, where novelty is currency, running out of questions '
                                'motivated many escapes. Most secretly want to return, if only '
                                'briefly -- dusty mortal tomes no longer scratch the same itch.',
                 'blessing': 'When using Investigation to solve a riddle or puzzle, three successes '
                             'count as an exceptional success. Neck Riddle: Spend a Glamour and '
                             'roll Wits + Expression + Wyrd to persuade a target to resolve a '
                             'conflict with a riddle instead. If the target cannot guess the answer '
                             'within three attempts, they must let the Riddleseeker go without '
                             'pursuing the conflict until after the scene ends.',
                 'book': 'Kith 100'},
 'sideromancer': {'name': 'Sideromancer',
                 'skill': 'Occult',
                 'description': "Sideromancers became attuned to the Wyrd's ripples and now read "
                                'futures through chosen mortal methods -- cards, bones, molten '
                                'lead, automatic writing. They shared a fear of the unknown before '
                                'abduction. Seeing the road ahead by a little is better than seeing '
                                'nothing at all, though they try not to think about the fact that '
                                'the future is not fixed.',
                 'blessing': 'When using an Occult divination Specialty, three successes count as '
                             'an exceptional success. Panomancy: Using her chosen method, spend a '
                             'Glamour and roll Wits + Occult + Wyrd (takes at least five minutes) '
                             'to predict outcomes of promises, pledges, debts, or payments she is a '
                             'primary party to. Ask the Storyteller yes/no questions equal to '
                             'successes during the same scene. Predicting further into the future '
                             'is an automatic dramatic failure.',
                 'book': 'Kith 101'},
 'spiegelbild': {'name': 'Spiegelbild',
                'skill': 'Persuasion',
                'description': 'Spiegelbilder were trapped in mirrors as advisors to the Gentry, '
                               'making friends with the creatures peeking in and with light itself. '
                               'Bound by the twin pillars of reflection and refraction: telling the '
                               'truth does not mean you cannot emphasize some things and minimize '
                               'others. Before abduction, they were the sort of person people spoke '
                               'to in confidence -- and they never kept secrets forever.',
                'blessing': 'When using Persuasion to talk out of making a promise, three successes '
                            'count as an exceptional success. Mirror, Mirror on the Wall: Spend a '
                            'Glamour and roll Wits + Composure to enter mirror space through a '
                            'reflective surface. She can look through mirrors and hear what is on '
                            'the other side. The Wyrd binds her to answer truthfully if anyone asks '
                            'the mirror a question. She can hide her face with Manipulation + '
                            'Stealth + Wyrd contested by Wits + Composure. Breaking the mirror does '
                            'not force her out before end of scene.',
                'book': 'Kith 102'},
 'asclepian': {'name': 'Asclepian',
              'skill': 'Medicine',
              'description': 'Asclepians are clever healers who make do with impossible materials '
                             '-- a crown of flowers as a tourniquet, a camera lens transplanted for '
                             'an eye, mystical chants to close mortal wounds. It does not matter '
                             'what works in the mortal world; an Asclepian might use anything. Rare '
                             'and closely watched in Arcadia, even more in demand among the Lost.',
              'blessing': 'On first aid Medicine rolls, three successes count as an exceptional '
                          'success. Grafting: A touch stabilizes injuries and prevents worsening. '
                          'Spend a Glamour and roll Intelligence + Medicine to perform field '
                          'surgery with cobbled-together tools. Can heal injuries beyond normal '
                          'healing, even if the patient technically died within the last scene. '
                          'Scraps used should have thematic connection to their purpose. All grafts '
                          'become permanent additions. Can also resolve persistent physical '
                          'Conditions; removing a graft causes lethal damage and the Condition '
                          'returns.',
              'book': 'Kith 103'},
 'bridgeguard': {'name': 'Bridgeguard',
                'skill': 'Intimidation',
                'description': 'Bridgeguards are rear-guard legends, forged through twisted and '
                               'unfair challenges until they learned to pick their hill to die on. '
                               'Always outnumbered but never outmaneuvered, they find every edge in '
                               'circumstance, strategy, and terrain. They control the center of '
                               'gravity, forcing confrontations to happen at the time and place of '
                               'their choosing.',
                'blessing': 'When using Intimidation against multiple targets, three successes '
                            'count as an exceptional success. Against the Odds: When outnumbered, '
                            'spend a Glamour and roll Composure + Intimidation. Gain a Defense '
                            'bonus equal to successes rolled and Defense is no longer reduced '
                            'against multiple attacks. Lasts one scene, requires no action.',
                'book': 'Kith 104'},
 'librorum': {'name': 'Librorum',
             'skill': 'Intimidation',
             'description': 'Librorum guarded knowledge for the Gentry -- watching over libraries, '
                            "standing outside seers' temples, ferreting out missing secrets. "
                            'Mortals chosen to become Librorum tend to have mercenary and incurious '
                            'natures, doing their jobs with no questions asked. Most find their way '
                            'home through the very archives they were assigned to protect, taking '
                            'precious stolen knowledge with them.',
             'blessing': 'When rolling Intimidation in pursuit or protection of knowledge, three '
                         'successes count as an exceptional success. Stolen Knowledge: Once per '
                         'chapter, spend a Glamour and roll Intelligence + Occult + Wyrd while '
                         'meditating briefly. Divide successes between Library or Language Merits, '
                         "or apply as a Repository, unlocking purloined knowledge from her Keeper's "
                         'library.',
             'book': 'Kith 104'},
 'liminal': {'name': 'Liminal',
            'skill': 'Survival/Streetwise',
            'description': 'Liminals are creatures of duality and transition, bound to thresholds. '
                           'They were placed in dark woods to test heroes, fashioned into locks on '
                           'vaults, or set at front desks before nightmarish corridors. Many '
                           'twisted their mandate to help others escape -- a sphinx tells her '
                           'simplest riddle, a green man neglects to fill a rabbit hole. Most had '
                           'to be pulled out by other changelings.',
            'blessing': 'When using Survival or Streetwise to navigate, three successes count as an '
                        'exceptional success. Line in the Sand: While on a threshold, make a '
                        'conditional declaration and spend a Glamour. Roll Resolve + Intimidation + '
                        'Wyrd contested by Composure + Wyrd. Does not physically prevent crossing, '
                        'but those who fail and cross without meeting conditions suffer the Lost '
                        'Condition.',
            'book': 'Kith 105'},
 'reborn': {'name': 'Reborn',
           'skill': 'Occult',
           'description': 'Reborn were broken down and rebuilt by their Keepers, sometimes again '
                          'and again. Each reconstruction burned out everything unnecessary and '
                          'weak. Only those who seized and held fast to their core identity '
                          'survived with humanity intact. After escape they no longer return from '
                          'death, but they carry adaptive power in their blood.',
           'blessing': 'When using Occult to separate fact from fake, three successes count as an '
                       'exceptional success. Retune: After taking lethal damage, spend a Glamour '
                       'and roll Intelligence + Occult to redistribute Skill dots equal to '
                       'successes from one Skill to another for the scene (cannot exceed Wyrd '
                       'maximum). Once per chapter, spend a Willpower dot to make the '
                       'redistribution permanent.',
           'book': 'Kith 105'},
 'stoneflesh': {'name': 'Stoneflesh',
               'skill': 'Intimidation',
               'description': 'A common kith forged for durability: stone-skinned trolls, bronze '
                              'hounds, armored knights on a bloody chessboard. The Gentry take '
                              'stubborn humans and toughen them up, dangling a sliver of hope just '
                              'out of reach. Back in the mortal world, they often become community '
                              'pillars -- they survived Arcadian horrors, so whatever mortal life '
                              'throws at them, they can weather it.',
               'blessing': 'When using physical presence for Intimidation, three successes count as '
                           'an exceptional success. Obdurate Skin: Spend a Glamour and roll Stamina '
                           '+ Athletics + Wyrd. Divide successes between Armor, Resolve, and '
                           'Composure for the scene.',
               'book': 'Kith 106'},
 'wisewitch': {'name': 'Wisewitch',
              'skill': 'Persuasion',
              'description': "Wisewitches were marked by contact with a Keeper's Title, pressed "
                             'into them like a seal into wax. Some were shaped deliberately; others '
                             'touched the Title on their own without their Keeper realizing it. '
                             'Other changelings have difficulty identifying them visually, but '
                             'their appearance always carries some mark of their brush with the '
                             'Title. Today they commonly practice as psychics, herbalists, shamans, '
                             'or priests.',
              'blessing': 'When using Persuasion to warn someone away from supernatural danger, '
                          'three successes count as an exceptional success. Keen Bargains: The '
                          'Wisewitch can form pledges with spirits and angels not of fae kind.',
              'book': 'Kith 106'},
 'airtouched': {'name': 'Airtouched',
               'skill': 'Athletics',
               'description': 'Some Airtouched were already one step removed from others before '
                              'abduction. Others were deeply rooted people whose connections the '
                              'Gentry severed one by one. Either way, their Keepers drained their '
                              'attachments and crafted them into clouds or distant, circling birds. '
                              'The ache for connection remains. Those who escape prove the Fae '
                              'cannot consistently sever humanity from its need for others.',
               'blessing': 'When rolling Athletics to climb, jump, or move vertically, three '
                           'successes count as an exceptional success. The Drift: Spend a Glamour '
                           'to move as though weighing only a few ounces -- cross snow without '
                           'breaking through, walk on water, or balance on surfaces too fragile for '
                           'full weight. Penalize tracking attempts by Wyrd/2 (minimum 1).',
               'book': 'Kith 107'},
 'chalomot': {'name': 'Chalomot',
             'skill': 'Empathy',
             'description': 'Chalomot served as dream-road scouts, finding cracks in Bastions and '
                            "crafting lures within sleepers' minds. Their Keepers slowly stripped "
                            'away their sense of reality through repetitive dreams with subtle '
                            'tweaks until only oneiric logic made sense. Kept captive by a chain of '
                            'ivory and horn anchored to the bones of her wrist, each invaded '
                            'Bastion after Bastion until she tore the chain free.',
             'blessing': 'When gauging the strength of a Bastion, three successes on Empathy count '
                         'as an exceptional success. Dreamtread: Spend a Glamour to gain a bonus to '
                         'dreamweaving rolls equal to Wyrd/2 (minimum 1) for the rest of the scene. '
                         'May spend additional Glamour to share this blessing with up to five '
                         'fellow oneiromancers in the same Bastion.',
             'book': 'Kith 107'},
 'chevalier': {'name': 'Chevalier',
              'skill': 'Persuasion/Intimidation',
              'description': 'Chevaliers are shaped by the deep bond between rider and steed, '
                             'whether horse, motorcycle, or racing car. One Keeper lures young '
                             'riders with kelpies; another places ads for antique auto restorers. '
                             'The bond runs deep enough that breaking free often means losing an '
                             'irreplaceable mount in the Thorns.',
              'blessing': 'Choose Persuasion or Intimidation. When riding or piloting their steed '
                          'and rolling the chosen Skill, three successes count as an exceptional '
                          "success. Rider's Call: Spend a Glamour to touch a vehicle or mount and "
                          'name it Noble Steed. Spend another Glamour reflexively to call it from '
                          'anywhere at its fastest speed. Sapient steeds may refuse. Contested '
                          'claims prompt a Clash of Wills. The steed automatically senses the '
                          "rider's peril when she drops to 0 Willpower, gains a Clarity Condition, "
                          'or takes wound penalties.',
              'book': 'Kith 107'},
 'farwalker': {'name': 'Farwalker',
              'skill': 'Survival',
              'description': "Farwalkers patrolled the borders of their Keeper's realm until one "
                             'day they found a crack in the horizon wide enough to fit through. The '
                             'Gentry select those used to long solitary routes: hikers, night '
                             'security guards, latchkey kids, long-haul commuters. They can make '
                             'shelter anywhere and lead motleys on ranging treks through the Hedge.',
              'blessing': 'When using Survival to find or create shelter or forage in any realm, '
                          'three successes count as an exceptional success. Home Away from Home: '
                          'Spend a Glamour in wild terrain to create a one-dot Safe Place for a '
                          'day, sleeping Wyrd/2 people (minimum 1). Expand with extra Glamour per '
                          'person. In the Hedge, instead decrease the Hedge rating by one for the '
                          'same area and confer one feature of an existing Hollow.',
              'book': 'Kith 108'},
 'flickerflash': {'name': 'Flickerflash',
                 'skill': 'Athletics',
                 'description': 'Every Flickerflash carried deep restlessness long before the Fae '
                                'found them -- the runaway child, the Navy recruit escaping a dusty '
                                'hometown, the college student burning from one project to the '
                                'next. The Gentry twisted that longing into an unquenchable need '
                                'for speed. Many get caught in obsessive loops, proving themselves '
                                'again and again to their motleys and freeholds.',
                 'blessing': 'When using Athletics during a chase in any realm, three successes '
                             'count as an exceptional success. Instantaneous Velocity: Reflexively '
                             'spend a Glamour to triple Speed. Apply before any other Speed '
                             'modifiers.',
                 'book': 'Kith 110'},
 'levinquick': {'name': 'Levinquick',
               'skill': 'Computer',
               'description': 'Levinquick are electricity given purpose: scouts and couriers '
                              'flowing through grids and networks. Constantly looking to the '
                              'horizon, they know sitting still makes them vulnerable. The digital '
                              "world's restless children -- anyone raised with modern technology -- "
                              'make good Levinquick. The best carry an ineffable hunger for motion '
                              'that is never satisfied.',
               'blessing': 'When engaging in chase rolls within the BriarNet, three successes on '
                           'Computer count as an exceptional success. Lightning Walk: Touch a '
                           'land-connected telecom device, spend 3 Glamour, and roll Wits + '
                           'Athletics + Wyrd. On success, dissolve into the grid and reappear at '
                           'another known land-connected device within Wyrd miles. Can carry '
                           'companions for extra Glamour each; dragging unwilling people triggers a '
                           'Clash of Wills and potential moral consequences.',
               'book': 'Kith 110'},
 'swarmflight': {'name': 'Swarmflight',
                'skill': 'Stealth',
                'description': 'Swarmflights can disassemble into coherent swarms -- spiders, '
                               'fireflies, mice, bubbles -- and reform when danger passes. They '
                               'often respond to stress by literally falling apart. The swarm acts '
                               'as a single entity, perceiving through any individual creature.',
                'blessing': 'When using Stealth in swarm form, three successes count as an '
                            'exceptional success. Swarm Form: Spend a Glamour to dissolve into a '
                            'chosen swarm type (fixed at creation, Size 0 or 1 creatures). Spread '
                            'up to five yards per Wyrd dot. Everyone in the area suffers persistent '
                            'Distracted. Most single attacks deal only one point of damage (two on '
                            'exceptional), except iron and large-scale threats. Appropriate swarm '
                            'types may attack with Strength + Brawl ignoring Defense, dealing '
                            'lethal damage divided among those in the swarm.',
                'book': 'Kith 110'},
 'swimmerskin': {'name': 'Swimmerskin',
                'skill': 'Brawl',
                'description': 'Swimmerskins draw from global aquatic myth -- kuliltu, rusalka, '
                               'ningyo, kelpie, merrow. Those who love the water always face peril '
                               'for their adoration; some are lured into riptides, others dragged '
                               'through cracked ice. Sometimes an unfortunate who hates water gets '
                               'swept off a whale-watching deck. When Gentry caprice and the sea '
                               'combine, anything can happen.',
                'blessing': 'When rolling Brawl to grapple or ambush someone in or from water, '
                            "three successes count as an exceptional success. The Selkie's Skin: "
                            'Always breathe both air and water. Spend a Glamour to reflexively fuse '
                            'legs into a tail, tentacles, or aquatic appendages. Swim at double '
                            'Speed and suffer no penalties for weapons or complex tasks underwater. '
                            'May be invoked and dismissed reflexively.',
                'book': 'Kith 111'},
 'bearskin': {'name': 'Bearskin',
             'skill': 'Intimidation/Weaponry',
             'description': 'Bearskin soldiers were pushed into endless Arcadian wars, broken down '
                            'until they wanted to fight and die for their Keeper. The causes were '
                            "pointless -- a single flower, a golden apple. Many don't realize they "
                            'can escape until their Keeper rejects them or pushes them past a line. '
                            'A Bearskin with a cause fashions their whole self into its sword; a '
                            'liege need not prove herself worthy -- she just needs to ask.',
             'blessing': 'Choose Intimidation or Weaponry. When using the chosen Skill to defend a '
                         "motley-mate's Aspiration (not her own), three successes count as an "
                         'exceptional success. Dulce et Decorum Est: When an opponent surrenders or '
                         'the Bearskin successfully intimidates or coerces someone, spend a Glamour '
                         "to replace one of the defeated opponent's Aspirations with one of her own "
                         'for the rest of the story.',
             'book': 'Kith 111'},
 'beastcaller': {'name': 'Beastcaller',
                'skill': 'Animal Ken',
                'description': 'Beastcallers corralled goblin war-beasts for the Gentry -- '
                               'briarwolves, birds of omen, and stranger things. Before abduction, '
                               'they may have been zookeepers, lion tamers, or dog fighters. The '
                               'hardest part of escape was leaving a bonded beast behind. Working '
                               'with animals soothes trauma, but the closer the bond, the harder it '
                               'is to tell one mind from another.',
                'blessing': 'When making an Animal Ken roll to tame a goblin beast, three successes '
                            'count as an exceptional success. Night Rider: Spend a Glamour and roll '
                            'Presence + Animal Ken + Wyrd to possess a goblin beast for turns equal '
                            'to Wyrd. The Beastcaller takes bashing for each lethal dealt to the '
                            'beast, and lethal for each aggravated. If the beast dies while '
                            'possessed, the changeling returns to her own body with an additional '
                            'aggravated wound.',
                'book': 'Kith 112'},
 'cyclopean': {'name': 'Cyclopean',
              'skill': 'Investigation',
              'description': 'Cyclopeans are towering nightmare giants: caryatids holding living '
                             'temples, shepherds of golden-fleeced sheep, armies of oni. Almost '
                             'every Cyclopean carries some lasting injury from service -- a missing '
                             'arm, a lost leg. Their muchness, once a problem, became the solution. '
                             'In freeholds they usually serve as combatants or protectors, though '
                             'some choose the softer roles of shepherd, builder, or tracker.',
              'blessing': 'When using Investigation to track down any fae creature other than a '
                          'Huntsman, three successes count as an exceptional success. Smell The '
                          "Blood: Once per scene, spend a Glamour to learn the target's weakest "
                          'points, reducing penalties for attacks to specified targets by 2 '
                          '(minimum -1). If the attack would deal bashing, it deals lethal instead.',
              'book': 'Kith 112'},
 'plaguesmith': {'name': 'Plaguesmith',
                'skill': 'Medicine',
                'description': 'Plaguesmiths were living biological weapons the Gentry sent into '
                               'war. Not all knew what the Fae did to them until they watched '
                               'symptoms appear on test subjects. They return acutely aware of '
                               'their poisoned touch and become extraordinarily choosy about '
                               'interaction. Many become hypochondriacs, fearing the diseases '
                               'incubated in their bodies could turn on them or their loved ones.',
                'blessing': 'When using Medicine to treat infectious disease, three successes count '
                            'as an exceptional success. Plague of Arcadia: Touch a target, spend a '
                            'Glamour, and roll Strength + Medicine + Wyrd contested by Stamina + '
                            'Wyrd. The target suffers a grave disease dealing one aggravated per 12 '
                            'hours. Stopping it requires successful resistance rolls equal to the '
                            "Plaguesmith's Wyrd. Symptoms should reflect the Keeper's Title and may "
                            'be fantastical.',
                'book': 'Kith 113'},
 'razorhand': {'name': 'Razorhand',
              'skill': 'Brawl',
              'description': 'Razorhands had blades installed where fingers once were. The Fae '
                             'often chose the gentlest of souls, delighting in watching them grow '
                             'calluses over their hearts. A Razorhand never escapes the bloodshed '
                             'built into his body -- some embrace it, some struggle against it, but '
                             'the hands remain.',
              'blessing': 'When attacking with bladed hands, three successes count as an '
                          'exceptional success. Sakin: Spend a Glamour to transform one hand into a '
                          '1L knife for the scene; a second Glamour allows the other hand as well '
                          '(with offhand penalties). Uses Brawl and unarmed styles. Unless someone '
                          'removes her limbs, a Razorhand may never be disarmed.',
              'book': 'Kith 114'},
 'sandharrowed': {'name': 'Sandharrowed',
                 'skill': 'Survival',
                 'description': "Sandharrowed were set loose in Arcadia's vast deserts as nomads or "
                                'dust devils. Before abduction, they were quietly useful people -- '
                                'the administrator who sends all the mail, the head of the '
                                'street-sweeping crew, the substitute teacher who always shows up '
                                'on time. They learned to survive windstorms without a scratch and '
                                'carry that sand with them as a weapon.',
                 'blessing': 'When using Survival to get through an area affected by an '
                             'environmental Tilt, three successes count as an exceptional success. '
                             'Enveloping Sands: Once per scene, before a Brawl or Weaponry attack, '
                             'spend a Glamour. On success, the target suffers the Immobilized Tilt '
                             'as a sand pillar traps them. The pillar has Durability 2 and the '
                             'target has cover while trapped.',
                 'book': 'Kith 115'},
 'valkyrie': {'name': 'Valkyrie',
             'skill': 'Persuasion/Intimidation',
             'description': 'Valkyries walk battlefields selecting who rises and who falls. The '
                            'Gentry favor mortals with deep convictions about right and wrong, then '
                            'delight in forcing them to choose between their survival and someone '
                            "else's until they lose all sense of themselves. They accumulate "
                            'symbols of whatever mythos their Keeper adhered to, though many Fae '
                            'just made up their own tortured symbology.',
             'blessing': 'Choose Persuasion or Intimidation. When inspiring an ally or intimidating '
                         'a foe on the battlefield with the chosen Skill, three successes count as '
                         'an exceptional success. Chooser of the Slain: A number of times per scene '
                         'equal to Wyrd/2 (minimum 1), spend a Glamour and roll Wits + Occult + '
                         'Wyrd contested by Resolve + Wyrd to grant an ally Inspired or Steadfast, '
                         'or inflict Frightened or Reckless on a foe.',
             'book': 'Kith 115'},
 'venombite': {'name': 'Venombite',
              'skill': 'Brawl',
              'description': 'Not poisonous but venomous, Venombites take their name from their '
                             'dangerous bites. Everyone carries small resentments, words they never '
                             "say, petty hatreds boiling in their stomachs. A Venombite's durance "
                             'distilled those feelings into Arcadian toxin. They were kept as pets, '
                             'poison sources, or assassins. That path of destruction often '
                             'continues in the mortal world.',
              'blessing': 'When using Brawl to grapple, three successes count as an exceptional '
                          'success. Deadly Bite: Once per scene, spend a Glamour before rolling a '
                          'Brawl attack. If it succeeds, inject the victim with toxin in addition '
                          'to normal damage. The attack deals lethal and inflicts the Poisoned Tilt '
                          '(grave poison).',
              'book': 'Kith 116'},
 'apoptosome': {'name': 'Apoptosome',
               'skill': 'Miscellaneous',
               'description': 'Apoptosomes died and reformed in empty fortresses, over and over, '
                              'waging solitary war against trespassers. Each death left them '
                              'misshapen by the blow that killed them, but wiser to the tricks of '
                              'the next attacker. They never saw their Keeper directly. They often '
                              'return with questionable boundaries, treating disagreements as '
                              'preludes to new attacks.',
               'blessing': 'Perfectly remembers fight progressions she loses -- gains an extra die '
                           'on one roll per scene in subsequent contests with that creature or '
                           'person. Sparagmos: In a fight with someone who has hurt her before, '
                           'spend a Glamour to deal one aggravated to that foe. For the rest of the '
                           'scene, both the changeling and those enemies take an additional '
                           'aggravated point every time they damage the Apoptosome.',
               'book': 'Kith 116'},
 'becquerel': {'name': 'Becquerel',
              'skill': 'Stealth',
              'description': 'A relatively new kith, born from nuclear-era nightmares. The Gentry '
                             'noticed when nuclear energy rocketed down the trods near Trinity and '
                             'Lop Nur. Becquerels were used as art pieces, poisoners, and '
                             'assassins, their shadowy forms lending stealth in low light. Many '
                             'escape in spectacular bursts through the Hedge. Their touch is warm '
                             'and their passions run hot.',
              'blessing': 'When using Stealth in low-light areas, three successes count as an '
                          'exceptional success. Nuclear Shadow: When she successfully grapples '
                          'someone, spend a Glamour to burn them as though set on fire (torch size, '
                          'candle heat). Appears as radiation burns to mundane scans. Each turn she '
                          'maintains the grapple, she may inflict Stunned or Poisoned.',
              'book': 'Kith 117'},
 'blightbent': {'name': 'Blightbent',
               'skill': 'Disease/Poison',
               'description': 'Blightbent toiled in the foulest conditions Arcadia could offer -- '
                              'ammonia cauldrons, furnace towers, sour bogs, volcanic calderas. '
                              'They became poison to survive the poison. Most did not choose to '
                              'escape; they woke up dumped in the Hedge when they had absorbed too '
                              'much. The smell of tar feels more natural to them than wildflowers.',
               'blessing': 'When making Stamina + Resolve to mitigate disease and poison damage, '
                           'automatically downgrade aggravated to lethal, lethal to bashing, or '
                           'ignore bashing. Brimstone: When she successfully grapples someone, '
                           'spend a Glamour to inflict the Poisoned Tilt through her caustic touch.',
               'book': 'Kith 117'},
 'enkrateia': {'name': 'Enkrateia',
              'skill': 'Empathy/Persuasion/Subterfuge',
              'description': 'Enkrateia were created as better angels -- silver statues brokering '
                             'peace, fang-toothed giants pronouncing judgment, caged songbirds '
                             'chirping subtle advice. Their Keepers listened only when they felt '
                             'like it. In freeholds, they excel when heightened emotions override '
                             "everyone else's better natures.",
              'blessing': 'When attempting to calm a conflict, roll the highest of Empathy, '
                          'Persuasion, or Subterfuge. Eloquent Analysis: When the Enkrateia takes '
                          'an extended action to Investigate, she only begins to lose dice after '
                          'the third successive roll.',
              'book': 'Kith 118'},
 'gravewight': {'name': 'Gravewight',
               'skill': 'Empathy/Intimidation',
               'description': 'Gravewights performed death-work in Arcadia: executions, funerary '
                              'rites, dredging battlefields. Not necessarily morbid -- they can '
                              'become cavalier about death, including their own. Their presence '
                              'attracts ghosts and beings caught between life and death. A clever '
                              'monarch knows how to use a loyal Gravewight.',
               'blessing': 'Choose Empathy or Intimidation. When influencing someone with her mien, '
                           'physical presence, or knowledge of death mechanics, three successes '
                           'count as an exceptional success. Charnel Sight: Spend a Glamour to see '
                           'and hear ghosts in Twilight. Ghosts appear more frequently and '
                           'completely near her.',
               'book': 'Kith 119'},
 'shadowsoul': {'name': 'Shadowsoul',
               'skill': 'Subterfuge',
               'description': 'Shadowsouls were crafted for nocturnal or chthonic Keepers into '
                              'evening stars, dark doppelgangers, or crystal cave-dwellers. They '
                              'took long, dangerous roads out of Arcadia, unable to move faster '
                              "than the moon's pace. They carry frailties tied to daylight and "
                              'embrace the darkness not out of preference but necessity.',
               'blessing': 'Gain a Subterfuge bonus equal to Wyrd and the 8-again rule on '
                           'Subterfuge rolls. Nightblind: Gain natural affinity with the Mirror '
                           'Regalia in addition to other affinities. Once per scene, on an '
                           'exceptional attack success, inflict temporary Blindness on someone she '
                           'touches. Resolves at end of scene.',
               'book': 'Kith 119'},
 'telluric': {'name': 'Telluric',
             'skill': 'Drive/Streetwise',
             'description': "Tellurics were set as stars in Arcadia's heavens -- burning with fire, "
                            'shining with radiance, visible to everyone but spoken to by no one. '
                            'They were all lonely in some way before abduction. The Gentry lured '
                            'them with promises of beauty and attention. Escaped Tellurics tell sad '
                            'stories about friends consumed by their own perfection who fell to the '
                            'forests as shooting stars.',
             'blessing': 'When chasing someone with Drive or Streetwise on a clear night under '
                         'visible stars, three successes count as an exceptional success. Burn '
                         'Bright: Spend a Glamour to throw a ball of starflame as a ranged attack '
                         'using Dexterity + Athletics. The fire is torch-sized with candle heat.',
             'book': 'Kith 120'},
 'whisperwisp': {'name': 'Whisperwisp',
                'skill': 'Subterfuge',
                'description': 'Whisperwisps were built to be spies and saboteurs, constantly '
                               'cataloging the habits of others, punctuated by grueling '
                               'interrogations and mock trials. Most are cold and a little amoral, '
                               'lying reflexively even when sharing would be better. Nearly all '
                               'stay apart, ready to fade into shadows at the first sign of '
                               'personal danger.',
                'blessing': 'When influencing someone with a known falsehood, three successes count '
                            'as an exceptional success. When influencing with truth, five successes '
                            'count as exceptional. Forked Tongue: Choose Stealth or Persuasion at '
                            'character creation. Rolls with the chosen skill gain both 9-again and '
                            'a bonus equal to Wyrd.',
                'book': 'Kith 120'},
 'antiquarian': {'name': 'Antiquarian',
                'skill': 'Empathy',
                'description': "Antiquarians were built to guard a Keeper's one true vulnerability "
                               'by burying it under names, memories, and confessions stolen from '
                               'countless others. They survive by hoarding truth, speaking rarely, '
                               'and reading what people do not mean to reveal. What they know can '
                               'rescue a freehold or ignite a war, depending on when they speak.',
                'blessing': 'Secrets and Whispers: when using Empathy to uncover hidden truths, '
                            'three successes count as exceptional success. Once per session, spend '
                            '1 Glamour and roll Intelligence + Composure to ask a question and draw '
                            'an answer through research, intuition, omen, or dream-whisper; '
                            'required successes scale with how hidden the truth is. Secrets and '
                            'Whispers scales from ordinary research to occult revelation, depending '
                            'on success and narrative access.',
                'book': 'DE2 69'},
 'chimera': {'name': 'Chimera',
            'skill': 'Subterfuge',
            'description': 'Chimera are patchwork composites stitched from multiple bestial forms '
                           '-- predator, courier, executioner in one body. They retain kinship with '
                           'goblins and hedge creatures and understand deception from the inside '
                           'out. Common where Gentry experiment openly with form, especially in '
                           'realms that prize spectacle and utility.',
            'blessing': 'Goblin Kin: when using Subterfuge to detect spoken or written trickery, '
                        'three successes count as exceptional success. Each chapter, choose one '
                        'Goblin Contract the character know; that Contract does not incur Goblin '
                        'Debt when invoked, and this benefit rotates until all eligible Goblin '
                        'Contracts have been selected. Goblin Kin supports rotational versatility '
                        "and encourages regular use of the kith's broader Goblin Contract toolkit.",
            'book': 'CTL JS 47 / DE2 69'},
 'dryad': {'name': 'Dryad',
          'skill': 'Survival',
          'description': 'Dryads were cultivated as living ornaments and wardens in Arcadian '
                         'gardens and sacred groves. They often prefer trees to crowds, navigating '
                         'forest and Hedge instinctively. Even in cities, many seek parks and '
                         'overgrown margins for safety. They tend to trust trees and thorns faster '
                         'than people.',
          'blessing': 'Fade into the Foliage: in wooded areas (including the Hedge), Survival rolls '
                      'for tracking and pathfinding treat three successes as exceptional success. '
                      'If unobserved for one turn, spend 1 Glamour to conceal themself behind '
                      'substantial foliage; remain perfectly hidden while still, and add Wyrd to '
                      'Stealth when moving. Fade into the Foliage turns terrain into defense, '
                      'rewarding patience, sight-line control, and woodland positioning.',
          'book': 'DE2 70'},
 'muse': {'name': 'Muse',
         'skill': 'Mantle',
         'description': 'Muses inspire, pressure, and provoke excellence in others, prized by '
                        'Keepers who measured power through monuments and performance. Socially '
                        'magnetic and politically useful, they can elevate status by presence '
                        'alone. Their influence can be genuine inspiration or coercive pressure '
                        'dressed as encouragement.',
         'blessing': 'Tyranny of Ideas: once per session, interact with other Lost as though the '
                     "character's Mantle or court Goodwill were one dot higher. By spending 1 "
                     'Glamour and making an appropriate social roll against a human target, the '
                     "character grant bonus dice to that target's creation roll and let three "
                     'successes count as exceptional success for the resulting work. Tyranny of '
                     'Ideas creates indirect power by amplifying mortal creators rather than '
                     'harvesting glamour from their output.',
         'book': 'DE2 70'},
 'nymph': {'name': 'Nymph',
          'skill': 'Athletics',
          'description': 'Nymphs are waterborn changelings thriving in harbors, riverways, and '
                         'hidden channels where information and tribute move together. Natural '
                         'aquatic scouts and social powers in port communities, balancing '
                         'hospitality and danger with the same current that carried them out of '
                         'Arcadia.',
          'blessing': 'Gift of Water: when making Athletics rolls while swimming, three successes '
                      'count as exceptional success. Spend 1 Glamour and succeed on a Stamina + '
                      'Athletics roll to manifest gills and an aquatic lower form, allowing '
                      'air-and-water breathing, double swim speed, and normal use of weapons and '
                      'complex actions underwater for the scene. Gift of Water provides sustained '
                      'aquatic superiority, making ports, rivers, and flooded zones decisive home '
                      'ground.',
          'book': 'DE2 70'},
 'cleverquick': {'name': 'Cleverquick',
                'skill': 'Occult',
                'description': 'Quick-witted hunters and schemers who often worked in pairs to '
                               "expose an enemy's hidden weaknesses. They thrive on preparation, "
                               'pattern recognition, and dangerous bargains. Victory, for a '
                               'Cleverquick, is proof of preparation rather than brute force.',
                'blessing': "Know the character's Enemy: when using Occult to outsmart an "
                            'adversary, three successes count as exceptional success. Spend 1 '
                            'Glamour to learn one existing frailty, ban, or bane; spend 3 Glamour '
                            'to impose a temporary one for the chapter, but the character accept '
                            'the same weakness for that duration. Paired Cleverquicks may split '
                            'costs and share outcomes.',
                'book': 'DE2 368'}}


def get_kith(kith_key):
    """Get a specific kith by key."""
    return ALL_KITHS.get(kith_key.lower().replace(" ", "_"))


def get_all_kiths():
    """Get all kiths."""
    return ALL_KITHS.copy()
