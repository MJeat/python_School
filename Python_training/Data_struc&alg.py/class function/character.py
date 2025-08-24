# Class is like a blueprint of creating objects.

class Character:
    def __init__(self, name: str, health:int, damage:int) -> None: # put all things that u need for ur character inside the parameters.
        self.name = name                                            # The "->" means that this function will output None. If '-> int' means that this function will output intergers.
        self.health= health
        self.health_max = health
        self.damage = damage        #these things are like something that all the characters in the game have. 
                                    #It is something that we must need it for the objects or the game to function


    def attack(self, target) -> None:
        target.health -= self.damage # '-=' means to subtract
        target.health = max(target.health, 0 )





