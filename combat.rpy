python early:
    import random

    #Profile for 'objects' that fight (Each of us and the geese)
    class fighter():

        #Defines the name, nickname for easy reference, current health, and full health for each fighter
        def __init__(self,name,nickname,health):
            self.name = name
            self.nickname = nickname
            self.health = health
            self.fullHealth = health

        def takeDmg(self,dealt):
            self.health -= dealt

        def heal(self):
            self.health = self.fullHealth

        '''
        Returns the attack (Name, damage) based on which fighter called this function (self)  and what attack number they want (atkNum)

        Andrew, you can add more code, like randomizers, under the if/elif for each attack. Save the damage in a variable, 
        and return that variable in the second element in the list (just like ive done with the dmg variable on the first 2 attacks)
        '''
        
        #AR,WC - This is the move table for all characters in the game
        def atkList(self,atkNum, recoil=0):
            if self.nickname == 'w': #WC - nickname check allows for each character the ability to only choose between the 3 moves assigned to them
                if atkNum == 1: #WC - Move check to see which move was input 
                    dmg = random.randint(15,50) #AR, WC - a dmg variable is set to a randomized number that is then called upon for the damage value of the move
                    return ["Killer Groove",dmg,1]#WC - order of list, name of move, damgage, number of times the move hits
                elif atkNum == 2:
                    hitnumber = random.randint(1,5)#AR, WC - The variable hitnumber is assigned to a random value between 1-5 and then called upon in the return statement
                    dmg = random.randint(10,15)
                    return ["Drum Beating",dmg,hitnumber]#AR, WC - the randomzied hitnumber will now take effect in the amount of times the move is used
                else:
                    return ["AbMaj7(b9,#13)",32,1]
            elif self.nickname == 'a':
                if atkNum == 1:
                    chance = random.randint(1,1000)#AR, WC - chance is randomized and then sent through a if statement check
                    dmg = 0
                    if chance <= 272: #AR, WC - if the check succeeds the attack will deal 6022 damage if not it will deal 0 damage
                        dmg = 6022
                    return ["Euler's Punch",dmg,1]
                    
                elif atkNum == 2:
                    return ["PV=NRT",35,1]
                else:
                    dmg = random.randint(25,46)
                    return ["Span(B)",dmg,1]
            elif self.nickname == 'b':
                if atkNum == 1:
                    if recoil == 3: #AR, WC - the value of recoil is a parameter that is randomized between 1-3
                        n("The blue cheese was actually just moldy cheddar")
                        n("Ben takes 25 damage")

                    return ["Blue Cheese",45,1]#AR, WC - if the recoil check is true the move will be altered to deal damge to ones self as well as the regular damage
                elif atkNum == 2:
                    hitnumb = random.randint(1,2)
                    dmg = random.randint(20,30)
                    return ["Gouda Gun",dmg,hitnumb]
                else:
                    dmg = random.randint(1,80)
                    return ["Brie Bomb",dmg,1]
            elif self.nickname == 'cmg':
                if atkNum == 1:
                    return ["Sonic Honk",25,1]
                elif atkNum == 2:
                    return ["Acid Breath",33,1]
                else:
                    return ["Radiation",40,1]
            elif self.nickname == olg:
                if atkNum == 1
                    return["Hop",1,1]
            elif self.nickname == tlg
                if atkNum == 1
                    dmg = random.randint(10,15)
                    return ["Triple Kick",dmg,3]
                elif atkNum == 2
                    return ["Shuffle Stomp",25,1]
                else:
                    return ["Body Check",30,1]
        
        #This is an old system of dealing with attacks and damage. Its simpler but much longer (and you know Im down-bad for efficiency)
        def atk(self,atkNum):
            if self.nickname == 'w':
                return wAttacks(atkNum)
            elif self.nickname == 'a':
                return aAttacks(atkNum)
            elif self.nickname == 'b':
                return bAttacks(atkNum)
            elif self.nickname == 'cmg':
                return cmgAttack()

    #All these functions are also part of the old attacking system
    def aAttack(x):
        if x == 1:  #Punch
            return 12
        elif x == 2:    #PV=NRT
            return 32
        else:   #Span(B)
            return 50 

    def bAttack(x):
        if x == 1:  #Sharp Cheddar
            return 45
        elif x == 2:    #Gouda Gun
            return 8
        else:   #Brie Bomb
            return 50 
    
    def wAttack(x):
        if x == 1:  #Killer Groove
            return 12
        elif x == 2:    #Drum Beating
            return 32
        else:   #AbMaj7(b9,#13)
            return 50 
    
    def cmgAttack(x):
        if x == 1:  #Sonic Honk
            return 2
        elif x == 2:    #Acid Breath
            return 22
        else:   #Tripple Kick
            return 222

    def combatCycle(foe):
        '''
        WC: This is the main cycle for all combat encouters
        It takes the object of the enemy as the argument
        The player chooses an attack, their fighter deals the damange from that attack to the foe
        The foe randomly picks and attack and deals the damage form that attack to the player's fighter
        The function returns true if the player won and false if they lost
        '''
        n((player.name + " verses the " + foe.name + ".")) #WC: Introduces the combat encounter

        #WC: Sets all fighters health to full before the attack
        foe.heal() 
        player.heal()

        #WC: The combat loops until the loop is broken (when a fighter dies)
        playerAlive = True
        while True:
            #WC: Uses the renpy menu function to prompt the user to choose an attack and saves the attack number in the 'choice' variable
            n("Choose an attack:")
            choice = renpy.display_menu([ (player.atkList(1)[0],1),(player.atkList(2)[0],2),(player.atkList(3)[0],3) ])
            n((player.name+ " uses " + player.atkList(choice)[0] + "."))

            #WC: For attacks that have the possiblility of hitting multiple times (fighter.atklist()[2] > 1) then a for loop is used to deal damage
            damage = player.atkList(choice)[1]
            loop = player.atkList(choice)[2]
            for i in range(loop):
                n((player.name+" deals "+str(damage)+" damage" + (" again"*i) + "." ))
                foe.takeDmg(damage) 

            #WC: If the attack cooresponding to the choice contains recoil code in 'atkList', this code passes it a random number from 1 to 3
            reco = random.randint(1,4)
            player.atkList(choice, reco) 
            
            #WC: If the foe has been reduced to 0 or healther or lower, the combat loop is broken out of, otherwise the foes current health is printed
            if foe.health <= 0:
                break
            n((foe.name+" is at "+str(foe.health)+" health."))
             
            #WC: A random attack number is generated from 1 to 3 and the cooresponding attack in the atkList is called and the damage is dealt to the player
            rand = random.randint(1,3)
            damage = fighter.atkList(foe,rand)[1]
            n((foe.name+" uses "+fighter.atkList(foe,rand)[0]+ "."))
            n((foe.name+" deals "+str(damage)+" damage."))
            player.takeDmg(damage)

            #WC: If the player has been redused to  of 0 health or lower, the playerAlive is set to false and the combat loop is broken, otherwise the players current health is printed
            if player.health <= 0:
                playerAlive = False
                break   
            n((player.name+" is at "+str(player.health)+" health."))
        
        return playerAlive #WC: Returns true if they player is still alive after the combat
        




    #$n("Choose an attack:")
    #choice = renpy.display_menu([(fighter.atkList(player,1),1),(fighter.atkList(player,2),2),(fighter.atkList(player,3),3)])
    '''$n((player.name+ " uses " + fighter.atkList(player,choice)))
    $n((player.name+" deals "+str(aAttack(choice))+" damage" ))
    $foe2.takeDmg(aAttack(choice))
    $n((foe2.name+" is at "+str(foe2.health)+" health"))

    $n((foe2.name+" uses "+fighter.atkList(foe2,1)))
    $n((foe2.name+" deals "+str(cmgAttack(1))+" damage"))
    $player.takeDmg(cmgAttack(1))
    $n((player.name+" is at "+str(player.health)+" health"))
    '''

    
            