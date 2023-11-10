# Data Structure Conversion
# int, float, bool, str တန်ဖိုးတွေကို type conversion လုပ်ပြီးပြောင်းလဲလို့ရသလို။
# list, tuple, set, dict တန်ဖိုးတွေကို လည်း type conversion လုပ်ပြီးပြောင်းလဲလို့ရတယ်။
# list(), tuple(), set(), dict() တွေသည် constructor များဖြစ်သည်။
# ၄င်းတို့ကိုသုံးပြီး data structure conversion လုပ်လို့ရသည်။

# Tuple to List
tup1 = (1,2,3,4,5)
print(f'Original tup : {tup1}')
print(type(tup1))
tup_to_list = list(tup1)
print(f'Converted tup to list : {tup_to_list}')
print(type(tup_to_list))

# Set to List
Set1 = {1,2,3,4,5}
print(f'Original set : {Set1}')
print(type(Set1))
set_to_list = list(Set1)
print(f'Converted set to list : {set_to_list}')
print(type(set_to_list))

# Dict to List
Dict1 = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five'
}
print(f'Original Dictionary : {Dict1}')
print(type(Dict1))
# dict_to_list = list(Dict1)
# dict_to_list ဆိုပြီးရိုးရိုးပဲ သုံးရင် Dictionary ရဲ့ key တန်ဖိုးကို ပဲယူပြီး list ထဲထည့်မှာပါ။
dict_to_list = list(Dict1.items()) # items() ကိုသုံးလိုက်ရင် list ထဲမှာ tuple data type နဲ့ key, value ကို ထည့်ပေးမှာပါ။
print(f'Converted dict to list : {dict_to_list}')
print(type(dict_to_list))

# Dictionary to Set
# Set သည် unordered data structure ဖြစ်တဲ့အတွက် dict ထဲမှာ key သည် ဖြစ်ချင်တာဖြစ်မယ်။
dict1 = {
    1: 'one',
    2: 'two',
    3: 'three'
}
dict_to_set = set(dict1.items())
print(dict_to_set)

# List, tuple, Set to Dictionary
# Dict သည် key, value pair တွေကိုပဲ လက်ခံတဲ့ data type ဖြစ်တယ်။
# ဒါကြောင့် item တစ်ခုတည့်ပဲရှိတဲ့ list, tuple, set တွေကို Nested လုပ်ပြီး dict ကို convert လုပ်လို့ရတယ်။
listA = [[1,'one'], [2, 'two'], [3, 'three']]
print(f'Original List : {listA}')
list_to_dict = dict(listA)
print(f'Converted list to dict : {list_to_dict}')
# list တင်မှ မဟုတ်ဘူး တစ်ခြား tuple, set တွေဆိုရင် လည်း nested လုပ်ပြီးမှ dict ကို convert လုပ်လိုရတယ်။