class NPC:
    def __init__(self, name, npc_type, health) -> None:
        self.name = name
        self.npc_type = npc_type
        self.health = health
    def NPC_status(self):
        print(f"Name : {self.name}")
        print(f"Type : {self.npc_type}")
        print(f"Health : {self.health}")
    def work(self, fav_job):
        print(f"I am {self.name} and I like {fav_job}")
    
peasant = NPC("Maria", "ShopKeeper", 30)
peasant.NPC_status()
peasant.work("Selling things")