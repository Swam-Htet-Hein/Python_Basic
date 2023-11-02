# Set Data-type
# immutable
# unordered

empty_set = set()
print(type(empty_set))
print(empty_set)

# set is unordered ဒါကြောင့် result က ထွက်ချင်တဲ့ items ကထွက်မယ်။
_set = set(('apple', 'orange', 'banana'))
print(_set) # {'orange', 'apple', 'banana'}

_set = {'apple', 'orange', 'banana'} # set ကိုဒီလိုလည်း ကြေညာလို့ရတယ်။
print(_set) # {'apple', 'banana', 'orange'}

# set သည် items တွေ duplicate(တူညီ) လို့ မရပါဘူး
_set = {1, 3, 4, 1, 5, 4, 6, 1}
# duplicate ဖြစ်နေလျှင် ဖြစ်နေတဲ့ item ကို တစ်ခုတည်း ယူပြီး ထုတ်ပြပေးမှာဖြစ်တယ်။
print(_set) # {1, 3, 4, 5, 6}

# list ကို set() ထဲယူသုံးခြင်း
my_list = ['coffee', 'milk', 'sugar', 'tea', 'milk', 'sugar', 'cup', 'coffee']
set_list = set(my_list)
print(set_list) # {'cup', 'tea', 'coffee', 'milk', 'sugar'}