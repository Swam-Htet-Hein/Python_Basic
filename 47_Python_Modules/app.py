import my_module as mm
# import my_module ဆိုရင် my_module ကို လိုက်ရေးနေရမှာ မလိုချင်ဘူးဆိုရင် keyword 'as' ကို သုံးပြီး ကိုယ်ပေးချင်တဲ့ name ပေးလိုက်ရုံပဲ။

students = ['Swam', 'Aung', 'SuSu', 'Kyaw']

print(mm.test)
print(mm.find_index(students, 'SuSu'))

# Module ထဲမှာမှ အတိအကျ function or variable ကို လိုချင်ရင်
from my_module import find_index
print(find_index(students, 'Aung'))

# function or variable ကို short_name ပေးချင်လည်းတယ်။
from my_module import find_index as fi
print(fi(students, 'Kyaw'))

# my_module ကို လည်းမရေးချင်ဘူး၊ function or variable ကို လည်းမသတ်မှတ်ထားချင်ဘူး၊ my_module ထဲက function or variable တွေကို ယူသုံးချင်ရင် '*' သုံး။
from my_module import *
print(find_index(students, 'Swam'))