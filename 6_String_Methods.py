first_name = "Sophia"
last_name = "Taylor"

# the combination of two or more strings is concatenation
# the concatenation can be used for same data-type
print(first_name +' '+ last_name)

full_name = first_name + ' ' + last_name
length_of_full_name = len(full_name) # len() can be used to find the amount of string
print(length_of_full_name)

Head_line = "computer science college is open"
# python မှာ အရာအားလုံးသည် objects (ပစ္စည်း) တွေဖြစ်တယ်။
# ပစ္စည်းတွေမှာ ကိုယ်ပိုင်အရည်အချင်းတွေ ပြုမှုပုံတွေ ရှိတယ်။
# python string လည်း object ဖြစ်တဲ့ အတွက် သုံးလိုရမဲ့ method တွေရှိတယ်။
# object ရဲ့ method တွေသည်များသောအားဖြင့် return method ဖြစ်သည်။

capitalize_head_line = Head_line.capitalize()
print(type(capitalize_head_line))
print(capitalize_head_line) # paragraph ရဲ့ အရှေ့ဆုံးကဟာကို အကြီးလုပ်ပေးတယ်။

title_head_line = Head_line.title()
print(type(title_head_line))
print(title_head_line) # စကားလုံးတစ်လုံးချင်းစီရဲ့ ရှေ့ကို စာလုံးကြီး လုပ်ပေးတယ်။

count_head_line = Head_line.count('c')
print(type(count_head_line))
print(count_head_line) # count ထဲ့မှာ ရှိတဲ့ c က string ထဲမှာ ဘယ်နလုံးရှိလဲဆိုတာဖော်ပြတယ်။ 

startswith_head_line = Head_line.startswith('c')
print(type(startswith_head_line))
print(startswith_head_line) # string ထဲမှာ c နဲ့ စရင် True မစရင် False
endswith_head_line = Head_line.endswith('n')
print(type(endswith_head_line))
print(endswith_head_line)   # string ထဲမှာ n နဲ့ ဆုံးရင် True မဆုံးရင် False

upper_head_line = Head_line.upper()
lower_head_line = Head_line.lower()
print(type(upper_head_line))
print(upper_head_line) # make all capital letter
print(lower_head_line) # make all small letter

content = 'computer programming and computer science are more popular than the last decade.'
print('Is this all lower cases?', end=' ')
print(content.islower())
print('Is this all upper cases?', end=' ')
print(content.isupper())