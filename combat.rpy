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
        def atkList(self,atkNum):
            if self.nickname == 'w':
                if atkNum == 1:
                    dmg = 12
                    return ["Killer Groove",dmg]
                elif atkNum == 2:
                    dmg = 32
                    return ["Drum Beating",dmg]
                else:
                    return ["AbMaj7(b9,#13)",50]
            elif self.nickname == 'a':
                if atkNum == 1:
                    return ["Punch",8]
                elif atkNum == 2:
                    return ["PV=NRT",45]
                else:
                    return ["Span(B)",60]
            elif self.nickname == 'b':
                if atkNum == 1:
                    return ["Sharp Cheddar",30]
                elif atkNum == 2:
                    return ["Gouda Gun",20]
                else:
                    return ["Brie Bomb",50]
            elif self.nickname == 'cmg':
                if atkNum == 1:
                    return ["Sonic Honk",2]
                elif atkNum == 2:
                    return ["Acid Breath",22]
                else:
                    return ["Triple Kick",222]
        
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
        n((player.name + " Verses the " + foe.name))
        foe.heal()
        player.heal()
        playerAlive = True
        while True:
            n("Choose an attack:")
            choice = renpy.display_menu([ (player.atkList(1)[0],1),(player.atkList(2)[0],2),(player.atkList(3)[0],3) ])
            n((player.name+ " uses " + player.atkList(choice)[0]))
            n((player.name+" deals "+str(player.atkList(choice)[1])+" damage" ))
            foe.takeDmg(player.atkList(choice)[1])
            if foe.health <= 0:
                break
            n((foe.name+" is at "+str(foe.health)+" health"))
             
            rand = random.randint(1,3)
            n((foe.name+" uses "+fighter.atkList(foe,rand)[0]))
            n((foe.name+" deals "+str(fighter.atkList(foe,rand)[1])+" damage"))
            player.takeDmg(fighter.atkList(foe,rand)[1])
            if player.health <= 0:
                playerAlive = False
                break
                
            n((player.name+" is at "+str(player.health)+" health"))
        
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
       