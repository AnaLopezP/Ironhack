
# Soldier


class Soldier:
    
    def __init__(self, health, strength):
        
        self.health = int(health)
        self.strength = int(strength)
    
    def attack(self):
        
        return int(self.strength)
    
    def receiveDamage(self, damage):
        
        self.health = int(self.health) - int(damage)

# Viking


class Viking(Soldier):
    def __init__(self, health, strength, name):
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
        return "Odin owns you all!!"
    

# Saxon


class Saxon:
    pass

# War


class War:
    pass