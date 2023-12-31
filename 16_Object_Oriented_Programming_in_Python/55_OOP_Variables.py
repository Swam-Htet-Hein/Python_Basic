# Instance Variable
# Class Variable

# Object တစ်ခုတည်းနဲ့ဆိုင်တဲ့ variable သည် Instance variable ဖြစ်သည်။
# Object တွေအများကြီးနဲ့ဆိုင်တဲ့ variable သည် Class variable ဖြစ်သည်။

class animal:
    # Type_of_Place သည် animal class ရဲ့ object တွေအကုန်လုံးနဲ့ သက်ဆိုင်တဲ့အတွက် Class Variable တစ်ခုဖြစ်သည်။
    Type_of_Place = "Wild Life Plain in Africa"

    def __init__(self, type_of_animal, color, age) -> None:
        # type_of_animal, color and age သည် object တစ်ခုတည်းနဲ့ ဆိုင်ပြီး အစားသွင်းရသည်။
        # အဲဒီအတွက် ဒီ variable ကို Instance Varaible လို့‌ခေါ်သည်။
        self.type = type_of_animal
        self.color = color
        self.age = age
    def Explain(self, fav_food):
        print(f"It's a {self.type}.")
        print(f"Its color is {self.color}.")
        print(f"It's {self.age} years old.")
        print(f"Its favorite food is {fav_food}.")

animal_1 = animal("Tiger", "Yellow", 19)
animal_2 = animal("Lion", "Gold", 21)
animal_3 = animal("Elephant", "Gray", 30)

animal_1.Explain("Meat")
animal_2.Explain("Meat")
animal_3.Explain("Vegetable")

print(animal_1.Type_of_Place)
print(animal_2.Type_of_Place)
print(animal_3.Type_of_Place)