class person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    def display_info(self):
        print(f"Name:{self._name}|Age:{self._age}")

class employee(person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self._emp_id = employee_id
    def display_info(self):
        super().display_info()
        print(f"Employee ID:{self._emp_id}")

class manager(employee):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age, employee_id)
        self._department = department
    def display_info(self):
        super().display_info()
        print(f"Department:{self._department}")

obj1 = manager('Swam', 21, 'a004', 'Finance')
obj1.display_info()