class car:
    # __init__() သည် constructor တစ်ခုဖြစ်သည်။
    # constructor တစ်ခုတည်ဆောက်ပြီးပါက object တစ်ခု ဖန်တီးလျှင် constructor အတိုင်း object ကို arguments သွင်းရတယ်။
    # constructor သည် void data typeဖြစ်ရမည်။ ဆိုလိုသည်မှာ return မပြန်ရပါ။
    def __init__(self, name, color, model, price) -> None:
        self.name = name
        self.color = color
        self.model = model
        self.price = price
    
    # Function သည် self parameter သုံးစရာမလိုပဲ
    # Special Method သည် class နဲ့ဆိုင်တဲ့ အတွက် self parameter သုံးပေရမည်။
    def check_status(self):
        # self သည် ဒီ class ကို ပြန်ရည်ညွန်းသည်။
        print(self.name)
        print(self.color)
        print(self.model)
        print(self.price)

Car_1 = car("Tesla", "Grey", "EV001", "20000")
Car_1.check_status()

Car_2 = car("BMW", "White", "BMW001", "30000")
Car_2.check_status()