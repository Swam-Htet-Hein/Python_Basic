# Dictionary Operations
books = {
    'MaungKyaw': 'Python programming',
    'TunThiha': 'C++ programming'
}
print(books) # {'MaungKyaw': 'Python programming', 'TunThiha': 'C++ programming'}

# Adding, Updating and Deleting
# Adding new keys and values
# Dictionary ထဲသို့ keys နဲ့ value အသစ်ပေါင်းထည့်ခြင်း
books['KyawThu'] = 'Java programming'
print(books) # {'MaungKyaw': 'Python programming', 'TunThiha': 'C++ programming', 'KyawThu': 'Java programming'}

# Updating existing keys
# ရှိပြီးသား key ထဲကို value ပြောင်းလဲခြင်း
books['MaungKyaw'] = 'Advance Python programming'
books['TunThiha'] = 'Unreal Game Engine'
print(books) # {'MaungKyaw': 'Advance Python programming', 'TunThiha': 'Unreal Game Engine', 'KyawThu': 'Java programming'} 

# Deleting existing keys and values
# ရှိပြီးသား key နဲ့ value တွေကို ဖျက်ခြင်း
del(books['KyawThu'])
print(books) # {'MaungKyaw': 'Advance Python programming', 'TunThiha': 'Unreal Game Engine'}
# del() သည် key, value ကို ဖျက်ပေးနိုင်သော်လည်း return မပြန်ပါ။

# pop() သည် ကိုယ်ဖျက်လိုက်တဲ့ အရာကို return ပြန်ပြီး dictionary ကိုလည်းပြုပြင်ပေးသည်
deleted_book = books.pop('MaungKyaw') # () ထဲ့ဘာမှမရေးလျှင် default အနေဖြင့် နောက်ဆုံးကဟာကို ဖျက်ပစ်တယ်။
print(f'deleted book: {deleted_book}') # pop() သည် ကိုယ်ဖျက်လိုက်တဲ့ key ရဲ့ value ကို ပဲ return ပြန်တယ်။ # Advance Python programming
print(books) # {'TunThiha': 'Unreal Game Engine'}

# popitem() သည် ကိုယ်ဖျက်တဲ့ key ရော value ရော return ပြန်ပေးတယ်။
names = {
    'Swam': 21,
    'Kyaw': 25,
    'SuSu': 23
}
print(f"Deleted by pop() : {names.pop('Swam')}") # key ကို return မပြန်ဘဲ့ value 21 ကို ပဲ return ပြန်တယ်။
print(f"Deleted by popitem() : {names.popitem()}") # key ကို ပြန်ရုံသာမက value ကို ပါပေါင်းပြီး tuple data-type အနေနဲ့ return ပြန်ပေးတယ်။
# ('SuSu', 23)
# popitem သည် takes no arguments ဖြစ်တဲ့ အတွက်() ထဲ ဘာမှထည့်လိုမရပါဘူး။
print(names) # {'Kyaw': 25}

# Checking items with keyword 'in'
# 'in' နဲ့ Dictionary ထဲ့ မှာ ကိုယ်ရှာနေတဲ့ item ရှိမရှိ စစ်ဆေးခြင်း
Identity = {
    'Jhon': '001',
    'Sophia': '002',
    'Bob': '003'
}
# 'in' သည် boolean နဲ့ ပြန်ထုတ်တယ်။
print('Jhon' in Identity) # True
print('Bob' in Identity) # True
print('James' in Identity) # False

# Update Dictionary by other Dictionaries
Extended_identity = {
    'James': '004',
    'Dylan': '005',
    'Lucy': '006'
}
# update() သည် တခြား Dictionary တစ်ခု ကို ကိုယ်ပေါင်းထည့်ချင်တဲ့ Dictionary ထဲ ပေါင်းထည့် ပေးတယ်။
print(Identity) # {'Jhon': '001', 'Sophia': '002', 'Bob': '003'}
Identity.update(Extended_identity)
print(Identity) # {'Jhon': '001', 'Sophia': '002', 'Bob': '003', 'James': '004', 'Dylan': '005', 'Lucy': '006'}