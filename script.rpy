#The Battle of the Waterloo Region
#William Comay, Andrew Robinet, and Benjamin Cheung (21073761)

define w = Character("Will", color="#43e312")
define a = Character("Andrew", color="#d62811")
define b = Character("Ben", color="#115dd6")
define olg = Character ("One-legged Goose")
define cmg = Character ("Chemically-mutated Goose")
define tlg = character ('Three-Legged Goose')
define n = Character("",what_color="#03fcc6")

python early:
    wpHolder = fighter('Will','w', 100)
    apHolder = fighter('Andrew','a',100)
    bpHolder = fighter('Ben','b',100)

    foe1 = fighter("One-legged Goose",'olg', 75)
    foe2 = fighter('Three-Legged Goose','tlg',100)
    foe3 = fighter('Chemically-mutated Goose','cmg', 100)


$ uChoice = 1

if uChoice == 1:
    define m = Character("Will", color="#43e312")
    $ p = w

elif uChoice == 2:
    define m = Character("Andrew", color="#d62811")
    $ p = a
else:
    define m = Character("Ben", color="#115dd6")
    $ p = b



# The game starts here.

label start:
 
    scene outside dc #BC This sets the background of the game to outside the Davis Centre 

    #BC The next 30 lines of code are the prologue of the actual game
    #BC It sets up the conflict and background of the story
    n"Since 1957, a war has been raging in the region of Waterloo."

    n "First-year students eager to attend the University of Waterloo in which they were admitted, 
    were only expecting to go to classes, study, and potentially hang out with their friends if they could find the time… "

    n "but that’s not all they found…"

    n "Walking down a path to their classes, expecting peace…"

    n"but finding war. "

    show ptyler1 #BC shows a goose, matching up with the text being printed on the screen

    #BC still the prologue text screens
    n"GEESE."

    n"The Canadian Goose. "

    n"Branta canadensis, in scientific terms. "

    n"To everyone else, they are just another bird with a black head, white cheeks, and a grey-brown body."

    n"But to UW students, they could strike at any moment."

    n"Waiting…on the fields…on the paths…for their next victim. Why do they attack? Why are they so aggressive? So many questions gone unanswered."

    n"Luckily, there are those will no longer let these geese persist, do whatever they want."

    n"There are those who want fight back."

    n"Will you fight back?"

    n "This is..."

    hide ptyler1 #BC this hides the goose image in order to put up a different image

    show titlecard #BC this puts the titlecard "Battle of the Waterloo Region" onto screen, symbolizing the start of the actual game

    n"" #BC an empty screen that splits up the title card from the choose your character screen

    hide titlecard #BC removes the titlecard from the screen

    n "Choose your character." #BC prompts the user to pick a character
    
    $charChoice = renpy.display_menu([ ('Will',1),('Andrew',2),('Ben',3) ])
    if charChoice == 1:
        $player = wpHolder
        $boss = apHolder
        $m = w
        $e = a
        n"An excellent decision." #BC if the user chooses Will, this text will pop up
        m"With the power of music, those geese won’t know what’s coming for them." #BC if the user chooses Will, this dialogue will pop up
    elif charChoice == 2:
        $player = apHolder
        $boss = bpHolder
        $m = a
        $e = b
        n"An excellent decision." #BC if the user chooses Andrew, this text will pop up
        m"With the power of engineering, those geese won’t know what’s coming for them." #BC if the user chooses Andrew, this dialogue will pop up
    else:
        $player = bpHolder
        $boss = wpHolder
        $m = b
        $e = w
        n"An excellent decision." #BC if the user chooses Ben, this text will pop up
        m"With the power of cheese, those geese won’t know what’s coming for them." #BC if the user chooses Ben, this dialogue will pop up
        


    #$foe2 = fighter('Chemically-mutated Goose','cmg', 100)
    


    #BC This will be the text before the Tutorial battle against the One-legged Goose

    scene e2 #BC changes the scene to outside E2 as the player is going to their first programming lab

    #BC the story before the first battle 
    n"It’s the first day of classes and it is time for your first programming lab!"

    n"On the way to the lab, you see something odd."

    n"A goose…"

    n"A goose…but with only one leg."

    show ptyler1 #BC the image of the One-legged goose appears

    n"The one-legged goose looks at you, as if it knows you are on the opposing side of the battle."

    n"I guess this is the perfect opportunity for you to learn how to fight…"

    n"I guess this is the perfect opportunity for you to learn how to fight… against a…"

    n"I guess this is the perfect opportunity for you to learn how to fight… against a… not too difficult opponent…"

    #The battle begins
    python:
        #When a fighter dies, it restarts the combat cycle if the player is the one that died (akd if combatCycle == False)
        
        outcome = combatCycle(foe1)
        if outcome:
            #BC if the player wins the battle, this dialogue will be used
            m("The first battle victory of many more to come! Even if it was just against a one-legged goose…")
        else:
            #BC if the player loses the battle, this dialogue will be used
            m("Well, it could be worse. I could have lost against a zero-legged goose…")

    n"Combat over." #BC let's the player know that the battle sequence has concluded 

    hide ptyler1 #BC since the battle is over, the image of the goose can disappear


    #BC This will be the text before the fight with the Three-legged day

    scene main path #BC the scene changes to the main path outside RCH

    #BC this is the dialogue before the second battle
    n"Finally! A free day in your busy schedule."

    n"No assignments, no labs, no tutorials, and no classes."

    n"You can finally…"

    n"You can finally…relax…?"

    n"You hear a scream."

    n"A fellow student is yelling for help!"

    n"You rush over as quickly as possible."

    n"You are confused by what you see."

    n"It was odd for a goose to have one leg, but it is logical that it just lost it in an accident."

    n"Why does this one have three legs?!"

    show ptyler1 #BC the image of the Three-legged goose appears

    n"You conclude that it is probably just a one in a million genetic mutation."

    n"Those are always possible…not likely…but possible."

    n"To protect your fellow student, there is no other option but to fight."

    #The battle begins
    python:
        #When a fighter dies, it restarts the combat cycle if the player is the one that died (akd if combatCycle == False)
        
        outcome = combatCycle(foe2)
        if outcome:
            #BC if the player wins the battle, this dialogue will be used
            m("No one attacks a UW student unwarranted even if it is a three-legged goose! BUT WHY DOES IT HAVE THREE LEGS?")
        else:
            #BC if the player loses the battle, this dialogue will be used
            m("A normal goose is bad enough, but one with three legs…come on…")

    n"Combat over." #BC let's the player know that the battle sequence has concluded 

    hide ptyler1 #BC since the battle is over, the image of the goose can disappear


    #BC This will be the text before the fight with the Chemically-mutated Goose

    scene e7 #BC the scene changes to E7 at the Ideas Clinic

    #BC this is the dialogue before the third battle
    n"After making soap through the process of saponification, it is time to clean up the clinic. "

    n"*cling* "

    n"Wait. What was that sound?"

    n"*cling* *clang*"

    n"It’s coming from that mysterious box in the corner..."

    n"You slowly approach the box, when suddenly, a goose springs out of the box, but it’s no normal goose."

    show ptyler1 #BC the image of the Chemically-mutated Goose appears

    n"This goose has mutated and looks like it has been chemically modified!"

    n"What is going on?!"

    n"I guess you have no choice but to engage in battle with this mysterious mutant chemical goose…"

    #The battle begins
    python:
        #When a fighter dies, it restarts the combat cycle if the player is the one that died (akd if combatCycle == False)
        
        outcome = combatCycle(foe3)
        if outcome:
            #BC if the player wins the battle, this dialogue will be used
            m("Good thing this chemically modified goose didn’t bring any extremely toxic chemicals to this battle…")
        else:
            #BC if the player loses the battle, this dialogue will be used
            cmg("HONK!")
            m("I should have brought neutralizer. And maybe some PPE…")


    n "Combat over." #BC let's the player know that the battle sequence has concluded 

    hide ptyler1 #BC since the battle is over, the image of the goose can disappear


    #BC This will be the text before the fight with One of us

    scene rch #BC the scene changes to RCH where the final battle takes place

    #BC dialogue before the final battle
    #BC the character 'e' will have the dialogue of one of the starter characters depending on the character chosen at the beginning of the game
    m"First it was a one-legged goose, then a three-legged goose, and then whatever the last goose was."

    m"Some strange chemically modified mutant goose..."

    m"There must be something else happening here."

    m"Wait..."

    m"Wait... chemically modified..."

    m"Wait... chemically modified... it's not possible..."

    m"Wait... chemically modified... it's not possible... is it?"

    e"Yes. It is possible."

    #BC depending on which character the player is, one of the other characters will appear
    if m == a:
        show andrew pose #BC if Andrew was chosen, Ben will appear as the final boss
    elif m == b:
        show andrew pose #BC if Ben was chosen, Will will appear as the final boss
    else:
        show andrew pose #BC if Will was chosen, Andrew will appear as the final boss

    #BC dialogue before the final battle
    n"" #BC this line adds dramatic effect as no dialogue shows up until the player clicks

    m"No, it cannot be."

    e"It was me..."

    e"I have been chemically engineering the geese to fight against UW students."

    m"But... why?"

    e"Ever since I failed my first exam back in 1957 when the university first came into being, I needed a way to take my revenge, and to prove my abilities in chemical engineering."

    m"But you’re a first-year and can’t possibly be that old…"

    e"The geese aren’t the only thing that I chemically modified."

    m"So, we have been fighting the geese the entire time although they are just innocent birds being manipulated… manipulated by you"

    m"I will not allow these geese to be acted cruelly on again."

    m"This eternal revenge plan of yours ends here. This will be the final Battle of the Waterloo Region..."

    m"This eternal revenge plan of yours ends here. This will be the final Battle of the Waterloo Region... FOR THE GEESE!!"

    #The battle begins
    python:
        #When a fighter dies, it restarts the combat cycle if the player is the one that died (akd if combatCycle == False)
        
        outcome = combatCycle(boss)
        if outcome:
            #BC if the player wins the battle, this dialogue will be used
            m("Your reign of chemical terror is over.")
            m("The geese will no longer be chemically modified, and UW students will no longer be terrorized by those chemically modified geese.")
            m("It’s time for you to move on from university…I mean it has been decades after all…")
            e("I never thought that anyone would thwart my plans. But you may be right, it may be time for me to retire at the ripe ol’ age of 18.")
            m("You’re not 18. You’ve been here since 1957.")
            e("Right…")

        else:
            #BC if the player loses the battle, this dialogue will be used
            e("You really thought some random first-year chemical engineering student could beat me? HA HA HA.")

    n "Combat over." #BC let's the player know that the battle sequence has concluded 

    #BC since the battle is over, the image of one of us can disappear
    #BC depending on which character the player is, one of the other characters will disappear
    if m == a:
        hide andrew pose #BC if Andrew was chosen, Ben will disappear 
    elif m == b:
        hide andrew pose #BC if Ben was chosen, Will will disappear 
    else:
        hide andrew pose #BC if Will was chosen, Andrew will disappear 


    #BC Epilogue starts here

    scene outside dc #BC scene changes back to the beginning of the game 

    #BC the epilogue dialogue of the game, describing life after the battles
    n"After the final Battle of the Waterloo Region, life was peaceful."
    n"The geese went back to minding their own business on the fields, classes continued as if nothing every happened."
    n"And the UW students went back to worrying about their first mid-terms…"
    n"Let’s just hope none of them fail. Or that could mean the start of another…"

    show titlecard #BC the title card appears

    n"" #BC adds dramatic effect before showing the final screen

    hide titlecard #BC removes title card for dramatic effect

    n"The End." #BC last text screen to appear symbolizing the end of the game

    # This ends the game.

    return
