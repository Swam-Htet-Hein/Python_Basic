"""
Python မှာ အရာအားလုံးကို Object တွေလို့သတ်မှတ်လို့ရတယ်။

    Object မှာ နှစ်မျိုးရှိတယ်။
    1. Static (Object နဲ့ဆိုင်တဲ့ အချက်အလက်တွေ (နာမည်၊ model...))
    2. Behavior (Object တစ်ခုကလုပ်နိုင်တဲ့အရာ(သို့)အပြုအမှုရှိတဲ့အရာ)
Class
    Class ကို design (or) blueprint တွေလို့ခေါ်လို့ရတယ်။
    ကားတစ်စီး တည်ဆောက်တဲ့အခါမှ အရင်ဆုံးကားနဲ့ ဆိုင်တဲ့ blueprint(or)design ရေးဆွဲရတယ်။
    ပြီးမှ အဲဒီ blueprint ပေါ်မှာအခြေခံပြီး ကားအစီးရေ ကြိုက်သလောက်ထပ်ထုတ်လို့ရတယ်။
    Programming မှာလည်း အဲဒီအတိုင်းပဲ ကိုယ်ဖြစ်ချင်တဲ့အရာအတွက် class ကိုကြိုရေးဆွဲထားရင် အဲဒီ class ကို သုံးပြီး တူညီသော Objectတွေဖြစ်စေ၊ မတူညီသော Objectတွေဖြစ်စေ ကြိုက်သလောက်ဖန်တီး သုံးဆွဲလို့ရတယ်။
"""
class car:
    # constructor (special method)
    def __init__(self, color, brand) -> None:
        self.color = color # self.color သည် car class ရဲ့ color variable ကို ရိုးရိုးcolor ကနေလာတဲ့ data တွေနဲ့ assign လုပ်လိုက်ခြင်းဖြစ်သည်။
        # အဲ့လို assign လုပ်လိုက်ခြင်းဖြင့် color variable ကို class အတွင်းမှာအသုံးပြုလို့ရသွားတယ်။
        self.brand = brand

car_1 = car('White', 'Toyota')
print(car_1.color)
print(car_1.brand)