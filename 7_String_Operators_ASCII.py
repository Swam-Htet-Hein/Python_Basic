# python သည် unicode character (ASCII) ကိုအသုံးပြုထားသည်
print(ord('a')) # 97 in decimal
print(ord('b')) # 98 in decimal
print(ord('c')) # 99 in decimal

print()

# ဒါ့ကြောင့် comparison operators တွေသုံးတော့မယ်ဆိုရင် ASCII ကအဓိကကျ လာပါပြီ
print('a' > 'b')
print('b' > 'c')
print('a' < 'b')
print('b' < 'c')

print()

name = 'Swam'
address = 'Mandalay Myanmar'
print(name > address) # comparison operator သည် ရှေ့ဆုံးကဟာကိုပဲ ယူတဲ့ အတွက် length နဲ့ မဆိုင်ပါ။

print()

print('Sw' in name) # in သည် ရှိရင် True မရှိရင် False
print('sw' in name)
print('Sw' not in name) # not in သည် ရှိရင် False မရှိရင် True
print('sw' not in name)

print()

# character to unicode (ord())
print(ord('A')) # 65 decimal
print(type(ord('A')))
# unicode to character (chr())
print(chr(65)) # A character
print(type(chr(65)))
