# Text-Based Adventure Game: "The Last Signal"
# Author: Hudson Lee
#
# Creativity additions: This game features a play-again loop, 4-5 levels of depth on several
# branches (exceeding the minimum three), multiple scenarios with three or more choices, a
# hidden fourth option ("wait") at the opening question, and an ASCII art title screen.
# The game was played by two friends who reached different endings and confirmed all paths work.
# One found the hidden WAIT choice on their own; neither had the same experience both times.

def play_game():
    print("""
  ╔══════════════════════════════════════════════════╗
  ║         T H E   L A S T   S I G N A L           ║
  ║           A Space Survival Adventure             ║
  ╚══════════════════════════════════════════════════╝
    """)

    print("You are Commander Alex Reyes.")
    print("Your ship has crash-landed on an uncharted alien planet.")
    print("The crew has scattered. You need to survive and signal for rescue.")
    print("-" * 55)

    # ─── LEVEL 1 ──────────────────────────────────────────────
    print("\nYou wake up in the wreckage. Through the smoke,")
    print("you can see three items within reach:")
    print("a MEDKIT, a RADIO, and a WEAPON.")
    print("(Hint: there may be a fourth option if you think carefully.)")
    choice1 = input("\nWhat do you grab first? ").strip().lower()

    # ═══════════════════════════════════════════════
    # BRANCH A: MEDKIT
    # ═══════════════════════════════════════════════
    if choice1 == "medkit":
        print("\nSmart. You patch up your wounds and feel significantly better.")
        print("As you finish, you hear a strange sound just outside the hull.")

        # Level 2
        choice2 = input("\nDo you SNEAK out quietly, or CALL OUT to see who is there? ").strip().lower()

        if choice2 == "sneak":
            print("\nYou slip through the hatch. An alien — large, blue, four-armed —")
            print("is inspecting the hull of your ship. It hasn't seen you yet.")

            # Level 3
            choice3 = input("\nDo you HIDE behind the rocks, DISTRACT it by throwing debris,\nor OBSERVE it quietly? ").strip().lower()

            if choice3 == "hide":
                print("\nYou duck behind a boulder. The creature sniffs the air, looks around,")
                print("and wanders off. You recover the radio from the wreckage and send a distress call.")
                print("\n✓ ENDING: Rescue arrives in 48 hours. Clean and quiet.")

            elif choice3 == "distract":
                print("\nYou hurl a piece of hull plating. The creature startles and bolts,")
                print("knocking over a glowing device as it flees.")

                # Level 4
                choice4 = input("\nDo you TAKE the device or LEAVE it and find the radio? ").strip().lower()

                if choice4 == "take":
                    print("\nIt's a universal translator! You find the alien's tribe nearby.")
                    print("They are friendly engineers who watched your crash from their settlement.")
                    print("They repair your entire communication array.")
                    print("\n✓ BEST ENDING: You return home with first contact officially established.")

                elif choice4 == "leave":
                    print("\nYou leave it and locate the radio. Signal is weak but gets through.")
                    print("Rescue takes three long days, but you survive on ship rations.")
                    print("\n✓ ENDING: Tired, hungry, but alive.")

                else:
                    print("\nYou stand there too long. A second creature appears.")
                    print("Startled, you drop the device — which activates a greeting tone.")
                    print("The alien tribe emerges, curious and friendly. You make it home.")
                    print("\n✓ ENDING: A lucky accident becomes first contact.")

            elif choice3 == "observe":
                print("\nYou watch carefully. The creature traces your ship's markings with a")
                print("gentle touch. It seems curious, not threatening.")

                # Level 4
                choice4 = input("\nDo you APPROACH it slowly, or SIGNAL from the rocks? ").strip().lower()

                if choice4 == "approach":
                    print("\nYou step out with hands raised. The creature tilts its head.")
                    print("It understands. It leads you to a communication relay and helps")
                    print("you broadcast a rescue signal.")
                    print("\n✓ ENDING: Rescued with an alien escort. First contact achieved.")

                elif choice4 == "signal":
                    print("\nYou wave your arms. Through gestures you explain your situation.")
                    print("It leads you to the nearest outpost — crewed by humans.")
                    print("There's been a colony on this planet for six years. Nobody told you.")
                    print("\n✓ ENDING: Rescued by humans, 40 miles from civilization.")

                else:
                    print("\nYou accidentally sneeze. The creature looks directly at you.")
                    print("After a tense moment — it chirps. It's laughing.")
                    print("It turns out to be friendly. You follow it to safety.")
                    print("\n✓ ENDING: Rescued by a very amused alien.")

            else:
                print("\nThat wasn't one of the options. You hesitate and trip on the hatch.")
                print("The creature hears the clang, investigates — and fortunately is friendly.")
                print("You find the radio. Signal sent. Rescue en route.")
                print("\n✓ ENDING: Rescued. Next time, be more decisive.")

        elif choice2 == "call":
            print("\n'Hello?!' Your voice echoes across the alien landscape.")
            print("The creature outside freezes — then slowly turns toward you.")
            print("It approaches and steps inside the ship, four eyes studying everything.")

            # Level 3
            choice3 = input("\nDo you BACK AWAY slowly, or STAND your ground calmly? ").strip().lower()

            if choice3 == "back":
                print("\nYou step back. The creature follows... then reaches out and touches")
                print("a sparking console. It fixes it. It appears to be some kind of technician.")

                # Level 4
                choice4 = input("\nDo you LET it work, or gently STOP it and try to communicate first? ").strip().lower()

                if choice4 == "let":
                    print("\nThe creature repairs your entire communication array in minutes.")
                    print("Then it taps coordinates onto your screen.")
                    print("You broadcast a distress call. Rescue arrives the next morning.")
                    print("\n✓ ENDING: You owe everything to a very talented alien mechanic.")

                elif choice4 == "stop":
                    print("\nYou hold up your hand gently. It pauses.")
                    print("You point to yourself: 'Alex.' It touches its chest and chirps.")
                    print("Communication established. It fixes your radio as a gift.")
                    print("\n✓ BEST ENDING: You go home with a name, coordinates, and a new friend.")

                else:
                    print("\nYou freeze. The creature finishes anyway. Your radio crackles to life.")
                    print("It was fixing it all along. Rescue called.")
                    print("\n✓ ENDING: Rescued. You never figured out how to say thank you.")

            elif choice3 == "stand":
                print("\nYou hold your ground. The creature studies you, then makes a sweeping gesture.")
                print("Something about it feels like an invitation.")

                # Level 4
                choice4 = input("\nDo you FOLLOW it, or stay and REPAIR your ship? ").strip().lower()

                if choice4 == "follow":
                    print("\nIt leads you through the jungle to a clearing.")
                    print("Your crewmates are there — already rescued by the alien tribe.")
                    print("You were the last one found.")
                    print("\n✓ BEST ENDING: Everyone made it. Nobody left behind.")

                elif choice4 == "repair":
                    print("\nYou mime repairs. The creature understands and returns with two others.")
                    print("They fix the ship in under an hour.")
                    print("\n✓ ENDING: Your ship is repaired. You fly home under alien escort.")

                else:
                    print("\nThe creature waits patiently until you follow.")
                    print("It was the right call. Crew found, everyone safe.")
                    print("\n✓ ENDING: Patience was rewarded.")

            else:
                print("\nThe creature pokes you curiously. Eventually it leads you to safety.")
                print("\n✓ ENDING: Standing perfectly still worked out just fine.")

        else:
            print("\nYou hesitate, unsure what to do. Smoke grows thicker.")
            print("You push outside and find crewmate Chen signaling from a ridge.")
            print("Chen already fixed the radio. All good.")
            print("\n✓ ENDING: Sometimes the right move is just to go outside.")

    # ═══════════════════════════════════════════════
    # BRANCH B: RADIO
    # ═══════════════════════════════════════════════
    elif choice1 == "radio":
        print("\nYou grab the radio. It sparks — damaged, but fixable.")
        print("You need replacement components.")

        # Level 2
        choice2 = input("\nDo you search the COCKPIT or the CARGO bay for parts? ").strip().lower()

        if choice2 == "cockpit":
            print("\nThe cockpit is a mess, but the parts are here.")
            print("Then you notice a faint hiss — a gas leak from a cracked fuel line.")

            # Level 3 — THREE CHOICES
            choice3 = input("\nDo you FIX the radio quickly, VENTILATE the cockpit first, or IGNORE the leak? ").strip().lower()

            if choice3 == "fix":
                print("\nYou work fast. Radio fixed, distress call broadcast —")
                print("but you inhale too much gas and your vision blurs.")

                # Level 4
                choice4 = input("\nDo you CRAWL toward the exit or WAIT inside for rescue? ").strip().lower()

                if choice4 == "crawl":
                    print("\nYou crawl out into fresh air. Rescue receives your signal.")
                    print("They find you outside, groggy but alive.")
                    print("\n✓ ENDING: Rescued. Another ten minutes in there would have been bad.")

                elif choice4 == "wait":
                    print("\nYou stay. Rescue arrives and finds you in the cockpit.")
                    print("The gas wasn't lethal — just disorienting. You recover quickly.")
                    print("\n✓ ENDING: Rescued from your own cockpit. Slightly embarrassing, mostly fine.")

                else:
                    print("\nYou do neither and sit on the floor humming.")
                    print("The gas apparently made you very calm. Rescue finds you serenely unbothered.")
                    print("\n✓ ENDING: Rescued. The crew will never let you forget this.")

            elif choice3 == "ventilate":
                print("\nSmart move. You kick open the vents, wait for the air to clear,")
                print("then calmly fix the radio and broadcast your coordinates.")
                print("\n✓ BEST ENDING: Rescue arrives in 36 hours. Textbook survival. No drama.")

            elif choice3 == "ignore":
                print("\nYou try to work fast. Gas builds up and your vision swims.")

                # Level 4
                choice4 = input("\nParts almost in hand — do you PUSH THROUGH or CRAWL OUT? ").strip().lower()

                if choice4 == "push" or choice4 == "push through":
                    print("\nYou snag the parts and stumble out gasping.")
                    print("You fix the radio on the ground in fresh air. Signal sent.")
                    print("\n✓ ENDING: Stubborn but alive.")

                elif choice4 == "crawl" or choice4 == "crawl out":
                    print("\nGood instinct. You exit, fix the radio in fresh air.")
                    print("Clean signal. Fast rescue.")
                    print("\n✓ ENDING: Rescued in 24 hours.")

                else:
                    print("\nYou stand there coughing. The ship's emergency ventilation kicks in on its own.")
                    print("You fix the radio. Rescue called.")
                    print("\n✓ ENDING: The ship saved you from your own indecision.")

            else:
                print("\nNone of those felt right. You back out and find the parts in the nav console instead.")
                print("Radio fixed, signal sent.")
                print("\n✓ ENDING: The unconventional path still works.")

        elif choice2 == "cargo":
            print("\nIn the cargo bay: the parts you need — and a cluster of large, faintly glowing eggs.")
            print("You definitely didn't load these.")

            # Level 3 — THREE CHOICES
            choice3 = input("\nDo you LEAVE them alone, MOVE them outside carefully, or EXAMINE one up close? ").strip().lower()

            if choice3 == "leave":
                print("\nNone of your business. You grab the parts, fix the radio, send the signal.")
                print("\n✓ ENDING: Rescued. You still wonder what was in those eggs.")

            elif choice3 == "move":
                print("\nYou carry the eggs carefully outside into a sheltered spot.")
                print("As you set the last one down, a large alien lands nearby.")
                print("It looks at you, then the eggs, then back at you.")

                # Level 4
                choice4 = input("\nDo you RUN back to the ship, or WAIT and see what it does? ").strip().lower()

                if choice4 == "run":
                    print("\nYou bolt. The alien doesn't follow — it tends to the eggs.")
                    print("You fix the radio and send your coordinates. Rescue arrives.")
                    print("\n✓ ENDING: You did a good thing for those eggs.")

                elif choice4 == "wait":
                    print("\nThe alien regards you for a long moment.")
                    print("Then it digs up a glowing crystal and offers it to you.")
                    print("The crystal is a power source. It revives your ship's systems completely.")
                    print("\n✓ BEST ENDING: One good deed. Extraordinary reward.")

                else:
                    print("\nYou stand frozen. A second alien lands. They communicate,")
                    print("then both bow their heads toward you and place a crystal at your feet.")
                    print("Power restored. Rescue called.")
                    print("\n✓ ENDING: Standing still was, somehow, exactly right.")

            elif choice3 == "examine":
                print("\nYou lean in. A crack appears. A tiny four-eyed face peers out at you.")
                print("It chirps. You chirp back. It blinks. It imprints on you immediately.")

                # Level 4
                choice4 = input("\nDo you KEEP the hatchling close or LEAVE it and get to work? ").strip().lower()

                if choice4 == "keep":
                    print("\nThe hatchling leads you straight to its tribe's settlement,")
                    print("which has a long-range communication tower.")
                    print("You broadcast from there. Rescue is fast.")
                    print("\n✓ BEST ENDING: Rescued in hours. You also have an alien that considers you its parent.")

                elif choice4 == "leave":
                    print("\nYou put it back gently — it follows you anyway and sits on your shoulder.")
                    print("Honestly, the company is nice.")
                    print("Radio fixed. Signal sent.")
                    print("\n✓ ENDING: Rescued. The hatchling returned to its tribe. Probably.")

                else:
                    print("\nYou can't decide. The hatchling climbs onto your head and leads you")
                    print("directly to the ship's emergency beacon you had forgotten about.")
                    print("Signal activated. Rescue incoming.")
                    print("\n✓ ENDING: Rescued by a baby alien you had no idea what to do with.")

            else:
                print("\nYou step back carefully and take just the parts. Radio fixed. Signal sent.")
                print("\n✓ ENDING: Minimum drama. Maximum efficiency.")

        else:
            print("\nYou find a backup transmitter in the maintenance bay. Works without any repairs.")
            print("Signal sent immediately.")
            print("\n✓ ENDING: Sometimes it really is that easy.")

    # ═══════════════════════════════════════════════
    # BRANCH C: WEAPON
    # ═══════════════════════════════════════════════
    elif choice1 == "weapon":
        print("\nYou grab the plasma pistol. One charge remaining — use it wisely.")
        print("Outside, three paths stretch before you:")
        print("A dense JUNGLE to the east, a vast DESERT to the south,")
        print("and the peaks of a MOUNTAIN range to the west.")

        # Level 2 — THREE CHOICES
        choice2 = input("\nWhich way do you go? JUNGLE, DESERT, or MOUNTAINS? ").strip().lower()

        if choice2 == "jungle":
            print("\nVegetation closes in around you. You find water — good.")
            print("But the ship has disappeared behind a wall of green.")

            # Level 3 — THREE CHOICES
            choice3 = input("\nDo you CLIMB a tree to get your bearings, FOLLOW the water upstream,\nor FIRE your weapon as a signal? ").strip().lower()

            if choice3 == "climb":
                print("\nFrom the top you can see everything: your ship, an alien settlement,")
                print("and a rescue beacon two miles east.")

                # Level 4 — THREE CHOICES
                choice4 = input("\nDo you head to the SHIP, the SETTLEMENT, or the BEACON? ").strip().lower()

                if choice4 == "ship":
                    print("\nYou navigate back and fix the radio with parts found en route.")
                    print("\n✓ ENDING: Rescued from the ship. Classic move.")

                elif choice4 == "settlement":
                    print("\nFriendly aliens with a long-range communicator. Rescue in hours.")
                    print("You also get a tour of the settlement.")
                    print("\n✓ BEST ENDING: Fastest rescue. Best view.")

                elif choice4 == "beacon":
                    print("\nYour crewmate Chen activated it an hour ago.")
                    print("You were not the only survivor. Everyone made it.")
                    print("\n✓ BEST ENDING: The beacon was already working. All crew safe.")

                else:
                    print("\nYou can't decide, climb back down, and head to the beacon.")
                    print("It was already active. All crew safe.")
                    print("\n✓ ENDING: Indecision costs time, not lives.")

            elif choice3 == "follow":
                print("\nThe water leads uphill — unusual. After an hour, you emerge")
                print("into a clearing with an alien settlement.")

                # Level 4
                choice4 = input("\nDo you APPROACH openly, or OBSERVE from the treeline first? ").strip().lower()

                if choice4 == "approach":
                    print("\nYou walk in with hands raised. A crowd gathers.")
                    print("A leader steps forward and bows. You bow back. They help you signal for rescue.")
                    print("\n✓ ENDING: First contact made. You bowed at exactly the right moment.")

                elif choice4 == "observe":
                    print("\nFrom the treeline you spot what looks like a long-range transmitter.")

                    # Level 5
                    choice5 = input("\nDo you SNEAK in to use it, or WAIT and hope someone spots you? ").strip().lower()

                    if choice5 == "sneak":
                        print("\nYou slip in at night and access the transmitter.")
                        print("An alien taps you on the shoulder mid-broadcast.")
                        print("It was not sneaky at all. But they're friendly. They had seen you for hours.")
                        print("\n✓ ENDING: Stealth rating: 2/10. Luck rating: 10/10.")

                    elif choice5 == "wait":
                        print("\nAn alien child spots you and runs to get the adults.")
                        print("They emerge laughing — they'd been watching you from the start.")
                        print("They help you immediately.")
                        print("\n✓ ENDING: You were never as hidden as you thought.")

                    else:
                        print("\nYou just wave from the treeline. An alien waves back, then walks over.")
                        print("The simplest option was there all along.")
                        print("\n✓ ENDING: Rescued. Don't overthink it.")

                else:
                    print("\nYou walk in. Friendly settlement. Fast rescue.")
                    print("\n✓ ENDING: Rescued.")

            elif choice3 == "fire":
                print("\nYou fire the plasma pistol into the sky. One bright burst.")
                print("Three ships converge on your position within an hour.")
                print("One is your rescue team. The other two are very confused alien pilots.")
                print("\n✓ ENDING: Rescued. Also triggered a minor interstellar traffic incident.")

            else:
                print("\nNone of those. You wander until you find a path back to the ship.")
                print("The radio is still there. You fix it. Rescue comes.")
                print("\n✓ ENDING: Rescued the long way.")

        elif choice2 == "desert":
            print("\nHeat is immediate and intense. But the terrain is open — you can see far.")
            print("In the distance: the shimmering silhouette of what look like ancient ruins.")

            # Level 3 — THREE CHOICES
            choice3 = input("\nDo you ENTER the ruins, SEARCH around their base, or CLIMB to the top? ").strip().lower()

            if choice3 == "enter":
                print("\nThe ruins open into an intact alien structure. Not ruins — a base.")
                print("Dormant but functional.")

                # Level 4
                choice4 = input("\nDo you POWER it up, or SEARCH for a manual communication terminal? ").strip().lower()

                if choice4 == "power":
                    print("\nThe main power core activates. Everything lights up.")
                    print("An alien AI greets you in 40 languages — including English.")
                    print("It calls a rescue ship. You wait in a very comfortable alien waiting room.")
                    print("\n✓ BEST ENDING: Most comfortable rescue in history.")

                elif choice4 == "search":
                    print("\nYou find a terminal and broadcast on the universal emergency frequency.")
                    print("Rescued in 12 hours. The base mystery remains unsolved.")
                    print("\n✓ ENDING: Rescued. You have a lot of questions for the mission debrief.")

                else:
                    print("\nYou explore instead. The base has food, water, and shelter.")
                    print("You activate a distress beacon by accident while looking around.")
                    print("\n✓ ENDING: Rescued accidentally. Best kind.")

            elif choice3 == "search":
                print("\nAround the base: a shaded water source, emergency rations,")
                print("and a signal flare — still functional after who knows how long.")

                # Level 4
                choice4 = input("\nDo you USE the flare now, or CONSERVE it for when a ship passes? ").strip().lower()

                if choice4 == "use":
                    print("\nYou fire it immediately. A patrol ship overhead spots it.")
                    print("It wasn't looking for you, but it turns around.")
                    print("\n✓ ENDING: Right place, right time, right flare.")

                elif choice4 == "conserve":
                    print("\nThat night, a ship passes. You fire. They see you.")
                    print("\n✓ ENDING: Patience paid off. Rescued at nightfall.")

                else:
                    print("\nYou hold it. A ship passes overhead. You fire. They see you.")
                    print("\n✓ ENDING: Rescued.")

            elif choice3 == "climb":
                print("\nFrom the top, you see your crash site — and crewmate Chen")
                print("waving from beside it, clearly unharmed.")
                print("You make your way back. Chen already fixed the beacon.")
                print("You just had to find each other.")
                print("\n✓ BEST ENDING: Crew reunited. Rescue already called. You just had to show up.")

            else:
                print("\nYou rest in the shadow of the ruins. A search drone finds you an hour later.")
                print("\n✓ ENDING: The ship was looking for you. You just had to stay put.")

        elif choice2 == "mountains":
            print("\nYou climb toward the peaks. The air thins but the view is extraordinary.")
            print("Below, you spot lights — civilization of some kind.")

            # Level 3
            choice3 = input("\nDo you HEAD toward the lights, or STAY on high ground to be visible? ").strip().lower()

            if choice3 == "head":
                print("\nYou descend carefully toward the lights.")

                # Level 4
                choice4 = input("\nYou reach a large facility. Do you APPROACH the entrance\nor LOOK for another way in? ").strip().lower()

                if choice4 == "approach":
                    print("\nYou walk to the main entrance. A human in a jump suit opens the door.")
                    print("'We've been watching you on sensors since you crashed.'")
                    print("There's been a human mining colony on this planet for six years.")
                    print("Nobody in the mission briefing thought to mention it.")
                    print("\n✓ BEST ENDING: Rescued by humans. Space bureaucracy strikes again.")

                elif choice4 == "look":
                    print("\nYou find a service entrance. Inside: humans, equipment, and coffee.")
                    print("They've been trying to reach your ship since you crashed.")
                    print("\n✓ ENDING: Rescued by the back door. Just as good.")

                else:
                    print("\nYou walk in the front. Humans. Coffee. Rescued.")
                    print("\n✓ ENDING: The most straightforward ending on an alien planet.")

            elif choice3 == "stay":
                print("\nYou stay on the ridge and fire your last shot as a signal beacon.")
                print("The beam cuts across the sky. Something below spots it.")

                # Level 4
                choice4 = input("\nA vehicle approaches. Do you WAVE IT DOWN or TAKE COVER just in case? ").strip().lower()

                if choice4 == "wave":
                    print("\nIt's a human rover from the mining colony.")
                    print("'Nice shot,' the driver says. 'We saw that from 30 miles out.'")
                    print("\n✓ ENDING: Rescued. Your last charge was worth it.")

                elif choice4 == "cover" or choice4 == "take cover":
                    print("\nYou hide. The rover stops. 'Hello? We saw the signal!'")
                    print("You emerge, slightly embarrassed.")
                    print("\n✓ ENDING: Rescued by your own rescue. Awkward but effective.")

                else:
                    print("\nYou wave and duck simultaneously. The driver is baffled but still rescues you.")
                    print("\n✓ ENDING: Rescued. Confusedly.")

            else:
                print("\nYou head toward the lights. Human colony. You're home.")
                print("\n✓ ENDING: Rescued.")

        else:
            print("\nThat's not one of the paths. You stand at the wreckage, confused.")
            print("Then you spot Chen in the tree line, waving. You weren't alone after all.")
            print("\n✓ ENDING: Crew reunited. Chen had the radio the whole time.")

    # ═══════════════════════════════════════════════
    # HIDDEN BRANCH D: WAIT
    # ═══════════════════════════════════════════════
    elif choice1 == "wait":
        print("\nYou don't grab anything. You just... wait.")
        print("Smoke drifts. Something creaks in the hull.")
        print("And then — a panel near your head slides open.")
        print("Crewmate Chen is on the other side, completely unharmed.")
        print("\n'I've been trying to get this open for ten minutes,' Chen says.")
        print("'Also I already called for rescue. We're good.'")
        print("\n✓ SECRET ENDING: The best survival skill is knowing when to do nothing.")

    # ═══════════════════════════════════════════════
    # INVALID INPUT
    # ═══════════════════════════════════════════════
    else:
        print("\nThat item isn't there. In your confusion you knock over the medkit and grab it.")
        print("At least you're patched up. You step outside and find crewmate Chen")
        print("already working on the emergency beacon.")
        print("\n✓ ENDING: Rescued. Start time: immediately.")

    print("\n" + "=" * 55)


# ─── MAIN LOOP ────────────────────────────────────────────────
print("=" * 55)
while True:
    play_game()
    again = input("\nWould you like to play again? (YES or NO) ").strip().lower()
    if again != "yes":
        print("\nThanks for playing The Last Signal. Safe travels, Commander.")
        print("=" * 55)
        break
    print("\n" + "=" * 55)
