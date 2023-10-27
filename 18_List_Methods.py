# List သည် class တစ်ခုဖြစ်သည်။
names = ['Swam', 'Swam', 'Aung', 'Myat', 'Sithu', 'Lwin']
# names သည် list class ရဲ့ object တစ်ခုဖြစ်သည်။
# object တွင် behaviors, methods တွေရှိသည်။

"""
    List methods
    - append()
    - pop()
    - count()
    - extend()
    - insert()
    - remove()
    - index()
    - copy()
    - clear()
    - sort()
    - reverse()
"""

# append()
# append() သည် names object ထဲ့သို့ object value အသစ်တစ်ခုပေါင်းထည့်ပေးသည်။
names.append('Kyaw') # append() သည် value return မပြန်သော method ဖြစ်သည်။
print(names)
names.append('SuSu')
print(names)
# ['Swam', 'Swam', 'Aung', 'Myat', 'Sithu', 'Lwin', 'Kyaw', 'SuSu']

# pop() 
# pop() သည် append() ရဲ့ ပြောင်းပြန်ဖြစ်ပြီး၊ names object ထဲ့မှ object value ကို ဖျက်ပေးသည်။
names.pop() # () ထဲဘာမှမရေးပေးလျှင်နောက်ဆုံးကဟာကို ဖျက်သည်။
print(names)
# ['Swam', 'Swam', 'Aung', 'Myat', 'Sithu', 'Lwin', 'Kyaw']

deleted_name = names.pop() # pop() သည် value process လုပ်ပေးရုံသာမက value return ပါပြန်ပေးသည်။
print(f'Deleted name : {deleted_name}')
print(f'Names : {names}')
# ['Swam', 'Swam', 'Aung', 'Myat', 'Sithu', 'Lwin']

deleted_name = names.pop(2) # pop() သည် ဘာမှမထည့်ရင် default နောက်ဆုံးဖျက်ပြီ၊ ထည့်ရင်တော့ index အတိုင်းဖျက်တယ်။
print(f'Deleted name : {deleted_name}')
print(f'Names : {names}')
# ['Swam', 'Swam', 'Myat', 'Sithu', 'Lwin']

# count()
# count() သည် string ထဲ့မှာလည်းသုံးသည်။
# list မှာလည်း list ထဲ့ကဘယ် items တွေက ဘယ်နှခုတူညီနေလဲ ဆိုတဲ့ int value ကို return ပြန်ပေးတယ်။
Swam_time = names.count('Swam') # list ထဲ့မှာ Swam ဆိုတဲ့ နာမည်ဘယ်နှခုပါနေလဲဆိုတာ ‌ရေတွက်ပြီး return ပြန်တယ်။
print(Swam_time) # 2

# extend()
# extend() သည် list တစ်ခုထဲမှ items တွေကို တစ်ခြား list ထဲကို ပေါင်းထည့်ပေးလိုက်ခြင်းဖြစ်သည်။
new_name = ['Kyaw Thu', 'Min Min', 'Thu Thu']
names.extend(new_name)
print(names) # ပေါင်းထည့်လိုက်သော items တွေသည် names ရဲ့ items အသစ်တွေဖြစ်လာတယ်။
# ['Swam', 'Swam', 'Myat', 'Sithu', 'Lwin', 'Kyaw Thu', 'Min Min', 'Thu Thu']
# အကယ်၍ append() ကို သုံးပြီးပေါင်းထည့်မယ်ဆိုရင် list တစ်ခုကို အခြား list တစ်ခုထဲ ပေါင်းထည့်လိုက်သလိုပဲဖြစ်မှာပါ။
# Nested list ဖြစ်သွားမှာပါ။
# new_name = ['Kyaw Thu', 'Min Min', 'Thu Thu']
# names.append(new_name)
# print(names) ==> ['Swam', 'Swam', 'Myat', 'Sithu', 'Lwin', ['Kyaw Thu', 'Min Min', 'Thu Thu']]