#  File: RPG.py
#  Description:
#  Student's Name:
#  Student's UT EID:
#  Course Name: CS 313E 
#  Unique Number: XXXXX
#
#  Date Created:
#  Date Last Modified:


class RPGCharacter():
    def __init__(self):
        pass
    
    def __str__(self):
        return (" Current Health:" +self.health +"\n"
                +"Current Spell Points:"+ self.health+"\n"
                +"Wielding:"+ self.wield +"\n"
                +"Wearing:" + self.armor +"\n"
                +"Armor Class:"+ self.AC +"\n")


        
class Armor(RPGCharacter):

    def __init__(self,armorType):
        self.armorType = ""
        protection = 2

    def armor(self,chainMail):
        Fighter.putOnArmor('fighterArmor')
        
        


class Weapon(RPGCharacter):
    damage = 0
    staff = 6
    
    def __init__(self,weaponType):
        self.weaponType = ""

    def weapon(self,staff):        
        Wizard.wield('wzdWeapon')
        self.damge = 6

        Fighter.wield('fighterWeapon')
        self.damage = 6
    


        

class Wizard(RPGCharacter):
    
    health = 16
    spellPoints = 20
    def __init__(self,name):
        self.name = ""
        
    def wield(self,wzdWeapon):

       self.wzdWeapon = ""

    def show(self):
        print("Current Health:" ,self.health ,"\n"
                +"Current Spell Points:", self.spellPoints,"\n"
                +"Wielding:",self.wield ,"\n"
                +"Wearing:"+"none"+"\n"
                +"Armor Class:"+ "AC" +"\n")

    def show(self):
        return RPGCharacter.self()
        
        
class Fighter(RPGCharacter):
     health = 40
     def __init__ (self,name):
         self.name = ""

     def putOnArmor(self,fighterArmor):
         self.fighterArmor = ""
         

     def wield(self,fighterWeapon):

         self.fighterWeapon = ""
         

     def show(self):
            print("Current Health:" ,self.health ,"\n",
            +"Current Spell Points:",0,"\n",
            +"Wielding:",self.wield ,"\n",
            +"Wearing:",self.putOnArmor,"\n",
            +"Armor Class:"+ "AC" +"\n")

            

        
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
    '''
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
    '''

main()
