#  File: RPG.py
#  Description:RPG GAME
#  Student's Name: Tyree Pearson
#  Student's UT EID: Tsp627
#  Course Name: CS 313E 
#  Unique Number: 86940
#
#  Date Created: 6/13/2017
#  Date Last Modified:6/15/2017


class RPGCharacter():

    
    def __init__(self):
        pass


    def show(self):
        print(self.name)
        print("\tCurrent Health:" ,self.health ,"\n"
                +"\tCurrent Spell Points:", self.spellPoints,"\n"
                +"\tWielding:", self.weapon ,"\n"
                +"\tWearing:" , self.armor ,"\n"
                +"\tArmor Class:",self.armor.armorClass,"\n")
                

    def __str__(self):
        return self
            
    #OBTAIN YOUR WEAPON
    def wield(self,weapon):
        if weapon.weaponType in self.allowedWeapon:
            print(self.name, ' is now wielding a(n) ', weapon.weaponType)
            self.weapon = weapon
        else:
            print('Weapon not allowed for this class')

    #UNWIELD YOUR WEAPON
    def unwield(self,weapon):
        if weapon.weaponType in self.allowedWeapon:
            print(self.name, ' is no longer wielding anything')
            self.weapon = weapon
        else:
            return
        

    #OBTAIN YOUR ARMOR 
    def putOnArmor(self,armor):
        
        if armor.armorType in self.allowedArmor:
            print(self.name,' is now wearing', armor.armorType)
            self.armor = armor
        else:
            print("Armor not allowed for this character class")

                    
    #TAKE OFF YOUR ARMOR
    def takeOffArmor(self,armor):
        self.noArmor = armor
        if armor.armorType in self.allowedArmor:
            print(self.name, ' is now wearing nothing')
            self.armor = armor
        else:
            return

    #FIGHT YOUR OPPONENT
    def fight(self, opponent):

            #DETERMINE WHOS FIGHTING
            print(self.name,"attacks",opponent.name,"with",self.weapon)
            opponent.health -= self.weapon.damage

            print(self.name,"does",self.weapon.damage,"to", opponent.name)
            print(opponent.name, "is now down to", opponent.health, "health")
            opponent.checkForDefeat()

    def checkForDefeat(self):
    
        if self.health <=0:
            print(self.name,"has been defeated!")
    
        


class Fighter(RPGCharacter):

    def __init__(self, name):
        self.name = name
        self.weapon = Weapon('none')
        self.armor = Armor('none')
        self.health = 40
        self.maxHealth = 40
        self.spellPoints = 0
        self.allowedWeapon = ['dagger', 'axe', 'staff', 'sword','none']
        self.allowedArmor = ['plate','chain','leather','none']

    def __str__ (self):
        return self


class Wizard(RPGCharacter):
    
    
    def __init__(self,name):
        self.name = name
        self.weapon = Weapon('none')
        self.armor = Armor('none')        
        self.health = 16
        self.maxHealth = 16
        self.spellPoints = 20
        self.allowedWeapon = ['staff','dagger','none']
        self.allowedArmor = ['none']

    def castSpell(self, spell, target):
        # check if spell exists
        spells = ["Fireball", "Lightning Bolt", "Heal"]
        if spell in spells:
                print(self.name, "casts", spell, "at", target.name)
        else:
                print("Unknown spell name. Spell failed.")
                return
        # FIREBALL
        if(spell == "Fireball"):
                cost = 3                
                if(-cost > self.spellPoints):
                        print("Insufficient spell points")
                        return
                
                self.spellPoints -= cost
                target.health -= 5
                
                print(self.name, "does", 5, "damage to", target.name)
                print(target.name, "is now down to", target.health, "health")
                target.checkForDefeat()
                
        # LIGHTNING BOLT
        elif(spell == "Lightning Bolt"):
                cost = 10                
                if(-cost > self.spellPoints):
                        print("Insufficient spell points")
                        return
                
                self.spellPoints -= cost
                target.health -= 10
                
                print(self.name, "does", 10, "damage to", target.name)
                print(target.name, "is now down to", target.health, "health")
                target.checkForDefeat()
        
        # HEAL
        elif(spell == "Heal"):
                # spell cost
                cost = 6
                effect = 6
                
                if(cost > self.spellPoints):
                    print("Insufficient spell points")
                    return                
                healthDif = target.maxHealth - target.health
                if(healthDif < effect):
                        effect = healthDif
                
                self.spellPoints -= cost
                target.health += effect
                        
                print(self.name, "heals", target.name, "for", effect, "health points.")
                print(target.name, "is now at", target.health, "health")                               
                                                
    def __str__(self):
        return self


class Weapon():

    def __init__ (self,weaponType):
        self.weaponType = weaponType
        self.damage = self.damageType()

    def damageType(self):
        weaponType = self.weaponType
        if weaponType == "dagger":
            return 4
        elif weaponType == "axe" or weaponType == "staff":
            return 6
        elif weaponType == "sword":
            return 10
        elif weaponType == "none":
            return 1
        else:
            return

    def __str__(self):
        return self.weaponType
        

class Armor(RPGCharacter):
    
    
    def __init__(self,armorType):
        self.armorType = armorType
        self.armorClass = self.armorProtection()
        
    def armorProtection(self):
        armorType = self.armorType
        
        if self.armorType == "chain":
            return 2 
        elif self.armorType == "plate":
            return 5 
        elif armorType == "leather":
            return 8
        elif armorType == "none":
            return 10

    def __str__ (self):
        return self.armorType
    

def main():

    chainMail = Armor("chain")
    sword = Weapon("sword")
    staff = Weapon("staff")
    axe = Weapon("axe")

    harry = Wizard("Harry Potter")
    harry.wield(staff)
    
    aragorn = Fighter("Aragorn")
    aragorn.putOnArmor(chainMail)
    aragorn.wield(axe)
    
    harry.show()
    aragorn.show()

    harry.castSpell("Fireball",aragorn)
    aragorn.fight(harry)

    harry.show()
    aragorn.show()

    harry.castSpell("Lightning Bolt",aragorn)
    aragorn.wield(sword)

    harry.show()
    aragorn.show()

    harry.castSpell("Heal",harry)
    aragorn.fight(harry)

    harry.fight(aragorn)
    aragorn.fight(harry)

    harry.show()
    aragorn.show()


main()
