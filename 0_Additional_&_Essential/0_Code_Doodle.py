class NPC:
    def __init__(self, name, age, health):
        self._name = name
        self._age = age
        self._health = health
    def get_damage(self, damage):
        self._health -= damage
        print(f"{self._name} get damage!")
        print(f"{self._health} Left")

class Vendor(NPC):
    def __init__(self, name, age, health, town):
        super().__init__(name, age, health) 
        self._town = town
    
    def display_info(self):
        print(f"Name:{self._name}")
        print(f"Age:{self._age}")
        print(f"Health:{self._health}")
        print(f"Town:{self._town}")

class Militia(NPC):
    def __init__(self, name, age, health, town, type):
        super().__init__(name, age, health) 
        self._town = town
        self._type = type
    
    def display_info(self):
        print(f"Name:{self._name}")
        print(f"Age:{self._age}")
        print(f"Health:{self._health}")
        print(f"Town:{self._town}")
        print(f"Type:{self._type}")

obj1 = Vendor('Rosy', 32, 80, 'HoneyWood')
obj2 = Militia('James', 35, 120, 'HoneyWood', 'TownGuard')

obj2.get_damage(30)