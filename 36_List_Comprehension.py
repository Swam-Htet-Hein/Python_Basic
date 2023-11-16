lst = [1,2,3,4]
# new list တစ်ခုကို modified လုပ်ထားတဲ့ မှုရင်း list နဲ့ ဖန်တီးချင်တယ်။

new_lst = list()
# for member in iterable-obj
for i in lst:
    new_lst.append(i * 2) # expression
print(f'Simple method : {new_lst}')
# 4 lines လောက်သုံးရတဲ့ code ကိုရေးမဲ့ အစား 1 line ပဲသုံးရမဲ့ code ကို ရေးချင်တယ်။

# new_list = expression for member in iterable-obj
new_lst = [i*2 for i in lst]
print(f'Comprehension method : {new_lst}')

# ဘယ်ဘက်ဆုံးက expression သည် return value လည်းဖြစ်သည်။
# for member in obj သည် looping ပတ်ခြင်းဖြစ်သည်။
# [expression for member in iterabale-obj if condition]
even_num = [i for i in range(1, 21) if i%2 == 0] # အကယ်၍ i သည် 2 နဲ့စားလို့ပြတ်ရင် ရှေ့ဆုံးက i တန်ဖိုးကို return ပြန်ပေးပါ။
print(f'Comprehension method for even num : {even_num}')
odd_num = [i-1 for i in range(1, 21) if i%2 == 0]
print(f'Comprehension method for odd num : {odd_num}')
