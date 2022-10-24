
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
        Saxon.receiveDamage(self, Viking.strength)
        if Saxon.health == 0:
            self.saxonArmy.pop(Saxon)