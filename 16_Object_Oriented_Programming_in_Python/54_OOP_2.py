# name = 'SWam'
class employee:
    def __init__(self, job_type, name, age, address) -> None:
        self.type = job_type
        self.name = name
        self.age = age
        self.address = address
    def Self_intro(self, fav_color):
        # fav_color သည် Self_intro အတွင်း local variable ဖြစ်တဲ့အတွက် self. ထည့်စရာမလိုပဲ တိုက်ရိုက်ရေးလို့ရတယ်။
        print(f"Hello, My name is {self.name}.")
        print(f"I am {self.age} years old and I'm from {self.address}.")
        print(f"I'll work here as a {self.type}.")
        print(f"And Personally, I love {fav_color} color.")

Emp_1 = employee("Web Developer", "Maung Kyaw", 28, "Yangon")
Emp_1.Self_intro("Blue")