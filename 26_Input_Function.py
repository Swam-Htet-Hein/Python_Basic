# Input function
# print function သည် user တွေဆီကို အချက်အလက်ထုတ်ပေးသလို
# input function သည် user တွေဆီမှ အချက်အလက်ကို ယူသည်။
# input function သည် return function ဖြစ်သည်။

user_input = input()
# input() သည် user တွေဆီမှ အချက်အလက်ကို ယူပြီး string အနေနဲ့ return ပြန်ပေးသည်။
print(f'You\'ve entered {user_input}')
print(type(user_input)) # return -> str

# input() ကတစ်ခုခုတော့တောင်းနေတာပဲ ဒါပေမဲ့ ဘာကိုတောင်းတာလဲဆိုတာကို မသိဘူး။
# အဲဒီတော့ prompt ကို သုံးပြီး code ရေးတဲ့ developer ကဘာတောင်းနေလဲဆိုတာ command ထဲမှာဖော်ပြထားလို့ရတယ်။
name = input('Enter your name: ')
print(f'Hello {name}, How are you?')

# Type conversion
# name, address တို့ ကို str အနေနဲ့ return ပြန်ပြီး တွက်ချက်မှုရင် ကိစ္စမရှိပေ မဲ့ age, temperature, numတို့ကို return ပြန်ပြီးတွက်ချက်မှုလုပ်ရင်တော့ ကိစ္စရှိလာပါပြီ
# input() သည် str အနေနဲ့ return ပြန်တဲ့ အတွက်ကြောင့်ပါ။
# ဒါဆိုရင် object တွေကို method သုံးပြီး ပြုပြင်ပြောင်းလဲသလိုပဲ
# Data-type တွေကို လဲ method တွေသုံးပြီး type conversion(typeပြောင်းလဲခြင်း) လုပ်လို့ရတယ်။
# int(), float(), str()
user_name = input('What\'s your name? : ')
user_age = int(input('How old are you? : '))
print(f'My name is {user_name}')
print(f'I am {user_age} years old')
print(type(user_name)) # <class 'str'>
print(type(user_age)) # <class 'int'>

