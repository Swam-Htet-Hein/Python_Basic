# Tuple သည် list လိုပဲ မတူညီတဲ့ data type တွေကို စု့စည်းပြီး store ပေးတယ်။
# Tuple သည် လက်သည်းကွင်း() နဲ့ ရေးပေးရတယ်။

names = ('swam', 'htet', 23, 3.4, True)
print(names)
print(type(names))

# Tuple သည် ordered structure ဖြစ်သည်။
print(names[0])
print(names[2])

# Tuple index slicing
start = 0
end = 2+1
step = 1
print(names[start : end : step])

# Tuple packing
marks = 100, 80, 90, 70.5 # () ထည့်စရာမလိုဘဲနဲ့လည်း tuple create လုပ်လို့ရတယ်။
print(marks)
print(type(marks))

# Tuple unpacking
Swam_mark, Kyaw_mark, SuSu_mark, Myat_mark = marks
# ညာထဲမှာ ရှိတဲ့ တန်ဖိုးကို ဘယ်ထဲကို ဖြေထည့်ပေးလိုက်တယ်။
print(f'Swam_mark is {Swam_mark}')
print(type(Swam_mark))
print(f'Kyaw_mark is {Kyaw_mark}')
print(type(Kyaw_mark))
print(f'SuSu_mark is {SuSu_mark}')
print(type(SuSu_mark))
print(f'Myat_mark is {Myat_mark}')
print(type(Myat_mark))

# Tuple သည် immutable ဖြစ်သည်။ (List သည် mutable)
tup1 = 20, 30, 10
# tup1[0] = 40
print(tup1) # 'tuple' object does not support item assignment (item overwirte)

# Tuple is immutable but, can concatenate
tup2 = 4.5, 3.2
print(tup1 + tup2) # (20, 30, 10, 4.5, 3.2)

# Tuple သည် list လိုမျိုး append method တွေ pop method တွေနဲ့ items တွေကို modify လုပ်လို့မရပါဘူး။
# ဒါကြောင့် tuple မှာ သုံးလို့ရတဲ့ method က ၂ခုဘဲ ရှိပါတယ်။
score = 80, 40, 70, 80, 60, 40, 40
print(score.count(40))
print(score.index(70))