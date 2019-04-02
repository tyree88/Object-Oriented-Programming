
#  File: RPG.py
#  Description: Use python classes to create a simple Role Playing Game
#  Student's Name: Charles Lybrand
#  Student's UT EID: cbl652
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: 02/04/17
#  Date Last Modified: 02/04/17



####################     Character Classes     ####################



class RPGCharacter:
    '''
    Creates a character with all the actions available for all characters
    '''
    
    def __init__(self):
        pass
    
    # actions all characters can use
    
    # wield a weapon
    def wield(self, weapon):
        # check if the weapon can be wielded by this character
        if weapon.weaponType in self.weaponTypes:
            print(self.name, "is now wielding a(n)", weapon.weaponType)
            # make this the characters new weapon
            self.weapon = weapon
        # warning message to say that character can't wield weapon
        else:
            print("Weapon not allowed for this character class.")

    # drop weapon
    def unwield(self):
        print(self.name, "is no longer wielding anything.")
        # make current weapon "none"
        self.weapon = Weapon("none")
        
    # put on armor
    def putOnArmor(self, armor):
        # check if the armor can be worn by this character
        if armor.armorType in self.armorTypes:
            print(self.name, "is now wearing", armor.armorType)
            # make this the characters armor
            self.armor = armor
        # warning message to say that character can't put on this armor
        else:
            print("Armor not allowed for this character class.")
            
    # take off armor
    def takeOffArmor(self):
        print(self.name, "is no longer wearing anything.")
        # make current armor "none"
        self.armor = Armor("none")
        
    # fight another character
    def fight(self, opponent):
        # print who is attacking who
        print(self.name, "attacks", opponent.name, "with a(n)", self.weapon.weaponType)
        # deduct damage from opponent
        opponent.health -= self.weapon.damage
        # print the result
        print(self.name, "does", self.weapon.damage, "damage to", opponent.name)
        print(opponent.name, "is now down to", opponent.health, "health")
        opponent.checkForDefeat()
        
    # show the current state of the character
    def show(self):
        # print the following information
        print()
        print(" %s" % self.name)
        print("   Current Health: %d" % self.health)
        print("   Current Spell Points: %d" % self.spellPoints)
        print("   Wielding: %s" % self.weapon.weaponType)
        print("   Wearing: %s" % self.armor.armorType)
        print("   Armor class: %d" % self.armor.armorClass)
        print()
        
    # check if the character has been defeated
    def checkForDefeat(self):
        # if the player's life is 0 or less, print that he/she has been defeated
        if (self.health <= 0):
            print(self.name, "has been defeated!")



class Fighter(RPGCharacter):
	'''
	Create a Fighter character
	'''
	
	# class variables
	maxHealth = 40
	maxSpellPoints = 0
	weaponTypes = ["dagger", "axe", "staff", "sword", "none"]
	armorTypes = ["plate", "chain", "leather", "none"]
	
	# initialize Fighter
	def __init__(self, name):
		self.name = name
		self.health = Fighter.maxHealth
		self.spellPoints = Fighter.maxSpellPoints
		self.weapon = Weapon("none")
		self.armor = Armor("none")



class Wizard(RPGCharacter):
	'''
	Create a Wizard character
	'''

	# class variables
	maxHealth = 16
	maxSpellPoints = 20
	weaponTypes = ["dagger", "staff", "none"]
	armorTypes = ["none"]
	
	# initialize Wizard
	def __init__(self, name):
		self.name = name
		self.health = Wizard.maxHealth
		self.spellPoints = Wizard.maxSpellPoints
		self.weapon = Weapon("none")
		self.armor = Armor("none")
		
	# cast a spell on a character
	def castSpell(self, spell, target):
		# check if spell exists
		if(spell in ["Fireball", "Lightning Bolt", "Heal"]):
			print(self.name, "casts", spell, "at", target.name)
		else:
			print("Unknown spell name. Spell failed.")
			return
		
		# for each spell, subtract the cost of spell points,
		# and subtract/add health points to target
		
		# FIREBALL
		if(spell == "Fireball"):
			# spell cost
			cost = -3
			effect = -5
			
			# if character doesn't have enough spell points, don't preform spell
			if(-cost > self.spellPoints):
				print("Insufficient spell points")
				return
			
			# deductions/additions
			self.spellPoints += cost
			target.health += effect
			
			# print the results
			print(self.name, "does", -effect, "damage to", target.name)
			print(target.name, "is now down to", target.health, "health")
			target.checkForDefeat()
			
		# LIGHTNING BOLT
		elif(spell == "Lightning Bolt"):
			# spell cost
			cost = -10
			effect = -10
			
			# if character doesn't have enough spell points, don't preform spell
			if(-cost > self.spellPoints):
				print("Insufficient spell points")
				return
			
			# deductions/additions
			self.spellPoints += cost
			target.health += effect
			
			# print the results
			print(self.name, "does", -effect, "damage to", target.name)
			print(target.name, "is now down to", target.health, "health")
			target.checkForDefeat()
		
		# HEAL
		elif(spell == "Heal"):
			# spell cost
			cost = -6
			effect = 6
			
			# if character doesn't have enough spell points, don't preform spell
			if(-cost > self.spellPoints):
				print("Insufficient spell points")
				return
			
			# make sure that character doesn't heal more than target's max health
			healthDif = target.maxHealth - target.health
			if(healthDif < effect):
				effect = healthDif
			
			# deductions/additions
			self.spellPoints += cost
			target.health += effect
				
			print(self.name, "heals", target.name, "for", effect, "health points.")
			print(target.name, "is now at", target.health, "health")
			


####################     Character Classes     ####################



class Weapon:
	
	def __init__(self, weaponType):
		self.weaponType = weaponType
		self.damage = self.damageFromType()
		
	def damageFromType(self):
		'''
		Return the amount of damage the given weapon type can do
		'''
		weaponType = self.weaponType
		if(weaponType == "dagger"):
			return 4
		elif(weaponType == "axe"):
			return 6
		elif(weaponType == "staff"):
			return 6
		elif(weaponType == "sword"):
			return 10
		elif(weaponType == "none"):
			return 1
		# if the weapon type is not recognized, assign it a value of 1 and print a message
		else:
			print("Weapon Type: " + str(weaponType) + " not found")
			return 1



class Armor:
	
	def __init__(self, armorType):
		self.armorType = armorType
		self.armorClass = self.armorFromType()
		
	def armorFromType(self):
		'''
		Return the amount of damage the given weapon type can do
		'''
		armorType = self.armorType
		if(armorType == "plate"):
			return 2
		elif(armorType == "chain"):
			return 5
		elif(armorType == "leather"):
			return 8
		elif(armorType == "none"):
			return 10
		# if the armor type is not recognized, assign it a value of 1 and print a message
		else:
			print("Armor Type: " + str(armorType) + " not found")
			return 1



####################     Start of Program     ####################



def main():
	'''
	Run a scenario of a fighter fighting a wizard
	'''

	chainMail = Armor("chain")
	sword = Weapon("sword")
	staff = Weapon("staff")
	axe = Weapon("axe")

	gandalf = Wizard("Gandalf the Grey")
	gandalf.wield(staff)
	
	aragorn = Fighter("Aragorn")
	aragorn.putOnArmor(chainMail)
	aragorn.wield(axe)
	
	gandalf.show()
	aragorn.show()

	gandalf.castSpell("Fireball",aragorn)
	aragorn.fight(gandalf)

	gandalf.show()
	aragorn.show()

	gandalf.castSpell("Lightning Bolt",aragorn)
	aragorn.wield(sword)

	gandalf.show()
	aragorn.show()

	gandalf.castSpell("Heal",gandalf)
	aragorn.fight(gandalf)

	gandalf.fight(aragorn)
	aragorn.fight(gandalf)

	gandalf.show()
	aragorn.show()



if __name__ == "__main__":
	main()

