# Inheritance အမွေဆက်ခံခြင်း
# အမွေပေးမဲ့ class --> parent class or superclass
# အမွေဆက်ခံမဲ့ class --> child class or subclass
# object နှစ်မျိုးရှိတယ်။ (class object) (instance object)
class First_class:
    data = "Hello world"
    num = 99
    def set_data(self, data):
        self.data = data
    def get_data(self):
        return self.data
    def display(self):
        print(f"This is first class {self.data}")

# Second_class သည် First_class ထံမှ အမွေဆက်ခံထားသည်။
class Second_class(First_class):
    def test(self):
        print('testing...')

# Inheritance search
# class တွေဟာသူတို့ရဲ့ member တွေကိုရှာဖွေတဲ့အခါမှာ သူတို့ရဲ့အတွင်း(local)မှာအရင်ရှာတယ်။
# ရှာလို့မတွေ့ရင် superclass or parent class တွေမှာသွားရှာတယ်။
class Third_class(Second_class):
    # def display(self):
    #     print(f"This is third class {self.data}")
    pass

# class တစ်ခုကိုသုံးပြီး ဖန်တီးလိုက်တဲ့ object ကို (instance object) လို့ခေါ်တယ်။
first = First_class()
# print(first.data)
# print(first.get_data())
# first.test() parent class က child class ရဲ့ member တွေကိုတော့လှမ်းယူသုံးလို့မရဘူး။

# class ကို object အနေနဲ့မြင်ပြီး အသုံးချကြည့်မယ်။
# print(First_class.data)
# print(First_class.num)
# ဘယ် variable မှာမှ instance object အနေနဲ့သုံးမထားဘူး ဒီအတိုင်း class ကိုတိုက်ရိုက်အသုံးချထားတဲ့အတွက် ဒါကို (class object) လို့ခေါ်တယ်။

# child class က parent class ရဲ့ member တွေကို လှမ်းယူသုံးလို့ရတယ်။
# ဒါပေမဲ့ parent class က encapsulated လုပ်ထားတဲ့ member တွေကိုတော့ ယူသုံးလို့မရဘူး။
second = Second_class()
second.test()

third = Third_class()
third.display()
