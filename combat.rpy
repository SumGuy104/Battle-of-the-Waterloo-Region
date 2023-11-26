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
        

        def atkList(self,atkNum, recoil=0):
            if self.nickname == 'w':
                if atkNum == 1:
                    dmg = random.randint(15,50)
                    return ["Killer Groove",dmg,1]
                elif atkNum == 2:
                    hitnumber = random.randint(1,5)
                    dmg = random.randint(10,15)
                    return ["Drum Beating",dmg,hitnumber]
                else:
                    return ["AbMaj7(b9,#13)",32,1]
            elif self.nickname == 'a':
                if atkNum == 1:
                    chance = random.randint(1,1000)
                    dmg = 0
                    if chance <= 272:   
                        dmg = foe.health
                    return ["Euler's Punch",dmg,1]
                    
                elif atkNum == 2:
                    return ["PV=NRT",35,1]
                else:
                    dmg = random.randint(25,46)
                    return ["Span(B)",dmg,1]
            elif self.nickname == 'b':
                if atkNum == 1:
                    if recoil == 3:
                        n("The blue cheese was actually just moldy cheddar")
                        n("Ben takes 25 damage")

                    return ["Blue Cheese",45,1]
                elif atkNum == 2:
                        hitnumb = random.randint(1,2)
                        dmg = random.randint(20,30)
                    return ["Gouda Gun",dmg,hitnumb]
                else:
                    dmg = random.randint(1,80)
                    return ["Brie Bomb",dmg,1]
            elif self.nickname == 'cmg':
                if atkNum == 1:
                    return ["Sonic Honk",2,1]
                elif atkNum == 2:
                    return ["Acid Breath",22,1]
                else:
                    return ["Triple Kick",222,1]
        
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
        n((player.name + " verses the " + foe.name + "."))
        foe.heal()
        player.heal()
        playerAlive = True
        while True:
            n("Choose an attack:")
            choice = renpy.display_menu([ (player.atkList(1)[0],1),(player.atkList(2)[0],2),(player.atkList(3)[0],3) ])
            n((player.name+ " uses " + player.atkList(choice)[0] + "."))

            for i in range((player.atkList(choice)[2])):
                n((player.name+" deals "+str(player.atkList(choice)[1])+" damage." ))
                foe.takeDmg(player.atkList(choice)[1])

            reco = random.randint(1,4)
            player.atkList(choice, reco)
            
            if foe.health <= 0:
                break
            n((foe.name+" is at "+str(foe.health)+" health."))
             
            rand = random.randint(1,3)
            n((foe.name+" uses "+fighter.atkList(foe,rand)[0]+ "."))
            n((foe.name+" deals "+str(fighter.atkList(foe,rand)[1])+" damage."))
            player.takeDmg(fighter.atkList(foe,rand)[1])
            if player.health <= 0:
                playerAlive = False
                break
                
            n((player.name+" is at "+str(player.health)+" health."))
        
        return playerAlive
        




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
            