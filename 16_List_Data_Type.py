# Static Type Programming
# Static type programming သည် variable တစ်ခု assign မလုပ်ခင်ကတည်းက value data type ကို ကြေညာပေးရတယ်။
# In C++, int age = 21;, string name = "Swam";
# Pros, Data type အတည်တကျသတ်မှတ်ထားတဲ့ အတွက် data type ကြောင့်ဖြစ်တတ်တဲ့ error တွေကို လျော့ချနိုင်တယ်။
# Cons, Data type တွေကို တစ်ခုချင်းစီ ကြေညာနေရတာဖြစ်တဲ့ အတွက် အချိန်ကြာတယ်။

# Dynamic Type Programming
# Dynamic type programming သည် data type ကြေညာပေးဖို့မလိုပဲ တိုက်ရိုက်တန်ဖိုး ထည့်လို့ရသည်။
# In Python, age = 21, name = 'Swam'
# Pros, Data type တွေလိုက်ကြေညာနေဖို့ မလိုအပ်တာကြောင်း အချိန်ကုန်သက်သာတယ်။
# Cons, Type casting လုပ်တဲ့ အခါတို့၊ data type ကြောင်းဖြစ်တတ်တဲ့ error တွေတော့ရှိတယ်။

# Data structure
# Data structure is way of storing and organizing data according to certain format of structure
# Python built-in data types are list / dictionary / tuple / set

# List
# list သည် data တွေကို စုစည်းပေးထားသော container တစ်လုံးဖြစ်သည်။like a array in other programming language
# - commonly used
# - allowed different data type in one container
# - can use square bracket
# - List has the ordered structure
# - Nested list and marge

name = ['Swam', 'Kyaw', 'Myat', 'Shwe']
#           0       1       2       3
print(name)
print(name[0])
print(name[3])
print(name[0:2]) # index slicing

Random = [45, 5.5, 'HH', True, "Guys", 0, -34] # list သည် data type ချင်းမတူတဲ့ ဟာကိုတောင် store ပေးသည်။
print(Random)

# mutable သည် index number နဲ့ value တွေကို assign လုပ်လို့ရတဲ့ data type အမျိုးအစားကို ဆိုလိုတယ်။
# mutable ==> list

# inmutable သည် index number နဲ့ value တွေကို assign လုပ်လို့မရတဲ့ data type အမျိုးအစားကို ဆိုလိုတယ်။
# inmutable ==> string(str)
# name = 'Swam'
# name[0] = 'htet'
# print(name[0]) TypeError: 'str' object does not support item assignment

# mutable
students = ['Swam', 'Hein', 'Pyae', 'Soe']
print(students)
print(type(students))
print(len(students))
students[1] = 'Kyaw'
print(students)
students[2] = 'ThuThu'
print(students)