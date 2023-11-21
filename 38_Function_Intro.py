# Function ဆိုတာ လုပ်ဆောင်ချက်တစ်ခုပဲ။
# အစာစားတယ်ဆိုတာ function တစ်ခုလို့ သတ်မှတ်ကြည့်မယ်။
# အရင်ဆုံး ပန်ကန်ပြားတစ်ချက်ကိုယူမယ်၊ ထမင်းထည့်မယ်၊ ဟင်းထည့်မယ်၊ ပြီးရင်စားမယ်။
# ဒီအဆင့်တွေကို နောက်ထပ်တစ်ကြိမ် ထပ်လုပ်ချင်ရင် အစာစားတယ်ဆိုတဲ့ function ကို ခေါ်သုံးလိုက်ရုံပဲ။

# Functions
# Built-in Functions
# User-defined Functions

# keyword(def) function_name() : implementation
def Greeting():
    print("Hello world", end=' ')
    print("This is Python")

Greeting() # return မပြန်တဲ့အတွက်ကြောင့် တန်ဖိုး အစားသွင်းလိုမရပါဘူး။ not a = Greeting()
Greeting()
Greeting()

# return ပြန်တဲ့ function 
def add():
    a = 3
    b = 4
    return a + b

print(add()) # add() သည် အခု return ပြန်တဲ့ function ဖြစ်သွားတဲ့ အတွက်တန်ဖိုးအစားသွင်းတာတွေလုပ်လို့ရသွားပြီ
added = add()
print(added)