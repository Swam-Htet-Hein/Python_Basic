class employee:
    def __init__(self, age) -> None:
        self.age = age

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    def __str__(self) -> str:
        return f"I am {self.name}"
    
    def __len__(self):
        return self.age
    
    def __eq__(self, others) -> bool:
        if self.name == others.name and self.age == others.age:
            return True
        else:
            return False
emp1 = employee(24)
emp2 = employee(24)
emp1.set_name('Moriko')
emp2.set_name('Moriko')
print(emp1 == emp2)