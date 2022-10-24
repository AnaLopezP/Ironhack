
# Soldier


class Soldier:
    
    def __init__(self, health, strength):
        
        self.health = int(health)
        self.strength = int(strength)
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        
        self.health = int(self.health) - int(damage)

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    #metodos
    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health == 0:
            return str(self.name) + " has died in act of combat"
        else:
            return str(self.name) + " has received " + str(damage) + " points of damage"
    
    def battleCry(self):
        return "Odin Owns You All!"
    

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health == 0:
            return "A Saxon has died in combat"
        else:
            return "A Saxon has received " + str(damage) + " points of damage"
# War


class War:
    def __init__(self, vikingArmy = [], saxonArmy = []):
        self.vikingArmy = vikingArmy
        self.saxonArmy = saxonArmy

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        Saxon.receiveDamage(self, Viking.attack(self))
        if Soldier.receiveDamage(self) == 0:
            self.saxonArmy.pop()
        return Saxon.receiveDamage(self, Viking.attack(self))

    def saxonAttack(self):
        Viking.receiveDamage(self, Saxon.attack(self))
        if Soldier.health == 0:
            self.saxonArmy.pop()
        return Viking.receiveDamage(self, Saxon.attack(self))

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."