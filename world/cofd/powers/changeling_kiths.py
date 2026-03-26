"""
Changeling Kith Data for Chronicles of Darkness 2nd Edition.

Kith data including skills, descriptions, blessings, and sources.
Based on Changeling: The Lost 2nd Edition core book, Kith & Kin, and Dark Eras 2.
"""

ALL_KITHS = {'artist': {'name': 'Artist',
            'skill': 'Crafts',
            'description': 'Creators whose bodies and habits were fused to their chosen medium by Arcadian compulsion, '
                           'whether paint, stone, architecture, music, or another art that consumed their every waking '
                           'hour. Artists were punished for pausing, resting, or presenting anything less than '
                           'perfection, and many escaped only by channeling that same obsessive creative force against '
                           'their Keepers. Many keep unfinished work hidden until it feels flawless enough to survive '
                           'another judgment. Their mien often carries marks of medium and method: stone skin, '
                           'ink-veins, pigment streaks, or tool-callused hands. Freeholds rely on them for inspired '
                           'creation but learn quickly not to interrupt their process at the wrong moment.',
            'blessing': 'Tools of the Trade: choose Crafts or Expression and an art Specialty. When using that '
                        'Specialty, three successes count as an exceptional success; by spending 1 Glamour, your tools '
                        'and materials manifest for a scene and grant bonus dice equal to Wyrd (maximum +5) on '
                        "relevant creation rolls. This blessing models the Artist's compulsive preparedness: tools "
                        'appear when inspiration hits, and technical focus spikes under pressure.',
            'book': 'CTL 2e 51'},
 'bright_one': {'name': 'Bright One',
                'skill': 'Socialize',
                'description': 'Radiant changelings forged from mortal passion driven to unbearable intensity, then '
                               'punished in Arcadia whenever that emotion surfaced. Bright Ones often escaped in '
                               'eruptions of light and fury, and even in mortal life they remain difficult to ignore - '
                               'luminous presences whose warmth, anger, and conviction can dominate a room. Keepers '
                               'often lured them through passion rather than force, then punished feeling until rage '
                               'became radiance. Their escape stories frequently involve blinding brilliance at '
                               'exactly the right second. In modern freeholds, they are both magnetic social anchors '
                               'and dangerous emotional accelerants.',
                'blessing': 'Flare: when using Socialize to become the center of attention, three successes count as '
                            'exceptional. By spending 1 Glamour, you intensify your glow to blinding brilliance for a '
                            'turn; visible enemies who can see you take bashing damage and suffer a -2 penalty on '
                            'Physical and Mental actions. Used well, it turns social spotlight into battlefield '
                            'control, punishing enemies who underestimate presence as a weapon.',
                'book': 'CTL 2e 52'},
 'chatelaine': {'name': 'Chatelaine',
                'skill': 'Empathy',
                'description': 'Perfect household servants drilled in protocol, hierarchy, and anticipatory obedience '
                               'within hostile fae estates where every misstep invited punishment. Chatelaines '
                               'survived by mastering social systems and reading immediate need, and they carry that '
                               'talent into freehold politics as planners, stewards, event-runners, and subtle '
                               'operators. They learned to survive by reading rooms before anyone spoke and by '
                               'borrowing structure from people with more apparent power. Many become exceptional '
                               'event stewards, negotiators, and court logisticians. Even after escape, service, '
                               'control, and self-worth remain tangled themes in their lives.',
                'blessing': "Will That Be All?: when using Empathy to read a target's immediate desires, three "
                            'successes count as exceptional. Spend 1 Glamour and roll Manipulation + Socialize to '
                            "temporarily use one other character's Social Merits as if your own for the scene, with "
                            'events remembered as though that target used them. It captures how a Chatelaine survives '
                            'through systems, protocol, and borrowed status rather than raw authority.',
                'book': 'CTL 2e 52'},
 'gristlegrinder': {'name': 'Gristlegrinder',
                    'skill': 'Brawl',
                    'description': 'Cannibal nightmares shaped by emptiness, deprivation, and Arcadian brutality, '
                                   'taught to cook, butcher, or devour other captives as warning and utility. '
                                   'Gristlegrinders return carrying bottomless appetites - not only for flesh, but for '
                                   'love, status, money, safety, and certainty - and many struggle to prove they are '
                                   'more than the hunger they survived. Their hunger is rarely only literal: it often '
                                   'manifests as obsession with security, affection, money, or certainty. Rumors about '
                                   'what they will or will not eat follow them through every court. The kindest among '
                                   'them work hard to prove they are more than the role Arcadia carved into their '
                                   'jaws.',
                    'blessing': 'To Serve Man: when grappling to feed, three Brawl successes count as exceptional. You '
                                'can make lethal bite attacks without grappling first, and by spending 1 Glamour and '
                                'rolling Stamina + Survival you may swallow smaller targets whole; those inside take '
                                'ongoing lethal damage and must inflict major internal harm to escape. The blessing '
                                'makes hunger tactically concrete, combining close-quarters lethality with terrifying '
                                'control once a target is seized.',
                    'book': 'CTL 2e 53'},
 'helldiver': {'name': 'Helldiver',
               'skill': 'Larceny',
               'description': 'Arcadian spies and infiltrators sent where even True Fae preferred not to go, often '
                              'bound by a painful silver tether to their Keeper until they found a way to sever it. '
                              'Helldivers are compulsive explorers and information thieves, forever drawn toward '
                              'secret places, occult crossings, and conversations they absolutely should not hear. The '
                              'silver thread of service is remembered as both leash and map, and severing it marks '
                              'true freedom. They remain compulsive explorers of odd realms, forbidden doors, and '
                              'half-known rumors. Knowledge is their comfort, their weapon, and sometimes their most '
                              'dangerous appetite.',
               'blessing': 'Dive: when using Larceny in the Hedge, Arcadia, or other unearthly realms, three successes '
                           'count as exceptional. Spend 1 Glamour and roll Dexterity + Occult to phase over time into '
                           'an invisible, incorporeal state like a dematerialized Hedge ghost; spend Glamour and roll '
                           'again to return, with access to inter-realm transit where valid gates exist. Dive rewards '
                           'planning around timing, Clarity, and exits, especially when crossing boundaries other '
                           'kiths cannot safely traverse.',
               'book': 'CTL 2e 53'},
 'hunterheart': {'name': 'Hunterheart',
                 'skill': 'Investigation',
                 'description': 'Predators of Arcadia shaped by relentless chase, blooded struggle, and mythic beast '
                                'archetypes rather than natural ecology. Hunterhearts may be noble stalkers, '
                                'terrifying ambushers, or disciplined trackers, but all retain the primal certainty '
                                'that survival belongs to whoever finds the trail first and closes fastest. Their '
                                'behavior follows mythic predator stories as much as biology: proud lions, solitary '
                                'wolves, or elegant stalking cats. Escape often comes through bloodshed, but just as '
                                'often through perfect patience. What matters is the chase, the strike, and never '
                                'surrendering the trail.',
                 'blessing': 'Pounce: choose Investigation or Survival; when using the chosen Skill to track fae '
                             'beings, three successes count as exceptional. If a target can meet your gaze, spend 1 '
                             'Glamour and contest Presence + Wyrd against Composure + Tolerance to inflict either '
                             'Insensate or Frightened, and your unarmed attacks against that prey become lethal. '
                             'Pounce blends predatory fear and finishing force, making first contact and eye-line '
                             'positioning crucial to success.',
                 'book': 'CTL 2e 54'},
 'leechfinger': {'name': 'Leechfinger',
                 'skill': 'Medicine',
                 'description': 'Predatory life-drainers shaped from takers of every social class - manipulators, '
                                'professionals, killers, and caretakers alike - then weaponized as contact-based '
                                'torture tools in Faerie. Leechfingers return with excellent bedside instincts and '
                                'terrifying intimacy-based power, making them useful healers and deeply mistrusted '
                                'companions. The kith carries the social unease of a healer who can also feed on '
                                'contact. Some choose strict personal boundaries; others rationalize predation as '
                                "necessity. Even allies may wonder how much help and harm can look identical at arm's "
                                'length.',
                 'blessing': "Sap the Vital Spark: when using Medicine to assess a target's health, three successes "
                             'count as exceptional. By maintaining physical contact for a full turn and spending 1 '
                             'Glamour, you deal bashing damage and heal yourself by downgrading damage; against '
                             'changelings, both inflicted and healed amounts double. Sap mechanics reinforce the '
                             "kith's duality: predation and restoration share the same touch and the same moral risk.",
                 'book': 'CTL 2e 55'},
 'mirrorskin': {'name': 'Mirrorskin',
                'skill': 'Stealth',
                'description': 'Identity-fluid survivors who escaped by becoming impossible to pin down, whether as '
                               'spies, prototype bodies, captive reflections, or living displays for capricious '
                               'Keepers. Mirrorskins are masters of adaptive selfhood; they can be anyone long enough '
                               'to survive, but often pay for that flexibility with uncertainty about who remains '
                               'underneath. People-pleasing instincts and survival disguise blend into a single craft '
                               'for most Mirrorskins. They can pass, infiltrate, and vanish through social systems '
                               'with frightening ease. Their hardest work is often not becoming someone else, but '
                               'deciding who they are when nobody is watching.',
                'blessing': 'Mercurial Visage: when using Stealth while disguised, three successes count as '
                            'exceptional. Spend 1 Glamour and roll Wits + Subterfuge + Wyrd to reshape your Mask into '
                            'a new composite identity; for an additional Glamour you can reshape your mien as well, '
                            'with supernatural detection resolved by Clash of Wills. Mercurial Visage is strongest in '
                            'social infiltration chronicles where identity itself becomes terrain.',
                'book': 'CTL 2e 55'},
 'nightsinger': {'name': 'Nightsinger',
                 'skill': 'Expression',
                 'description': 'Arcadian vocal artists whose songs were cultivated to produce exquisite emotional '
                                'devastation, from grief that breaks stone to joy that dissolves reason. Nightsingers '
                                'often escaped through performances that overwhelmed their captors, and though mortal '
                                'reality dulls their old scope, their voices still carry supernatural enthrallment. '
                                'Many escaped while their Keepers were enthralled by songs too sorrowful or ecstatic '
                                'to resist. Their voices no longer bend reality as easily in the mortal world, but '
                                'still alter rooms and crowds. Admiration, fear, and dependency often follow where '
                                'they perform.',
                 'blessing': 'Siren Song: when singing or composing with Expression, three successes count as '
                             'exceptional. Spend 1 Glamour and roll Presence + Expression + Wyrd contested by '
                             "listeners' Composure + Tolerance; those who fail become Swooned and rooted in place "
                             'while your song continues, unless disrupted by counter-magic, heavy harm, or blocked '
                             'hearing. Siren Song rewards control of line of hearing and scene pacing, often ending '
                             'fights before blows are traded.',
                 'book': 'CTL 2e 56'},
 'notary': {'name': 'Notary',
            'skill': 'Politics',
            'description': 'Living contracts upon whom fae pledges were written in blood, scar, and soul, trained to '
                           'witness every clause and survive every loophole. Notaries are dangerously valuable in '
                           'freehold life: legal memory, oath strategy, and technical interpretation wrapped in one '
                           'person who often escaped by out-lawyering the impossible. Their value lies not just in '
                           'legal knowledge but in exact memory under pressure. Keepers and freeholds alike treat them '
                           'as strategic assets in oath-driven politics. A single clause remembered at the right '
                           'moment can save a motley or doom a monarch.',
            'blessing': 'Abatement: when negotiating, reading, or interpreting fae pledges with Politics, three '
                        'successes count as exceptional. Once per chapter, if you officiate a pledge, you may negate '
                        'its Glamour cost entirely and thereafter recite its exact terms from perfect memory for as '
                        'long as the pledge persists. Abatement can shift entire pledge economies in a chronicle, '
                        'especially where formal bargains drive politics.',
            'book': 'CTL 2e 57'},
 'playmate': {'name': 'Playmate',
              'skill': 'Persuasion',
              'description': 'Beloved companions, comfort objects, and emotional supports crafted to satisfy a '
                             "Keeper's attachment needs, then often discarded once novelty faded. Playmates are "
                             'profoundly social and often painfully self-sacrificing, navigating suspicion from other '
                             'Lost while using their rare healing gift to keep motleys, courts, and communities alive. '
                             'Because many were discarded rather than pursued, they are often mistrusted despite their '
                             'generosity. Their blessing makes them precious in any crisis, but the personal cost can '
                             'be devastating. Motley bonds frequently become the first place they relearn chosen, '
                             'healthy attachment.',
              'blessing': 'Coeur Loyal: when using Persuasion to make someone like you or your allies, three successes '
                          'count as exceptional. By touching a target and spending 1 Glamour, you instantly heal their '
                          'bashing or lethal wounds and take equivalent mild or severe Clarity damage yourself, '
                          'potentially to the point of self-loss. Coeur Loyal offers extreme triage power, but the '
                          'Clarity cost keeps the blessing tragic and narratively sharp.',
              'book': 'CTL 2e 57'},
 'snowskin': {'name': 'Snowskin',
              'skill': 'Subterfuge',
              'description': 'Cold-reserved survivors forged in frigid Arcadian realms where emotional shutdown was '
                             'often the only defense against annihilation. Snowskins escaped by becoming unreadable '
                             'and untouchable to their Keepers, and many still carry that disciplined frost into '
                             'freehold life as strategic calm, social distance, and razor-edged contempt. They '
                             'survived by freezing affect and narrowing trust to what could not betray them. That '
                             'strategy remains effective, but socially isolating, after escape. Behind the cold '
                             'presentation, many hide fierce loyalty to the few they finally allow close.',
              'blessing': 'Heart of Ice: when using Subterfuge to hide your feelings, three successes count as '
                          'exceptional. Spend 1 Glamour and roll Presence + Intimidation + Wyrd contested by Composure '
                          '+ Tolerance to inflict Shaken and impose social penalties among changelings, freezing a '
                          'target out with public disdain. Heart of Ice weaponizes social exclusion, making reputation '
                          'damage as dangerous as physical harm in changeling courts.',
              'book': 'CTL 2e 58'},
 'absinthial': {'name': 'Absinthial',
                'skill': 'Crafts',
                'description': "Fickle, perfectionistic 'green fairies' forced to brew dream-soaked Arcadian absinthe "
                               'for the Gentry, often by distilling their own imagination, longing, and nightmares '
                               'into impossible drink. After escape, many become obsessive brewers, intoxicating '
                               'hosts, and dangerous artists whose charisma can feel like drowning in perfume, memory, '
                               'and hallucination. Absinthials were made to brew dreams into impossible absinthe, and '
                               'many escaped while their Keepers were incapacitated by ecstatic visions. In mortal '
                               'life they often become obsessive brewers, exacting hosts, and volatile aesthetes who '
                               'treat criticism as an existential insult. Storytellers can foreground this kith by '
                               'presenting scenes where its role, trauma, and social reputation all matter at once.',
                'blessing': "Green Fairy's Curse: once per scene, spend 1 Glamour and touch a target, then roll "
                            'Presence + Crafts + Wyrd contested by Composure + Tolerance. On success, your victim is '
                            'overwhelmed by intoxicating visions and rendered Insensate; when the effect ends, they '
                            'stagger back with the Confused Condition as dream and waking reality untangle. Green '
                            "Fairy's Curse combines social contact with incapacitating control, making touch-range "
                            'setup and timing critical.',
                'book': 'Kith 88'},
 'climacteric': {'name': 'Climacteric',
                 'skill': 'Investigation',
                 'description': 'Living calendars and stage-managers of Arcadian realms, once tasked with raising '
                                'suns, calling storms, and setting the rhythm of impossible courts to satisfy a '
                                "Keeper's theatrical whims. Escaped Climacterics excel at pattern-reading and "
                                'battlefield timing, but their old authority over tempo and atmosphere marks them as '
                                'both priceless tactical assets and dangerous beacons for Huntsmen. Climacterics once '
                                'managed weather and time cues for Arcadian pageantry, from candlelit nightfall to '
                                'staged dawns. Freeholds value their strategic timing but often fear the attention '
                                'their powers attract from Huntsmen and old enemies. Storytellers can foreground this '
                                'kith by presenting scenes where its role, trauma, and social reputation all matter at '
                                'once.',
                 'blessing': 'En Prise: whenever anyone rolls Initiative and you are present, you may spend 1 Glamour '
                             'to choose one other character to act at the top of the order without rolling. You cannot '
                             'choose yourself, but you can decisively shape the first beat of a conflict and force the '
                             'scene to begin on your terms. En Prise excels in initiative economies, enabling decisive '
                             'openers without requiring the Climacteric to act first personally.',
                 'book': 'Kith 88'},
 'concubus': {'name': 'Concubus',
              'skill': 'Empathy',
              'description': "Nocturnal companions made to sleep beside alien minds, soothe their Keepers' nightmares, "
                             'and survive long stretches of daylight isolation, abandonment, or confinement. Concubi '
                             'return with rare and frightening oneiromantic intimacy, often serving as therapists, '
                             'courtesans, and dream-guides while carrying the private burden of what they witnessed in '
                             'Gentry dreams that no one else can truly understand. Concubi endured nocturnal intimacy '
                             'with alien minds and long daylight isolation, leaving them uniquely skilled but deeply '
                             'scarred oneiromancers. Many become therapists, courtesans, or dream-guardians for other '
                             'Lost despite suspicion from harder-line courts. Storytellers can foreground this kith by '
                             'presenting scenes where its role, trauma, and social reputation all matter at once.',
              'blessing': 'Valerian and Violence: when you gain Dream Infiltrator by sleeping beside a dreamer and '
                          'working in their Bastion, you can remove one suitable non-persistent mental Condition with '
                          'a successful paradigm shift. Persistent healing is possible through repeated nights, '
                          'repeated access, and sustained oneiromantic intervention, making you one of the strongest '
                          'long-term dream healers in the freehold. Valerian and Violence is long-horizon healing '
                          'through dream access, rewarding sustained consent-based oneiromancy scenes.',
              'book': 'Kith 89'},
 'draconic': {'name': 'Draconic',
              'skill': 'Brawl/Weaponry',
              'description': 'Scaled, horned guardian-beasts forged in the image of Arcadian dragons and made to '
                             'defend towers, treasures, favored captives, or royal vanity projects for centuries at a '
                             'time. Draconics often feel too large and intense for mortal life, but once they trust a '
                             'motley they become fierce, loyal guardians of people, places, and treasured things they '
                             'call home. Draconics were shaped as guardian beasts for hoards, towers, and favored '
                             'captives, and many still organize their lives around territory and protection. They can '
                             'seem overwhelming at first contact, but are fiercely loyal once trust is earned. '
                             'Storytellers can foreground this kith by presenting scenes where its role, trauma, and '
                             'social reputation all matter at once.',
              'blessing': 'None Dare Resist: while your mien is revealed, you may spend extra Glamour to roar, '
                          'posture, or otherwise assert dominance and inflict fear on everyone who can perceive you. '
                          'You can also spend Glamour to take wing and fly briefly at supernatural speed, including '
                          'devastating aerial charges, before gliding safely down when the blessing ends. None Dare '
                          'Resist turns revealed mien into area fear pressure while adding short-burst aerial mobility '
                          'for tactical spikes.',
              'book': 'Kith 90'},
 'flowering': {'name': 'Flowering',
               'skill': 'Socialize',
               'description': 'Shaped by Arcadian gardens, perfumery, and ornamental service, Flowering are '
                              'mesmerizing companions whose tenderness can become emotional dependency before anyone '
                              'realizes what happened. Their scents and social grace make them ideal courtiers, '
                              'confidantes, and power-behind-the-throne manipulators, whether they nurture a '
                              "freehold's health or quietly bend it toward personal obsession. Flowerings were trained "
                              'to beautify others and can struggle with depersonalization after escape. Their scent '
                              'and social pull create dependency quickly, making them either stabilizing confidantes '
                              'or subtle court-poisoners depending on intent. Storytellers can foreground this kith by '
                              'presenting scenes where its role, trauma, and social reputation all matter at once.',
               'blessing': 'Seductive Fragrance: spend 1 Glamour and roll Presence + Empathy to release your signature '
                           'fae perfume for the scene. Others in your presence contest with Composure + Tolerance; '
                           'those who fail gain Leveraged regarding you, and with another Glamour during the same '
                           'scene you may inflict Frightened, Reckless, or Swooned on a Leveraged target. Seductive '
                           'Fragrance creates scene-long leverage webs that can be escalated into targeted emotional '
                           'conditions.',
               'book': 'Kith 90'},
 'ghostheart': {'name': 'Ghostheart',
                'skill': 'Perception',
                'description': "Keepers' undertakers and body-disposers, Ghosthearts handled Arcadia's dead directly "
                               'and learned truths many Lost cannot bear to hear. Haunted but never truly alone, they '
                               'return with uncanny perception, habitual relationships with Twilight beings, and '
                               'reputations as eerie but effective spies, couriers, archivists, and negotiators with '
                               "the restless dead. Ghosthearts handled Arcadia's dead and returned with unusual "
                               'comfort around spirits and memory. Courts that shun them usually regret it, because a '
                               "Ghostheart's Twilight network can harass enemies, gather intelligence, and defend "
                               'territory. Storytellers can foreground this kith by presenting scenes where its role, '
                               'trauma, and social reputation all matter at once.',
                'blessing': 'Friends in Strange Places: begin play with three additional dots of Retainers represented '
                            'by loyal or bound ghosts, each with chosen starting Numina from the allowed list. You may '
                            'invest further Allies to expand those relationships, making your supernatural support '
                            'network one of your defining strengths in both investigation and defense. Friends in '
                            'Strange Places front-loads supernatural support through ghost retainers and customized '
                            'utility.',
                'book': 'Kith 91'},
 'moonborn': {'name': 'Moonborn',
              'skill': 'Empathy/Intimidation',
              'description': 'Emotionally tormented playthings kept in near-constant Bedlam, Moonborn return with '
                             'volatile passions, fierce empathy, and deep scars around attachment, identity, and '
                             'trust. Many become defenders and mentors for new Lost who feel emotionally unmoored, '
                             'while others become dangerous bridge-burners who spread the same chaos once carved into '
                             'their own hearts. Moonborn were emotional test subjects kept in constant Bedlam, making '
                             'attachment and regulation lifelong battles. Many become protectors of new escapees, '
                             'while others externalize that trauma and spread chaos in return. Storytellers can '
                             'foreground this kith by presenting scenes where its role, trauma, and social reputation '
                             'all matter at once.',
              'blessing': 'Full Moon Catharsis: once per chapter, spend 1 Glamour and roll Manipulation + Expression '
                          'to trigger mass emotional destabilization in up to Wyrd targets, contested by Composure + '
                          'Tolerance. Those who fail gain one chosen emotional Condition, letting you weaponize your '
                          'own remembered overwhelm as a controlled outburst. Full Moon Catharsis converts personal '
                          'trauma memory into controlled mass emotional disruption once per chapter.',
              'book': 'Kith 92'},
 'uttervoice': {'name': 'Uttervoice',
                'skill': 'Intimidation',
                'description': 'Creators whose blocked longing and frustration were weaponized until their voices '
                               'became instruments of terror, shock, and destruction in Arcadian war. Some Uttervoices '
                               'barely speak above a whisper while others lean into open threat, but all struggle with '
                               'intimacy when ordinary communication can turn into collateral damage. Uttervoices were '
                               'forged from creative frustration into sonic weapons for fae warfare. Their social '
                               'lives are often marked by restraint, fear of collateral harm, and resentment at being '
                               'reduced to a voice that hurts. Storytellers can foreground this kith by presenting '
                               'scenes where its role, trauma, and social reputation all matter at once.',
                'blessing': 'Scream of Agony: spend 1 Glamour and unleash a scream contested by Presence + Wyrd versus '
                            "listeners' Composure + Tolerance, dealing bashing damage on failure and potentially "
                            'lethal on your exceptional success. You can sustain the scream by spending actions and '
                            'Glamour, and the force can shatter weak glass and trigger accidentally on certain '
                            'supernatural Presence rolls. Scream of Agony is high-collateral sonic force; positioning '
                            'and ally safety are as important as raw output.',
                'book': 'Kith 92'},
 'delver': {'name': 'Delver',
            'skill': 'Investigation',
            'description': "Relentless seekers forced to mine Arcadia's buried wealth and hidden secrets, often "
                           'surrendering pieces of themselves - voice, certainty, identity - in the dark. Delvers '
                           'return as patient and guarded specialists in recovering what was lost or hidden, and many '
                           'maintain hard-earned solidarity through coded vibration speech carried through the earth '
                           'itself. Delvers mined impossible wealth and secrets in isolation, often giving up pieces '
                           'of self in the process. Their underground communication culture and patience make them '
                           'excellent investigators, smugglers, and long-game operators. Storytellers can foreground '
                           'this kith by presenting scenes where its role, trauma, and social reputation all matter at '
                           'once.',
            'blessing': 'Tappingspeak: spend 1 Glamour to send encrypted tapped messages through earth-connected '
                        'surfaces to declared recipients within Wyrd miles, with instinctive understanding for '
                        'intended listeners. Other Delvers can intercept and decode; non-Delvers generally need '
                        'supernatural means, while you may spend Glamour and roll Investigation to decode intercepted '
                        'messages. Tappingspeak enables secure low-visibility coordination across distance, especially '
                        'when spoken channels are compromised.',
            'book': 'Kith 93'},
 'glimmerwisp': {'name': 'Glimmerwisp',
                 'skill': 'Persuasion',
                 'description': 'Living veils and fogs shaped to hide atrocity, scandal, and breaking points in '
                                'service to cruel masters who enjoyed outsourcing cruelty to willing cover stories. '
                                'Escaped Glimmerwisps can still cloud what others see, making them exceptional '
                                'emergency responders, fixers, and accomplices - or dangerous enablers who hide '
                                'exactly what should be confronted. Glimmerwisps were veils over atrocity, trained to '
                                'redirect attention and normalize the intolerable. After escape, some use that skill '
                                'for triage and de-escalation, while others slip into enabling violence behind a '
                                'perfumed haze. Storytellers can foreground this kith by presenting scenes where its '
                                'role, trauma, and social reputation all matter at once.',
                 'blessing': 'Concealing Mist: spend 1 Glamour to fill a room or nearby open area with perfumed haze '
                             'and roll Manipulation + Persuasion + Wyrd, contested by Resolve + Composure. Characters '
                             'who lose cannot perceive wrongdoing or shameful acts by others within the mist, and the '
                             'concealment lasts through the end of the scene. Concealing Mist controls what wrongdoing '
                             'can be perceived, shifting both accountability and witness dynamics.',
                 'book': 'Kith 94'},
 'gremlin': {'name': 'Gremlin',
             'skill': 'Crafts',
             'description': 'Brilliant obsessives trapped between perfection and destruction, Gremlins tear down '
                            'anything flawed - including their own nearly finished masterpieces - to rebuild it '
                            'correctly. Their volatile standards and furious precision make them indispensable makers '
                            'and infuriating allies, often tolerated because they can produce miracles under '
                            'impossible deadlines. Gremlins embody perfectionism so extreme that destruction becomes a '
                            'necessary step in creation. They are brilliant under pressure, but their intolerance for '
                            'flaws can strain every relationship around them. Storytellers can foreground this kith by '
                            'presenting scenes where its role, trauma, and social reputation all matter at once.',
             'blessing': 'Nightmare at 20,000 Feet: once per scene, spend 1 Glamour to convert an extended action into '
                         'an instant action, provided the work includes meaningful dismantling or destructive '
                         "teardown. This reflects your kith's paradoxical genius - destruction as acceleration - and "
                         'is especially potent in high-pressure repair or sabotage scenes. Nightmare at 20,000 Feet '
                         'compresses time by coupling destruction with rapid execution in critical moments.',
             'book': 'Kith 94'},
 'manikin': {'name': 'Manikin',
             'skill': 'Socialize',
             'description': "Runway figures, animated displays, and living canvases remade to present someone else's "
                            'vision flawlessly, whether adored as centerpieces or discarded as obsolete props. '
                            'Manikins survived through poise and purpose; many escape from storage, abandonment, or '
                            'theft, then leverage social adaptability to make any role, costume, setting, or audience '
                            'accept them as natural. Manikins survived as living display forms, props, and facades for '
                            "someone else's masterpiece. Their social advantage is effortless presentability, "
                            'especially in spaces where appearance matters more than substance. Storytellers can '
                            'foreground this kith by presenting scenes where its role, trauma, and social reputation '
                            'all matter at once.',
             'blessing': "Gold From Straw: spend 1 Glamour and roll Presence + Crafts to conceal an object's flaws for "
                         'one scene, granting up to +5 on related social rolls. In social maneuvering, this can raise '
                         'impression an extra step when presentation matters, without truly improving function - only '
                         'how convincingly value is perceived. Gold From Straw manipulates social valuation without '
                         'changing objective function, perfect for impression economies.',
             'book': 'Kith 95'},
 'oculus': {'name': 'Oculus',
            'skill': 'Persuasion',
            'description': 'Non-clairvoyant persuaders who make people see only the paths they prefer, whether as '
                           'diplomats, gamblers, envoys, or kingmakers in fragile freehold politics. Oculi learned in '
                           'Arcadia that everyone has a price and every argument has leverage points; in mortal '
                           'society they are brilliant negotiators and dangerous curators of false inevitability. '
                           'Oculi are non-clairvoyant persuaders who narrow options until their preferred path feels '
                           'inevitable. In court politics they can be kingmakers, grifters, or saboteurs depending on '
                           'who is paying attention. Storytellers can foreground this kith by presenting scenes where '
                           'its role, trauma, and social reputation all matter at once.',
            'blessing': 'Amaurosis Fugax: spend 1 Glamour and roll Presence + Persuasion + Wyrd contested by Resolve + '
                        'Tolerance to obscure all practical routes except the one you present. Whether the effect is '
                        'literal visual clouding or cognitive narrowing, your target is guided physically and mentally '
                        'toward your chosen destination or option. Amaurosis Fugax narrows choices into inevitability, '
                        'making route control and negotiation framing highly potent.',
            'book': 'Kith 95'},
 'polychromatic': {'name': 'Polychromatic',
                   'skill': 'Empathy',
                   'description': 'Emotion-modulators and living displays of shifting color, prized in Arcadia for '
                                  'keeping gatherings calm, safe, visually pleasing, and politically useful to their '
                                  'Keepers. In the mortal world, Polychromatics excel as mediators and '
                                  'crisis-soothers, wielding disarming beauty that asks little yet can emotionally '
                                  'overwhelm entire rooms when they choose to shine. Polychromatics were emotional '
                                  'regulators in volatile Arcadian gatherings, prized for safe beauty and '
                                  'de-escalation. They remain powerful mediators whose visual affect can either soothe '
                                  'conflict or overwhelm resistance. Storytellers can foreground this kith by '
                                  'presenting scenes where its role, trauma, and social reputation all matter at once.',
                   'blessing': 'Prismatic Heart: once per chapter, spend 1 Glamour to unleash a luminous surge of '
                               'color through your mien. Everyone else in the scene must spend Willpower or gain '
                               'Swooned, and Swooned characters suffer an additional penalty when resisting your '
                               'Empathy actions for the rest of the scene. Prismatic Heart is a scene-level emotional '
                               'overwhelm tool that strongly amplifies follow-up Empathy actions.',
                   'book': 'Kith 96'},
 'veneficus': {'name': 'Veneficus',
               'skill': 'Survival',
               'description': 'Arcadian cooks and gatherers whose craft blurs nourishment, medicine, and poison '
                              'through rare ingredients, sharp instincts, and ritual culinary precision. Venefici '
                              'often express devotion through feeding others, yet every meal can carry hidden '
                              'intention; comfort, confession, cure, and sabotage all emerge from the same practiced '
                              'hands. Venefici blur medicine and poison through culinary alchemy, and many show care '
                              'through feeding rituals. Their kitchens can heal, bind, expose, or betray, often with '
                              'the same ingredient list. Storytellers can foreground this kith by presenting scenes '
                              'where its role, trauma, and social reputation all matter at once.',
               'blessing': "Waste Not, Want Not: spend 1 Glamour reflexively to invert a plant's nature, making a "
                           'toxic plant edible or an edible one toxic. In play, this lets you rapidly adapt field '
                           'resources, alter social rituals around food, and turn ordinary ingredients into protective '
                           'medicine or subtle threat. Waste Not, Want Not is a fast polarity inversion that turns '
                           'ingredient context into tactical advantage.',
               'book': 'Kith 97'},
 'witchtooth': {'name': 'Witchtooth',
                'skill': 'Intimidation',
                'description': 'Predatory keepers of wild and abandoned places, remembered in stories as hags and '
                               'monsters but rooted in older truths about land, fear, and survival without permission. '
                               'Witchtooths prize autonomy above comfort, harvest Glamour through dread and '
                               'disorientation, and often become fierce, rough-edged mentors to those they judge '
                               'resilient enough to learn. Witchtooths channel the authority of wild and abandoned '
                               'places, harvesting fear as readily as Glamour. They guard autonomy fiercely, but often '
                               'become hard teachers for those they deem worth preparing. Storytellers can foreground '
                               'this kith by presenting scenes where its role, trauma, and social reputation all '
                               'matter at once.',
                'blessing': 'Nibble, Nibble, Little Mouse: spend 1 Glamour and roll Resolve + Intimidation to reshape '
                            'up to one square mile of local terrain into a frightening or misleading configuration for '
                            'Wyrd turns. Survival actions in that area suffer penalties, allowing you to control '
                            'atmosphere, pursuit, and territorial pressure during conflict scenes. Nibble, Nibble, '
                            'Little Mouse reshapes terrain expectation and pursuit outcomes over a meaningful local '
                            'footprint.',
                'book': 'Kith 97'},
 'bricoleur': {'name': 'Bricoleur',
               'skill': 'Crafts/Expression',
               'description': 'Mythmakers who connect unrelated symbols into transformative truths, turning language, '
                              'coincidence, and metaphor into practical power with alarming confidence. Bricoleurs are '
                              'ingenious, competitive, and maddeningly nonlinear thinkers - invaluable in a crisis, '
                              'exhausting in ordinary conversation, and quietly dangerous whenever identity, memory, '
                              'or narrative can be rewritten by intent. Bricoleurs survive by linking symbols into '
                              'living myths, turning scraps into systems and words into leverage. Their nonlinear '
                              'genius wins crises and starts arguments in equal measure. Storytellers can foreground '
                              'this kith by presenting scenes where its role, trauma, and social reputation all matter '
                              'at once.',
               'blessing': 'Creatio Ex Nihilo: with a thematically appropriate symbolic item, spend 1 Glamour and roll '
                           'Wits + Persuasion to alter a core truth about yourself for days equal to Wyrd. Others '
                           'accept the new myth as real while it lasts, and rumors persist that your fetch mirrors the '
                           'transformation in permanent ways. Creatio Ex Nihilo is identity myth-engineering; the '
                           'symbolic component keeps it narratively grounded and costly.',
               'book': 'Kith 98'},
 'cloakskin': {'name': 'Cloakskin',
               'skill': 'Social',
               'description': 'Changelings whose Masks are unseen by mortal eyes, leaving only shadow and implication '
                              'where a face should be, even under direct light. Cloakskins are often nomadic and '
                              'digitally social, aching for normal contact while navigating a life where visibility, '
                              'recognition, trust, and intimacy are perpetually unstable currencies. Cloakskins are '
                              'unseen by most mortals under the Mask and often become nomadic by necessity. They crave '
                              'ordinary human contact while living in an economy of invisibility, aliases, and '
                              'distance. Storytellers can foreground this kith by presenting scenes where its role, '
                              'trauma, and social reputation all matter at once.',
               'blessing': 'Now You See Me: spend 1 Glamour and roll Presence + Stealth + Wyrd to vanish from sight '
                           'for a scene, hiding even from cameras. You remain detectable by sound, touch, and scent, '
                           'but sight-based detection fails outright while other sense-based attempts suffer heavy '
                           'penalties. Now You See Me hard-counters visual detection and recording, emphasizing '
                           'multisensory counterplay instead.',
               'book': 'Kith 98'},
 'doppelganger': {'name': 'Doppelganger',
                  'skill': 'Empathy',
                  'description': 'Subtle mimics who rarely become perfect copies, but steal enough familiar detail to '
                                 'destabilize trust, memory, and instinctive social comfort. Born from lures, mistaken '
                                 'identity, and longing to be loved differently, Doppelgangers weaponize recognition '
                                 'itself and can turn every room into a soft paranoia spiral. Doppelgangers weaponize '
                                 'partial familiarity rather than perfect imitation, stealing trust through tiny '
                                 'echoes of someone else. Their power is most dangerous when social certainty is '
                                 'already fragile. Storytellers can foreground this kith by presenting scenes where '
                                 'its role, trauma, and social reputation all matter at once.',
                  'blessing': "Sea-Witch's Bargain: spend 1 Glamour and roll Presence + Empathy + Wyrd contested by "
                              'Resolve + Tolerance to steal a physical or auditory trait for days equal to Wyrd. The '
                              'target loses that trait until duration ends or they complete your declared task to win '
                              "it back early. Sea-Witch's Bargain ties trait theft to task economy, creating social "
                              'quests as part of power resolution.',
                  'book': 'Kith 99'},
 'lethipomp': {'name': 'Lethipomp',
               'skill': 'Empathy',
               'description': 'Walking oblivions who endured so much feeling that they now carry a terrifying calm, '
                              'pulling emotion out of memory like poison from a wound. Lethipomps offer relief from '
                              'grief, shame, and guilt at steep cost, collecting intimate suffering that can later '
                              'erupt outward as reenacted trauma. Lethipomps absorb emotion from memory and can offer '
                              'relief at a cost few fully grasp. Their therapeutic potential is real, but so is their '
                              'capacity to curate pain as social currency. Storytellers can foreground this kith by '
                              'presenting scenes where its role, trauma, and social reputation all matter at once.',
               'blessing': 'Waters of Lethe: spend 1 Glamour and roll Composure + Empathy + Wyrd contested by the '
                           'target to absorb emotions tied to a known memory. The target becomes temporarily Lethargic '
                           'while you bear an appropriate emotional Condition and may Incite Bedlam to recreate '
                           'elements of what you absorbed. Waters of Lethe trades emotional burden transfer for '
                           'temporary impairment and possible Bedlam reenactment fallout.',
               'book': 'Kith 99'},
 'lullescent': {'name': 'Lullescent',
                'skill': 'Stealth',
                'description': 'Mute listeners of Arcadia - transformed into flowers, mirrors, fixtures, and hidden '
                               'observers who heard everything while being denied a voice. Lullescents return with '
                               'extraordinary hearing, disciplined stillness, and unsettling patience, making them '
                               'feared informants, court servants, and quiet political threats in any freehold. '
                               'Lullescents were denied voice and made into listening instruments, then escaped by '
                               'weaponizing what they overheard. Their hearing and patience make them prized aides and '
                               'feared blackmail risks. Storytellers can foreground this kith by presenting scenes '
                               'where its role, trauma, and social reputation all matter at once.',
                'blessing': 'Song of Silence: spend 1 Glamour to invoke echolocation for navigation, distance '
                            'judgment, and object location without line of sight. With a successful Wits + Occult + '
                            'Wyrd roll, you can also reveal magically hidden entities or objects, potentially '
                            'triggering a Clash of Wills against active concealment. Song of Silence gives non-visual '
                            'mapping plus anti-concealment pressure through Clash-capable echolocation.',
                'book': 'Kith 100'},
 'riddleseeker': {'name': 'Riddleseeker',
                  'skill': 'Investigation',
                  'description': 'Compulsive hunters of meaning who soothed Keepers with riddles, guarded thresholds '
                                 'with questions, and learned to treat ignorance as existential danger. Riddleseekers '
                                 "are lore-drunk problem-solvers with one eye always turned toward Arcadia's "
                                 'unfinished puzzles, hoarded answers, and dangerous questions no one else dares ask. '
                                 'Riddleseekers treated knowledge as survival in Arcadia and still chase meaning '
                                 'compulsively. They can end conflict through wit, but their curiosity often drags '
                                 'them toward dangerous truths. Storytellers can foreground this kith by presenting '
                                 'scenes where its role, trauma, and social reputation all matter at once.',
                  'blessing': 'Neck Riddle: spend 1 Glamour and roll Wits + Expression + Wyrd to force a conflict '
                              'toward riddle-resolution instead of immediate escalation. If your target cannot answer '
                              'within limited guesses, they must release the conflict until scene end, creating '
                              'tactical breathing room through wit, ritual, and symbolic authority. Neck Riddle '
                              'transforms direct conflict into constrained puzzle arbitration with temporary '
                              'disengagement stakes.',
                  'book': 'Kith 100'},
 'sideromancer': {'name': 'Sideromancer',
                  'skill': 'Occult',
                  'description': "Wyrd-attuned diviners who survived Arcadia's impossible causality and now read "
                                 'futures through chosen mortal methods such as cards, lots, bones, writing, numbers, '
                                 'or omen-casting. Sideromancers crave certainty in unstable social worlds, '
                                 'specializing in promises, debts, and consequences that follow pledges like gravity. '
                                 'Sideromancers read Wyrd turbulence through chosen divinatory forms, seeking '
                                 'certainty in obligation and consequence. Their forecasts are strongest in immediate '
                                 'pledge-economies, not distant prophecy. Storytellers can foreground this kith by '
                                 'presenting scenes where its role, trauma, and social reputation all matter at once.',
                  'blessing': 'Panomancy: spend 1 Glamour and perform at least five minutes of your chosen divination, '
                              'then roll Wits + Occult + Wyrd to ask yes-or-no questions about imminent promises, '
                              'obligations, debts, or payments involving you as a primary party. This power is '
                              'intentionally short-horizon; pushing farther risks dramatic failure. Panomancy is '
                              'strongest for immediate pledge/debt decisions, not distant forecasting, and punishes '
                              'overreach harshly.',
                  'book': 'Kith 101'},
 'spiegelbild': {'name': 'Spiegelbild',
                 'skill': 'Persuasion',
                 'description': 'Truth-bent mirror dwellers who live between reflection and refraction, compelled '
                                'toward revelation but skilled at framing exactly how truth is delivered. '
                                'Spiegelbilder thrive on secrets, social pressure, and perspective control, and can '
                                'turn ordinary reflective surfaces into dangerous confessionals where image and '
                                'honesty become bargaining chips. Spiegelbilder live between reflection and '
                                'refraction, compelled toward truth but skilled in framing it. They are invaluable '
                                'confidants and deeply unsafe secret-keepers. Storytellers can foreground this kith by '
                                'presenting scenes where its role, trauma, and social reputation all matter at once.',
                 'blessing': 'Mirror, Mirror on the Wall: spend 1 Glamour and roll Wits + Composure to enter '
                             'mirror-space through a reflective surface, then observe and listen from within it for '
                             'the scene. While present you are bound to truthful answers if questioned, unless you '
                             'also successfully conceal your presence with a contested stealth roll. Mirror, Mirror on '
                             'the Wall grants remote observation with truth-binding risk while inside reflective '
                             'space.',
                 'book': 'Kith 102'},
 'asclepian': {'name': 'Asclepian',
               'skill': 'Medicine',
               'description': 'Arcadian combat medics, menders, and mad surgeons who learned to heal with impossible '
                              'grafts, improvised tools, and battlefield pragmatism unconcerned with mortal standards. '
                              'Asclepians are prized in nearly every freehold because they can stabilize and rebuild '
                              'what should be beyond saving, though their miracles often leave permanent uncanny '
                              'additions behind. Asclepians practiced impossible salvage medicine in places where '
                              'ethics and biology were optional. Freeholds court them aggressively because they can '
                              'stabilize the unsalvageable with whatever is at hand. Storytellers can foreground this '
                              'kith by presenting scenes where its role, trauma, and social reputation all matter at '
                              'once.',
               'blessing': 'Grafting: spend 1 Glamour and roll Intelligence + Medicine to perform emergency surgery '
                           'using available materials, from flowers and wire to engine parts and ritual scraps. You '
                           'can stabilize the dying, heal beyond normal limits, and resolve suitable persistent '
                           'physical Conditions, but grafts remain permanent until painfully removed. Grafting permits '
                           'impossible emergency intervention and persistent-condition fixes at visible bodily cost.',
               'book': 'Kith 103'},
 'bridgeguard': {'name': 'Bridgeguard',
                 'skill': 'Intimidation',
                 'description': 'Rear-guard legends forged through unwinnable trials until they could hold chokepoints '
                                'against overwhelming force and weaponize stubbornness into doctrine. Bridgeguards are '
                                'planners as much as warriors, experts at choosing ground, dictating tempo, and '
                                'standing visibly defiant precisely when everyone else has already begun to retreat. '
                                'Bridgeguards were forged in unwinnable scenarios until outnumbered became their '
                                'comfort zone. They excel at choosing terrain, anchoring retreats, and making costly '
                                'stands matter. Storytellers can foreground this kith by presenting scenes where its '
                                'role, trauma, and social reputation all matter at once.',
                 'blessing': 'Against the Odds: when outnumbered, spend 1 Glamour and roll Composure + Intimidation to '
                             'gain a Defense bonus from successes and ignore multi-attacker Defense reduction for the '
                             'scene. The blessing requires no action, making you exceptionally effective at sudden '
                             'holds, retreats, and last-stand maneuvers. Against the Odds converts being outnumbered '
                             'into defensive superiority and stable front-line endurance.',
                 'book': 'Kith 104'},
 'librorum': {'name': 'Librorum',
              'skill': 'Intimidation',
              'description': 'Wardens and retrieval specialists of dangerous archives, stolen lore, and whispered '
                             'secrets considered too valuable for open shelves or public memory. Librorum return with '
                             'curated fragments of Arcadian knowledge and the habits of professional guardianship, '
                             'making them indispensable investigators and deeply difficult people to deceive or '
                             'dislodge. Librorum guarded and retrieved dangerous knowledge under direct fae '
                             'supervision. Their escapes often included stolen archives, making them hunted assets and '
                             'strategic liabilities. Storytellers can foreground this kith by presenting scenes where '
                             'its role, trauma, and social reputation all matter at once.',
              'blessing': 'Stolen Knowledge: once per chapter, spend 1 Glamour and roll Intelligence + Occult + Wyrd '
                          'after brief meditative recall. Allocate successes as temporary Library or Language Merit '
                          'dots, or as Repository value, representing specific remembered volumes and cataloged '
                          "secrets taken from your Keeper's hidden collections. Stolen Knowledge turns meditation into "
                          'temporary scholarly infrastructure exactly when needed.',
              'book': 'Kith 104'},
 'liminal': {'name': 'Liminal',
             'skill': 'Survival/Streetwise',
             'description': 'Threshold-beings of roads, gates, desks, forests, and borders, shaped to test passage, '
                            'set terms, and enforce conditional movement between states. Liminals understand '
                            'transitions better than most Lost, often helping others escape through technicality and '
                            'timing while turning crossings into binding social and mystical battlegrounds. Liminals '
                            'are threshold specialists who enforce conditions at borders literal and symbolic. They '
                            'are often the hidden reason a route opened - or closed - at the exact wrong moment. '
                            'Storytellers can foreground this kith by presenting scenes where its role, trauma, and '
                            'social reputation all matter at once.',
             'blessing': 'Line in the Sand: while physically on a threshold, declare crossing conditions and spend 1 '
                         'Glamour to roll Resolve + Intimidation + Wyrd contested by Composure + Tolerance. Those who '
                         'fail are not physically blocked, but crossing in violation inflicts the Lost Condition and '
                         'disorients their intent. Line in the Sand imposes conditional crossing penalties that alter '
                         'behavior without hard physical barriers.',
             'book': 'Kith 105'},
 'reborn': {'name': 'Reborn',
            'skill': 'Occult',
            'description': 'Favorites repeatedly broken down and remade by Gentry experimentation until only a '
                           'hardened core identity survived through cycles of destruction and replacement. Reborn '
                           'carry adaptive Arcadian design in their blood, letting them retune themselves after injury '
                           'and reconfigure capability around immediate survival needs. Reborn survived repeated '
                           'teardown-and-rebuild cycles that stripped everything but core identity. Their adaptive '
                           'self-retuning reflects both hard resilience and lingering body-memory of being remade. '
                           'Storytellers can foreground this kith by presenting scenes where its role, trauma, and '
                           'social reputation all matter at once.',
            'blessing': 'Retune: after taking lethal damage, spend 1 Glamour and roll Intelligence + Occult to '
                        'temporarily move Skill dots from one Skill to another for the scene, capped by Wyrd limits. '
                        'Once per chapter, you may spend 1 Willpower dot to make a similar redistribution permanent '
                        'instead. Retune offers dynamic skill redistribution under injury pressure, including rare '
                        'permanent reconfiguration options.',
            'book': 'Kith 105'},
 'stoneflesh': {'name': 'Stoneflesh',
                'skill': 'Intimidation',
                'description': 'Juggernauts forged for endurance: trolls, bronze beasts, knight-plates, and other '
                               'stubborn forms built to outlast cruelty through sheer durability and refusal. '
                               'Stoneflesh frequently become the pillars of motleys and communities, meeting threat '
                               'with calm inevitability and refusing to move once they decide where the line is. '
                               'Stoneflesh were engineered for endurance and often become social pillars after escape. '
                               'Their calm persistence can read as kindness or intimidation depending on who is '
                               'confronting them. Storytellers can foreground this kith by presenting scenes where its '
                               'role, trauma, and social reputation all matter at once.',
                'blessing': 'Obdurate Skin: spend 1 Glamour and roll Stamina + Athletics + Wyrd, then divide successes '
                            'between Armor, Resolve, and Composure for the scene. This allows flexible defense against '
                            'both physical and social pressure, reinforcing your role as anchor under sustained '
                            'assault or intimidation. Obdurate Skin flexibly allocates resilience across armor and '
                            'mental steadiness for scene-long durability.',
                'book': 'Kith 106'},
 'wisewitch': {'name': 'Wisewitch',
               'skill': 'Persuasion',
               'description': "Rare changelings marked by direct contact with a Keeper's Title, carrying visible or "
                              'symbolic traces of that power in body, behavior, or fate. Wisewitches are practical '
                              'warning-givers, hedge mystics, and disciplined dealmakers whose authority extends '
                              'beyond fae circles into spirit and angelic negotiations. Wisewitches carry marks from '
                              "contact with a Keeper's Title and read power-lines others ignore. They are rare "
                              'dealmakers where fae, spirit, and angelic obligations intersect. Storytellers can '
                              'foreground this kith by presenting scenes where its role, trauma, and social reputation '
                              'all matter at once.',
               'blessing': 'Keen Bargains: you can form pledges with spirits and angels not of fae kind, expanding '
                           'your diplomatic and ritual reach far beyond ordinary changeling boundaries. In chronicles '
                           "heavy on cross-supernatural politics, this blessing can make a Wisewitch the freehold's "
                           'most valuable intermediary. Keen Bargains broadens pledge diplomacy beyond fae, enabling '
                           'high-value cross-splat negotiations.',
               'book': 'Kith 106'},
 'airtouched': {'name': 'Airtouched',
                'skill': 'Athletics',
                'description': 'Windswept survivors of distance and disconnection, remade as mountain-peaks, '
                               "cloud-forms, and circling birds in Arcadia's high and lonely spaces. Airtouched often "
                               'crave closeness while fearing attachment, and carry a literal lightness that lets them '
                               'drift over fragile surfaces that should never hold a human body. Airtouched were '
                               'shaped through distance and atmospheric isolation, leaving profound attachment hunger '
                               'and avoidance side by side. Their movement style reflects that liminal separation from '
                               'ground and crowd. Storytellers can foreground this kith by presenting scenes where its '
                               'role, trauma, and social reputation all matter at once.',
                'blessing': 'The Drift: spend 1 Glamour to invoke almost weightless movement, letting you cross water, '
                            'snow, and fragile surfaces without breaking through or leaving clear traces. Treat your '
                            'weight as only ounces for practical movement effects, and apply penalties to tracking '
                            'attempts based on your Wyrd. The Drift enables improbable traversal and tracking '
                            'suppression by re-defining effective weight.',
                'book': 'Kith 107'},
 'chalomot': {'name': 'Chalomot',
              'skill': 'Empathy',
              'description': 'Dream-road scouts and Bastion infiltrators trained by repetition, manipulation, and '
                             'reality erosion until only oneiric logic felt trustworthy. Chalomot move through dreams '
                             'with practiced predatory confidence, guiding oneiromancers through hostile spaces and '
                             'unraveling layered sleeping defenses that can trap the unprepared for entire stories. '
                             'Chalomot mapped Dreaming Roads and Bastion seams until dream logic felt more real than '
                             'waking continuity. They remain elite navigators of oneiric risk and entrapment. '
                             'Storytellers can foreground this kith by presenting scenes where its role, trauma, and '
                             'social reputation all matter at once.',
              'blessing': 'Dreamtread: spend 1 Glamour to gain a bonus to dreamweaving rolls equal to half Wyrd '
                          '(minimum 1) for the rest of the scene. You may spend extra Glamour to share this benefit '
                          'with allied oneiromancers in the same Bastion, enabling coordinated dream operations. '
                          'Dreamtread is a multiplier for coordinated oneiromancy teams operating in the same Bastion.',
              'book': 'Kith 107'},
 'chevalier': {'name': 'Chevalier',
               'skill': 'Persuasion/Intimidation',
               'description': 'Riders and drivers shaped by Arcadian ideals of mounted champions, bound emotionally '
                              'and mystically to steeds ranging from living mounts to roaring engines. Chevaliers '
                              'treat movement as identity, form deep attachments to chosen rides, and fight with '
                              'greatest confidence when saddle, cockpit, handlebars, or reins are in hand. Chevaliers '
                              'embody rider-steed bond myths across both animal and machine forms. Their identity is '
                              'inseparable from mobility, loyalty, and the politics of who gets carried to safety. '
                              'Storytellers can foreground this kith by presenting scenes where its role, trauma, and '
                              'social reputation all matter at once.',
               'blessing': "Rider's Call: spend 1 Glamour to designate a touched mount or vehicle as your Noble Steed, "
                           'then later spend Glamour reflexively to call it to you across realms if physically '
                           'possible. Sapient steeds can refuse, contested claims can trigger Clash of Wills, and your '
                           "steed senses your danger when you are compromised. Rider's Call formalizes steed bond "
                           'logistics across distance and crises, with consent and clash safeguards.',
               'book': 'Kith 107'},
 'farwalker': {'name': 'Farwalker',
               'skill': 'Survival',
               'description': 'Endless patrollers of realm-borders and horizon cracks, often chosen from mortals '
                              'already familiar with long solitary routes, shift work, and survival under isolation. '
                              'Farwalkers map danger, locate routes, and make shelter where there should be none, '
                              'serving as dependable trailblazers through wilderness, Hedge, and contested '
                              "no-man's-land. Farwalkers learned border patrol and route endurance as a way of life. "
                              'They are often the first to find escapees and the last to abandon a bad trail. '
                              'Storytellers can foreground this kith by presenting scenes where its role, trauma, and '
                              'social reputation all matter at once.',
               'blessing': 'Home Away from Home: spend Glamour in wild terrain to create a temporary one-dot Safe '
                           'Place for a day, sized by half your Wyrd and expandable with extra Glamour. In the Hedge, '
                           'this instead reduces local Hedge hostility and can project one feature of your own Hollow '
                           'into the shelter. Home Away from Home creates reliable temporary shelter and can project '
                           'hollow utility into the field.',
               'book': 'Kith 108'},
 'flickerflash': {'name': 'Flickerflash',
                  'skill': 'Athletics',
                  'description': 'Restless couriers and speed-junkie escapees whose Arcadian service turned ordinary '
                                 'longing for movement into urgent physical necessity and existential strategy. '
                                 'Flickerflashes run messages, outrun Huntsmen, and often overcompensate for old '
                                 'loyalties by proving repeatedly - and sometimes recklessly - that no one will ever '
                                 'catch them again. Flickerflashes are restlessness made flesh, using speed as both '
                                 'survival strategy and emotional regulation. Many keep scorecards of rescues and '
                                 'deliveries as proof of loyalty. Storytellers can foreground this kith by presenting '
                                 'scenes where its role, trauma, and social reputation all matter at once.',
                  'blessing': 'Instantaneous Velocity: spend 1 Glamour reflexively to triple your Speed before '
                              'applying any other modifiers, producing sudden inhuman acceleration. This blessing '
                              'defines your chase profile, supports rapid repositioning, and can turn a losing pursuit '
                              'into a blur of tactical initiative. Instantaneous Velocity is pure tempo control, '
                              'deciding chases before many opponents can react.',
                  'book': 'Kith 110'},
 'levinquick': {'name': 'Levinquick',
                'skill': 'Computer',
                'description': 'Electric, modern couriers adapted to grids, screens, and endless movement, often as '
                               'comfortable in the BriarNet as in crowded city streets. Levinquicks are jittery and '
                               'future-focused by habit, using infrastructure itself as route and refuge while fearing '
                               'stillness as a warning sign of recapture. Levinquicks are products of electric '
                               'modernity, perpetually in motion across digital and physical networks. Stillness feels '
                               'like capture to them, even in safety. Storytellers can foreground this kith by '
                               'presenting scenes where its role, trauma, and social reputation all matter at once.',
                'blessing': 'Lightning Walk: by touching a land-connected telecom device, spending 3 Glamour, and '
                            'rolling Wits + Athletics + Wyrd, you dissolve into the grid and reappear at another known '
                            'connected device within Wyrd miles. Extra Glamour can carry companions, while unwilling '
                            'transport may trigger Clash of Wills and moral consequences. Lightning Walk provides '
                            'high-cost, high-reach infrastructure transit with real ethical implications for unwilling '
                            'riders.',
                'book': 'Kith 110'},
 'swarmflight': {'name': 'Swarmflight',
                 'skill': 'Stealth',
                 'description': 'Changelings whose bodies can disassemble into coherent swarms - spiders, lights, '
                                'mice, insects, bubbles, or other mobile fragments of self depending on seeming and '
                                'story. Swarmflights are difficult to pin down emotionally and physically, often '
                                'scattering under stress and reforming only when threat or panic has passed. '
                                'Swarmflights disassemble identity into many moving parts, then reassemble when threat '
                                'recedes. Their perspective is distributed, watchful, and difficult for enemies to pin '
                                'down. Storytellers can foreground this kith by presenting scenes where its role, '
                                'trauma, and social reputation all matter at once.',
                 'blessing': 'Swarm Form: spend 1 Glamour to dissolve into your chosen swarm type, acting as a single '
                             'distributed body with shared senses and area effects. You gain strong resistance to many '
                             'personal attacks, can hinder and panic those in your area, and in suitable forms may '
                             'inflict lethal swarm attacks before reassembling. Swarm Form trades singular '
                             'vulnerability for distributed pressure, area disruption, and selective lethality.',
                 'book': 'Kith 110'},
 'swimmerskin': {'name': 'Swimmerskin',
                 'skill': 'Brawl',
                 'description': 'Aquatic myth made flesh: kelpie-riders, river-haunters, sea-brides, and deep-water '
                                'hunters shaped by drowning stories old as civilization itself. Swimmerskins move '
                                'between worlds as fluidly as between air and water, carrying strong ties to kinship, '
                                'predation, beauty, danger, and the irresistible pull of the depths. Swimmerskins draw '
                                'from global aquatic myth lineages and often build social power through ports and '
                                'river communities. Their waters are both refuge and hunting ground. Storytellers can '
                                'foreground this kith by presenting scenes where its role, trauma, and social '
                                'reputation all matter at once.',
                 'blessing': "The Selkie's Skin: you always breathe both air and water, and by spending 1 Glamour you "
                             'may reflexively shift to an aquatic lower form suited for powerful swimming. While '
                             'transformed, you move through water at double Speed and ignore underwater penalties for '
                             "weapons and complex actions. The Selkie's Skin grants seamless amphibious superiority "
                             'and underwater task normalcy on demand.',
                 'book': 'Kith 111'},
 'bearskin': {'name': 'Bearskin',
              'skill': 'Intimidation/Weaponry',
              'description': 'Conscript soldiers tempered in endless, often meaningless Arcadian wars until loyalty '
                             'itself became both weapon and scar carried into every future oath. Bearskins can become '
                             'unmatched defenders of chosen causes, but many struggle with guilt, identity, and the '
                             'urge to surrender themselves completely to a cause worth dying for. Bearskins were '
                             'conscripted into endless fae wars where loyalty was manufactured through attrition. '
                             'After escape, they often bind themselves to causes with dangerous totality. Storytellers '
                             'can foreground this kith by presenting scenes where its role, trauma, and social '
                             'reputation all matter at once.',
              'blessing': 'Dulce et Decorum Est: when an opponent yields in violence or you successfully coerce them, '
                          'spend 1 Glamour to replace one of their Aspirations with one of yours until story end. If '
                          'unfulfilled, their original Aspiration returns, highlighting your capacity to conscript '
                          'conviction itself. Dulce et Decorum est alters Aspiration economy to conscript motive, not '
                          'just body.',
              'book': 'Kith 111'},
 'beastcaller': {'name': 'Beastcaller',
                 'skill': 'Animal Ken',
                 'description': 'Handlers of Arcadian war-beasts, trained to tame, command, and sometimes become one '
                                'with goblin creatures far more dangerous than mortal animals. Beastcallers often find '
                                'solace in those bonds, but risk identity bleed and ethical collapse when beasts '
                                'become both companions and disposable combat bodies. Beastcallers were handlers of '
                                'goblin war-fauna and still navigate blurred lines between partnership and possession. '
                                'Their greatest strength and greatest ethical risk are often the same bond. '
                                'Storytellers can foreground this kith by presenting scenes where its role, trauma, '
                                'and social reputation all matter at once.',
                 'blessing': 'Night Rider: spend 1 Glamour and succeed on Presence + Animal Ken + Wyrd to possess a '
                             'goblin beast for turns equal to Wyrd. Damage to the beast echoes onto your own body, and '
                             'if the host dies while possessed you snap back with aggravated harm, making this power '
                             'potent but costly. Night Rider creates potent remote force projection while reflecting '
                             'host-body harm back to the user.',
                 'book': 'Kith 112'},
 'cyclopean': {'name': 'Cyclopean',
               'skill': 'Investigation',
               'description': 'Towering giants, living bulwarks, and sometimes architectural monstrosities remade to '
                              'be awe-inspiring and terrifying in equal measure for Arcadian spectacle and war. '
                              'Cyclopeans often bear lasting injuries from service, yet become steadfast protectors, '
                              'trackers, and front-line anchors for those they claim as kin. Cyclopeans were made to '
                              'be monumental, terrifying, and indispensable, often at the cost of lasting injury. They '
                              'frequently become visible protectors whose presence deters escalation. Storytellers can '
                              'foreground this kith by presenting scenes where its role, trauma, and social reputation '
                              'all matter at once.',
               'blessing': "Smell the Blood: once per scene, spend 1 Glamour to identify an enemy's vulnerabilities, "
                           'reducing penalties for targeted attacks and upgrading bashing to lethal on those strikes. '
                           'This turns your immense presence into surgical brutality when a confrontation must end '
                           'quickly. Smell the Blood improves called-shot lethality and rewards precision from an '
                           'otherwise brute profile.',
               'book': 'Kith 112'},
 'plaguesmith': {'name': 'Plaguesmith',
                 'skill': 'Medicine',
                 'description': 'Unwilling vectors forged for fae warfare, carrying tailored contagions that mirror '
                                "their Keepers' aesthetics, cruelty, and narrative logic of punishment. Plaguesmiths "
                                'can heal disease as expertly as they inflict it, often living with strict boundaries, '
                                "intrusive fear, and the persistent dread of becoming someone else's weapon again. "
                                'Plaguesmiths were cultivated as bioweapons and carry strict personal boundaries to '
                                'avoid repeating that role. Their healing skill and infectious threat coexist in '
                                'uneasy balance. Storytellers can foreground this kith by presenting scenes where its '
                                'role, trauma, and social reputation all matter at once.',
                 'blessing': 'Plague of Arcadia: on touch, spend 1 Glamour and roll Strength + Medicine + Wyrd '
                             'contested by Stamina + Tolerance to infect a target with a grave supernatural disease. '
                             'Symptoms can be fantastical and title-themed, recovery is demanding, and the condition '
                             'can inflict recurring aggravated damage over time. Plague of Arcadia is severe, '
                             'slow-burn pressure with storyteller-facing symptom design hooks.',
                 'book': 'Kith 113'},
 'razorhand': {'name': 'Razorhand',
               'skill': 'Brawl',
               'description': 'Changelings surgically and symbolically armed with blade-hands, crafted for pruning, '
                              "execution, display, artistry, or open war in their Keepers' domains. Razorhands live at "
                              'the edge between tenderness and violence - some embrace destruction, while others '
                              'struggle to heal despite carrying weaponized bodies they can never truly set aside. '
                              'Razorhands were physically weaponized for pruning, punishment, and spectacle. Many now '
                              'channel that precision into craft or defense while fearing accidental harm to those '
                              'they love. Storytellers can foreground this kith by presenting scenes where its role, '
                              'trauma, and social reputation all matter at once.',
               'blessing': 'Sakin: spend 1 Glamour to transform one hand into a 1L blade weapon for the scene, using '
                           'Brawl and unarmed styles; spend an additional Glamour for the off-hand as well. Cosmetic '
                           'form varies, but you cannot be disarmed short of limb removal, making your body a '
                           'permanent armory. Sakin makes the body an always-available weapon platform resistant to '
                           'conventional disarm tactics.',
               'book': 'Kith 114'},
 'sandharrowed': {'name': 'Sandharrowed',
                  'skill': 'Survival',
                  'description': "Nomads and storm-runners of Arcadia's brutal deserts, tempered by heat, scarcity, "
                                 'abrasive wind, and long marches through predatory emptiness. Sandharrowed carry '
                                 'desert discipline into every environment and can weaponize that memory directly, '
                                 'using moving grit and choking force to trap opponents who underestimate them. '
                                 'Sandharrowed survived Arcadian deserts by mastering scarcity, abrasion, and '
                                 'relentless weather. They bring that adaptability to every environment and weaponize '
                                 'terrain control naturally. Storytellers can foreground this kith by presenting '
                                 'scenes where its role, trauma, and social reputation all matter at once.',
                  'blessing': 'Enveloping Sands: once per scene, before a Brawl or Weaponry attack, spend 1 Glamour; '
                              'on a successful hit, a sand pillar erupts and inflicts Immobilized on the target. The '
                              'pillar has fixed Durability and provides cover while confining them, creating immediate '
                              'battlefield control from a single strike. Enveloping Sands adds once-per-scene '
                              'immobilization and cover dynamics off a successful hit.',
                  'book': 'Kith 115'},
 'valkyrie': {'name': 'Valkyrie',
              'skill': 'Persuasion/Intimidation',
              'description': 'Choosers of the slain shaped by mythic war iconography, forced to decide who rises and '
                             'who falls on Arcadian battlefields soaked in spectacle and sacrifice. Valkyries combine '
                             'battlefield charisma with occult fate-marking, granting resolve to allies and unraveling '
                             'enemies with declarations that land like sacred judgment. Valkyries were forced to '
                             'choose fates on battlefields designed as mythic theater. They carry that authority into '
                             'modern conflicts through morale shaping and selective doom. Storytellers can foreground '
                             'this kith by presenting scenes where its role, trauma, and social reputation all matter '
                             'at once.',
              'blessing': 'Chooser of the Slain: a limited number of times per scene, spend 1 Glamour and roll Wits + '
                          'Occult + Wyrd contested by Resolve + Tolerance to bless or curse a perceived target. On '
                          'success, you apply Inspired or Steadfast to allies, or Frightened or Reckless to foes. '
                          'Chooser of the Slain offers limited but repeatable morale-state assignment to allies and '
                          'enemies.',
              'book': 'Kith 115'},
 'venombite': {'name': 'Venombite',
               'skill': 'Brawl',
               'description': 'Assassins and saboteurs distilled from private resentments, with Arcadian venom running '
                              'where ordinary bitterness once lived quietly in the body. Venombites can appear almost '
                              'mundane until they strike; then personal grievance becomes precise biological warfare '
                              'delivered with the intimacy of a bite, grasp, or close-quarters hit. Venombites distill '
                              'quiet resentments into lethal close-quarters toxin. Their menace lies in appearing '
                              'ordinary until one committed strike changes everything. Storytellers can foreground '
                              'this kith by presenting scenes where its role, trauma, and social reputation all matter '
                              'at once.',
               'blessing': 'Deadly Bite: once per scene, before a Brawl attack, spend 1 Glamour to infuse the strike '
                           "with your kith's toxin. On success, the attack deals lethal damage and inflicts a grave "
                           'Poisoned effect in addition to normal harm, translating old resentment into immediate '
                           'physiological collapse. Deadly Bite front-loads lethal and poison effects into a single '
                           'close-range success each scene.',
               'book': 'Kith 116'},
 'apoptosome': {'name': 'Apoptosome',
                'skill': 'Miscellaneous',
                'description': 'Self-renewing survivors trapped in isolated fortresses, dying and reforming over and '
                               'over until their bodies became living archives of remembered harm and adaptation. '
                               'Apoptosomes often return with fractured boundaries and defensive aggression, but also '
                               'with perfect recall of prior defeat patterns and a brutal knack for making old enemies '
                               'bleed with them. Apoptosomes endured endless death-and-return cycles in isolated '
                               'kill-mazes, accruing combat memory as scar tissue. They often read disagreement as '
                               'imminent threat and retaliate preemptively. Storytellers can foreground this kith by '
                               'presenting scenes where its role, trauma, and social reputation all matter at once.',
                'blessing': 'Sparagmos: in conflict with someone who has hurt you before, spend 1 Glamour to deal '
                            'immediate aggravated damage to that foe. For the remainder of the scene, every time those '
                            'returning enemies damage you, both they and you suffer an additional aggravated point, '
                            'escalating the violence through shared ruin. Sparagmos escalates reciprocal aggravated '
                            'harm, favoring short brutal exchanges over attrition.',
                'book': 'Kith 116'},
 'becquerel': {'name': 'Becquerel',
               'skill': 'Stealth',
               'description': 'A newer kith born from nuclear-era anxieties, shaped into shadowy poisoners and silent '
                              'killers marked by radiant ruin and hush-filled dread. Becquerels often escape in '
                              'spectacular bursts through the Hedge and carry a dangerous touch that burns flesh in '
                              'patterns reminiscent of fallout and irradiated shadow. Becquerels emerged from '
                              'nuclear-era dread, styled as shadowy radiance and lingering burn. Their touch is feared '
                              'for what it does to bodies and what it symbolizes culturally. Storytellers can '
                              'foreground this kith by presenting scenes where its role, trauma, and social reputation '
                              'all matter at once.',
               'blessing': 'Nuclear Shadow: when you successfully grapple, spend 1 Glamour to burn the target as a '
                           'supernatural heat-shadow effect that resembles radiation injury to mundane scans. Each '
                           'turn you maintain the hold, you may apply Stunned or Poisoned, making prolonged contact '
                           'increasingly devastating. Nuclear Shadow applies thematic burn plus ongoing tilt pressure '
                           'while maintaining grapple control.',
               'book': 'Kith 117'},
 'blightbent': {'name': 'Blightbent',
                'skill': 'Disease/Poison',
                'description': "Workers of Arcadia's most toxic pits, furnaces, bogs, and chemical wastes, remade to "
                               'survive contamination by becoming part of it. Blightbent carry industrial scars, '
                               'lingering stench, and hard-earned resilience, often thriving where others fail while '
                               'finding ordinary social reintegration painfully difficult and physically complicated. '
                               'Blightbent survived toxic labor by becoming toxic themselves, and reintegration is '
                               'often physically and socially punishing. They carry industrial memory as both '
                               'resilience and stigma. Storytellers can foreground this kith by presenting scenes '
                               'where its role, trauma, and social reputation all matter at once.',
                'blessing': 'Brimstone: after a successful grapple, spend 1 Glamour to inflict Poisoned through your '
                            'caustic touch. Combined with your natural resistance profile and contamination narrative, '
                            'this lets you function as both hazard specialist and close-range threat in environments '
                            'most kiths would avoid entirely. Brimstone converts successful close contact into '
                            'immediate poisoning, reinforcing contamination identity.',
                'book': 'Kith 117'},
 'enkrateia': {'name': 'Enkrateia',
               'skill': 'Empathy/Persuasion/Subterfuge',
               'description': "Rare 'better angels' of Arcadia: mediators, analysts, judges, and counselors created to "
                              'advise Keepers through conflict, vanity, and strategic overreach. Enkrateia return as '
                              'dispassionate de-escalators with precise situational analysis, often indispensable in '
                              'freehold politics where everyone else runs too hot and too proud. Enkrateia served as '
                              'advisors and mediators where Keepers wanted reason without accountability. In '
                              'freeholds, they excel when emotions outrun strategy. Storytellers can foreground this '
                              'kith by presenting scenes where its role, trauma, and social reputation all matter at '
                              'once.',
               'blessing': 'Eloquent Analysis: during extended Investigation, you begin losing dice only after the '
                           'third successive roll, representing exceptional composure under pressure and methodical '
                           'reasoning. This makes you especially strong in tense social inquiries, layered '
                           'conspiracies, and drawn-out evidence synthesis scenes. Eloquent Analysis extends effective '
                           'investigation streak length before dice attrition begins.',
               'book': 'Kith 118'},
 'gravewight': {'name': 'Gravewight',
                'skill': 'Empathy/Intimidation',
                'description': "Executioners, psychopomps, and keepers of Arcadian dead who learned death's mechanics "
                               'too intimately to fear them in ordinary ways. Gravewights are often pragmatic rather '
                               'than theatrical, carrying grave-sense, ghost attention, and unnerving calm around '
                               'mortality that others read as either comfort or threat. Gravewights performed '
                               'death-work close to chthonic powers and returned with unusual composure around '
                               'mortality. Their presence attracts ghosts and obligations in equal measure. '
                               'Storytellers can foreground this kith by presenting scenes where its role, trauma, and '
                               'social reputation all matter at once.',
                'blessing': 'Charnel Sight: spend 1 Glamour to see and hear ghosts lingering in Twilight, while your '
                            'broader presence naturally attracts liminal dead and other in-between entities. In '
                            'practice this grants investigation leverage, social complication, and constant contact '
                            'with voices most people never hear. Charnel Sight is equal parts sensory expansion and '
                            'narrative magnet for liminal entities.',
                'book': 'Kith 119'},
 'shadowsoul': {'name': 'Shadowsoul',
                'skill': 'Subterfuge',
                'description': 'Nocturnal counterparts to brighter kiths, remade as dusk-bound ornaments, hunters, and '
                               'attendants in the courts of night-aligned Keepers. Shadowsouls carry lunar and mirror '
                               'affinities, thrive in concealment and ambiguity, and often endure lingering frailties '
                               'tied to daylight, scrutiny, and prolonged exposure. Shadowsouls were shaped by '
                               'nocturnal courts and punished with daylight frailties. They thrive in concealment and '
                               'mirror-work while carrying resentment toward imposed darkness. Storytellers can '
                               'foreground this kith by presenting scenes where its role, trauma, and social '
                               'reputation all matter at once.',
                'blessing': 'Nightblind: gain natural affinity with Mirror in addition to existing regalia affinities, '
                            'and once per scene on an exceptional attack success you may inflict temporary Blindness '
                            'by touch. The blessing rewards ambush, precision, and decisive openings rather than '
                            'prolonged stand-up brawling. Nightblind combines strong mundane deceit support with '
                            'targeted scene-limited sensory denial.',
                'book': 'Kith 119'},
 'telluric': {'name': 'Telluric',
              'skill': 'Drive/Streetwise',
              'description': "Isolated stars set in Arcadia's moving heavens, constantly seen yet rarely truly engaged "
                             'by those below, admired at distance and starved of ordinary belonging. Tellurics return '
                             'with deep travel instinct, courier talent, and complicated intimacy patterns - craving '
                             'connection while reflexively casting themselves as distant and untouchable. Tellurics '
                             'were set in Arcadian skies as distant ornaments and navigational assets. They are seen '
                             'easily, known poorly, and often lonely even in company. Storytellers can foreground this '
                             'kith by presenting scenes where its role, trauma, and social reputation all matter at '
                             'once.',
              'blessing': 'Burn Bright: spend 1 Glamour to hurl a starflame projectile using Dexterity + Athletics, '
                          'dealing torch-sized supernatural fire with candle-level heat profile. The attack provides '
                          'reliable ranged pressure and thematic spectacle, especially in chases, escapes, and '
                          'night-sky set pieces. Burn Bright gives reliable ranged supernatural pressure with strong '
                          'thematic presentation.',
              'book': 'Kith 120'},
 'whisperwisp': {'name': 'Whisperwisp',
                 'skill': 'Subterfuge',
                 'description': 'Cold-information specialists forged through surveillance, interrogation, blackmail, '
                                'and sabotage, trained to hear everything and reveal only what serves strategic '
                                'intent. Whisperwisps are consummate manipulators of truth and lies, often operating '
                                "at arm's length from courts they advise, exploit, undermine, or quietly protect. "
                                'Whisperwisps were built for surveillance, interrogation, and covert disruption. They '
                                'are exceptional manipulators of disclosure, and rarely show their full hand. '
                                'Storytellers can foreground this kith by presenting scenes where its role, trauma, '
                                'and social reputation all matter at once.',
                 'blessing': 'Forked Tongue: choose Stealth or Persuasion at character generation; rolls with that '
                             'Skill gain both 9-again and a bonus equal to Wyrd. Combined with your truth-vs-falsehood '
                             'exceptional thresholds, this creates an unusually strong toolkit for espionage, '
                             'confidence games, and social pressure operations. Forked Tongue supercharges one '
                             'selected social or stealth channel with both bonus and reroll edge.',
                 'book': 'Kith 120'},
 'antiquarian': {'name': 'Antiquarian',
                 'skill': 'Empathy',
                 'description': 'Living vaults of secrets layered beneath other secrets, Antiquarians were built to '
                                "guard a Keeper's one true vulnerability by burying it under names, memories, and "
                                'confessions stolen from countless others. They survive by hoarding truth, speaking '
                                'rarely, and reading what people do not mean to reveal, then trading answers only when '
                                'the price is right. In Alexandria and similar centers, Antiquarians became '
                                'indispensable librarians and keepers of dangerous catalogues. They measure trust in '
                                'layers and rarely disclose everything at once. What they know can rescue a freehold '
                                'or ignite a war, depending on when they speak.',
                 'blessing': 'Secrets and Whispers: when using Empathy to uncover hidden truths, three successes count '
                             'as exceptional success. Once per session, spend 1 Glamour and roll Intelligence + '
                             'Composure to ask a question and draw an answer through research, intuition, omen, or '
                             'dream-whisper; required successes scale with how hidden the truth is. Secrets and '
                             'Whispers scales from ordinary research to occult revelation, depending on success and '
                             'narrative access.',
                 'book': 'DE2 69'},
 'chimera': {'name': 'Chimera',
             'skill': 'Subterfuge',
             'description': 'Arcadian composites stitched from multiple bestial forms - predator, courier, '
                            'executioner, and terror-weapon in one body shaped by experimentation. Chimera often '
                            'retain kinship with goblins and hedge denizens, understand deception in all its forms, '
                            'and carry the uneasy pride of those remade from many things that should never have fit '
                            'together. Chimera are common where Gentry experiment openly with form, especially in '
                            'realms that prize spectacle and utility. Their patchwork bodies often mirror patchwork '
                            'social identities among Lost. Tales of predators like the Geryo reinforce both their '
                            'caution and their ferocity.',
             'blessing': 'Goblin Kin: when using Subterfuge to detect spoken or written trickery, three successes '
                         'count as exceptional success. Each chapter, choose one Goblin Contract you know; that '
                         'Contract does not incur Goblin Debt when invoked, and this benefit rotates until all '
                         'eligible Goblin Contracts have been selected. Goblin Kin supports rotational versatility and '
                         "encourages regular use of the kith's broader Goblin Contract toolkit.",
             'book': 'CTL JS 47 / DE2 69'},
 'dryad': {'name': 'Dryad',
           'skill': 'Survival',
           'description': 'Woodbound changelings cultivated as living ornaments, wardens, and seasonal fixtures in '
                          'Arcadian gardens and sacred groves, bound to green life even when imprisoned. Dryads often '
                          'return preferring trees to crowds, navigating forest and Hedge with instinctive ease while '
                          'carrying a stillness that can make them vanish into leaf and bark as if they were never '
                          'there. Wooded domains and sacred gardens shaped their instincts toward green cover, rooted '
                          'patience, and quiet paths. Even in cities, many seek parks, courtyards, and overgrown '
                          'margins for safety. They often trust trees and thorns faster than people.',
           'blessing': 'Fade into the Foliage: in wooded areas (including the Hedge), Survival rolls for tracking and '
                       'pathfinding treat three successes as exceptional success. If unobserved for one turn, spend 1 '
                       'Glamour to conceal yourself behind substantial foliage; remain perfectly hidden while still, '
                       'and add Wyrd to Stealth when moving. Fade into the Foliage turns terrain into defense, '
                       'rewarding patience, sight-line control, and woodland positioning.',
           'book': 'DE2 70'},
 'muse': {'name': 'Muse',
          'skill': 'Mantle',
          'description': 'Catalysts of brilliance who inspire, pressure, and provoke excellence in others, Muses were '
                         'prized by Keepers and courts that measured power through monuments, performance, and legacy. '
                         'They are often socially magnetic and politically useful, able to elevate status by presence '
                         'alone and drive mortals toward creation that outlasts everyone involved. Muses in this era '
                         'were tied to monumental ambition, from city projects to reputational contests among courts. '
                         'Their influence can be benevolent inspiration or coercive pressure dressed as encouragement. '
                         'Either way, they leave marks on culture larger than themselves.',
          'blessing': 'Tyranny of Ideas: once per session, interact with other Lost as though your Mantle or court '
                      'Goodwill were one dot higher. By spending 1 Glamour and making an appropriate social roll '
                      "against a human target, you grant bonus dice to that target's creation roll and let three "
                      'successes count as exceptional success for the resulting work. Tyranny of Ideas creates '
                      'indirect power by amplifying mortal creators rather than harvesting glamour from their output.',
          'book': 'DE2 70'},
 'nymph': {'name': 'Nymph',
           'skill': 'Athletics',
           'description': 'Waterborn changelings shaped in the image of mythic sea-kin, thriving in harbors, '
                          'riverways, and hidden channels where information and tribute move together. Nymphs are '
                          'natural aquatic scouts and social powers in port communities, balancing hospitality and '
                          'danger with the same current that carried them out of Arcadia. Harbors and riverways make '
                          'them natural scouts, informants, and guardians of exchange. Their communities often involve '
                          'tribute, bargains, and territorial etiquette around water. Allies learn quickly that '
                          'generosity and danger share the same tide.',
           'blessing': 'Gift of Water: when making Athletics rolls while swimming, three successes count as '
                       'exceptional success. Spend 1 Glamour and succeed on a Stamina + Athletics roll to manifest '
                       'gills and an aquatic lower form, allowing air-and-water breathing, double swim speed, and '
                       'normal use of weapons and complex actions underwater for the scene. Gift of Water provides '
                       'sustained aquatic superiority, making ports, rivers, and flooded zones decisive home ground.',
           'book': 'DE2 70'},
 'cleverquick': {'name': 'Cleverquick',
                 'skill': 'Occult',
                 'description': "Quick-witted hunters and schemers trained in pairs to expose an enemy's hidden "
                                'weaknesses and weaponize them with ruthless timing. Cleverquicks thrive on '
                                'preparation, pattern recognition, and dangerous bargains, often acting as '
                                'monster-slayers, court operatives, or precision saboteurs who would rather win '
                                'cleverly than fight fairly. Many Cleverquicks operate best in pairs, where planning '
                                'and execution can be split with ruthless precision. They thrive on identifying the '
                                'one weakness that turns a superior foe into prey. Victory, for them, is proof of '
                                'preparation rather than brute force.',
                 'blessing': 'Know Your Enemy: when using Occult to outsmart an adversary, three successes count as '
                             'exceptional success. Spend 1 Glamour to learn one existing frailty, ban, or bane; spend '
                             '3 Glamour to impose a temporary one for the chapter, but you accept the same weakness '
                             'for that duration. Paired Cleverquicks may split costs and share outcomes.',
                 'book': 'DE2 368'}}


def get_kith(kith_key):
    """Get a specific kith by key."""
    return ALL_KITHS.get(kith_key.lower().replace(" ", "_"))


def get_all_kiths():
    """Get all kiths."""
    return ALL_KITHS.copy()

