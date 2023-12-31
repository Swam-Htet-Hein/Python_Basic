# Module ဆိုတာ Python file တစ်ခုပဲ
# ဒါပေမဲ့ အသင့်ရေးထားတဲ့ Python file ဖြစ်တယ်။
# ဒီလို အသင့်ရေးထားတဲ့ Python file ကို ယူသုံးချင်ရင် import keyword ကို သုံးရတယ်။
import test_module

# greet, year and temperature သည် test_module.py ထဲမှာ ရေးထားတဲ့ code တွေဖြစ်ပြီး
# လက်ရှိ .py မှာ ယူသုံးနေတာဖြစ်တယ်။
print(test_module.greet)
print(test_module.year)
print(test_module.temperature)

# from - import ကိုသုံးပြီး ကိုယ်ထုတ်သုံးချင်တဲ့ variable ကို တိုက်ရိုက်ထည့်ထားလို့ရတယ်။
from test_module import greet, year, temperature 
print(greet)
print(year)
print(temperature)

# Modules သည် module folder တစ်ခုဖြစ်ပြီး test သည် module file(python file) ဖြစ်သည်။
from Modules import test
print(test.name)
print(test.age)

# random module
import random

# randint()
# random integer တန်ဖိုးကို return ပြန်ပေးတယ်။
# randint(1, 5) သည် ၁ ကနေ ၅ အတွင်းမှာရှိတဲ့ နံပတ်တွေကို ကျပန်းထုတ်ပေးတယ်။
num = random.randint(1, 5)
print(num)

# choice()
# choice() သည် ကိုယ်ရွှေးချယ်လိုက်တဲ့ ဟာထဲ့မှ ကျပန်းပြန်ထုတ်ပေးတယ်။
name = ['Swam', 'Htet', 'Kyaw', 'Myat', 'Thiha', 'SuSu']
choice_name = random.choice(name)
print(choice_name)