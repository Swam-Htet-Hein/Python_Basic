names = ['Swam', 'Aung', 'Kyaw']

# insert() 
# insert() သည် append() လို နောက်ဆုံးမှာ သွားထည့်တာမဟုတ်ဘဲ ကိုယ်ထည့်ချင်တဲ့ index ထဲမှာ ထည့်လို့ရတယ်။
names.insert(0, 'SuSu')
print(names) # အရင် သုံးခု ကို ညာဘက်ကို တွန်းပို့လိုက်ပြီး၊ index 0 နေရာမှာ 'SuSu' ကို ထည့်လိုက်တယ်။
names.insert(2, 'Htet')
print(names)
# ['SuSu', 'Swam', 'Htet', 'Aung', 'Kyaw']

# remove() 
# remove() သည် pop() လိုမျိုး index တွေနဲ့ ဖျက်တာမဟုတ်ဘဲ့ items value တွေနဲ့ ဖျက်တယ်။
names.remove('Swam')
print(names)
# ['SuSu', 'Htet', 'Aung', 'Kyaw']

# index()
# index() သည် list ထဲမှာရှိတဲ့ items တွေရဲ့ index ကို return ပြန်ပေးတယ်။
index_of_Htet = names.index('Htet')
print(index_of_Htet) # Htet သည် index 1 မှာရှိတဲ့အတွက် 1 ပြန်တယ်။

# copy() 
# copy() သည် list ကို အခြား list နဲ့ copy ကူးလိုက်ခြင်းဖြစ်သည်။
copy_of_names = names.copy()
print(copy_of_names)
# ['SuSu', 'Htet', 'Aung', 'Kyaw']

# clear()
# clear() သည် list အတွင်းမှာရှိတဲ့ items တွေကို ရှင်းထုတ်ပစ်တာပါ။
# names.clear()
# print(names) ==> []

# sort() 
# sort() သည် items တွေကို int တန်းဖိုးအလိုက် ငယ်စဉ်ကြီးလိုက် စီတာပါ။
num = [6,3,7,4,9,2,3,4]
num.sort()
print(num)
num.sort(reverse=True)
print(num)

# reverse() 
# reverse() သည် List slice ကို step -1 ထားလိုက်သလိုပဲ items တွေကို ပြောင်းပြန် လှန်တယ်။
names.reverse()
print(names)
# ['Kyaw', 'Aung', 'Htet', 'SuSu']