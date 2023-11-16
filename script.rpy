# The script of the game goes in this file.


# Declare characters used by this game. The color argument colorizes the
# name of the character.
#1920 x 1080

define w = Character("Will", color="#43e312")
define a = Character("Andrew", color="#d62811")
define b = Character("Ben", color="#115dd6")
define olg = Character ("One-legged Goose")
define cmg = Character ("Chemically-mutated Goose")
define n = Character("",what_color="#03fcc6")

python early:
    wpHolder = fighter('Will','w', 100)
    apHolder = fighter('Andrew','a',100)
    bpHolder = fighter('Ben','b',100)

    foe1 = fighter("One-legged Goose",'olg', 75)
    foe2 = fighter('Chemically-mutated Goose','cmg', 100)


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

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    #​image imageScale = im.Scale("orange lab.jpg", 70, 100) #adjust as required for you resolution
 
    scene orange lab2

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    #n "You've created a new Ren'Py game."

    n "Choose your character"
    
    $charChoice = renpy.display_menu([ ('Will',1),('Andrew',2),('Ben',3) ])
    if charChoice == 1:
        $player = wpHolder
        $boss = apHolder
        define m = w
        define e = a
    elif charChoice == 2:
        $player = apHolder
        $boss = bpHolder
        define m = a
        define e = b
    else:
        $player = bpHolder
        $boss = wpHolder
        define m = b
        define e = w
        


    $foe2 = fighter('Chemically-mutated Goose','cmg', 100)
    
    #$player = fighter('Will','w', 100)
    $evilAndrew = fighter('Andrew','a', 100)
    #$player = fighter('Ben','b', 100)

    python:
        #When a fighter dies, it restarts the combat cycle if the player is the one that died (akd if combatCycle == False)
        
        
        outcome = combatCycle(foe2)
        if outcome:
            m("I won")
        else:
            cmg("QUACK")


    n "Combat over"


    # This ends the game.

    return
