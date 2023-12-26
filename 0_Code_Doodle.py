class employee:
    def __init__(self) -> None:
        pass

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
emp1 = employee()
emp1.set_name('Moriko')
print(emp1.get_name())