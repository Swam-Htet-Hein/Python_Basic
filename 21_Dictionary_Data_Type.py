# Dictionary data-type stores values with keys
# {key : value}
# Dictionary data-type is unordered.
contacts = {
    # keys: values
    'Swam': '094545',
    'Myat': '096767',
    'Kyaw': '095656'
}
print(contacts)
print(type(contacts))

# value ပြန်ထုတ်ချင်ရင် index အစား key နဲ့ ပြန်ထုတ်ရတယ်။
print(f'Swam: {contacts["Swam"]}')
print(f'Myat: {contacts["Myat"]}')
print(f'Kyaw: {contacts["Kyaw"]}')

# Dictionary data-type သည် key တူလို့မရပါဘူး။ key သည် unique ဖြစ်ရပါမယ်။
address = {
    'Swam': '19st Mandalay',
    'Htet': '58st Mandalay',
    'Swam': 'Yuzana Yangon',
    'Kyaw': '19st Mandalay'
}
print(f'Swam: {address["Swam"]}') # Swam: Yuzana Yangon
# နောက်ဆုံး က value ကို လှမ်းယူပြီး၊ ရှေ့ကဟာကို ချန်ထားလိုက်တာပါ။

# Dictionary data-type သည် key တူလို့မရပေမဲ့ value တော့တူလို့ရတယ်။
print(f'Swam: {address["Swam"]}')
print(f'Kyaw: {address["Kyaw"]}')

# Dictionary Class ကနေ object တစ်ခုကို constructor နဲ့ ကြေညာပြီး ဖန်တီးလို့ရတယ်။
personality = dict()
print(f'Personality: {personality}')
# add keys and values into dictionary
personality['Swam'] = 'Handsome'
print(f'Swam\'s Personality: {personality["Swam"]}')
personality['Kyaw'] = 'Smart'
print(f'Kyaw\'s Personality: {personality["Kyaw"]}')
print(f'Personality: {personality}')

# Dictionary method ==> get()
# get() သည် key ရဲ့ value ကို return ပြန်ပေးသည်။
print(contacts.get('Swam')) # 094545
print(address.get('Kyaw')) # 19st Mandalay
print(personality.get('Swam')) # Handsome