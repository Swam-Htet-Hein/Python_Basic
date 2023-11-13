# Sequentail Statement
# Conditional Statement
# Looping Statement Or Iteration Statement

# Sequential Statement သည် အရှေ့က ရေးခဲ့တဲ့ code တွေလိုပဲ တစ်ကြောင်းပြီးရင်တစ်ကြောင်းအောက်ကိုဆင်းပြီး process လုပ်တယ်။

# Conditional Statement သည် မှန်လားမှားလားအရင်စစ်တယ် မှန်ရင် statement ကို run ပြီး မှားရင် statement ကို skip လုပ်တယ်။

# Looping Statement or Iteration Statement ကတော့ statement တစ်ခုကို ကိုယ့် run ချင်တဲ့ အကြိမ်ရေထိ သတ်မှတ်ပြီး run အောင်လုပ်တယ်။

# Looping Statement (for, while)

# Data container တစ်ခုထဲ့ကနေ items တွေကို တစ်ခုချင်းစီ ထုတ်ယူသုံးစွဲတာကို for loop
# List
names = ["Swam", "Myat", "Kyaw", "Thiha", "SuSu"]
for name in names:
    print(f'Hello, {name}')
# Tuple
tup = 100, 98, 46, 60, 78
for score in tup:
    print(f"You've got {score}")
# Dictionary
credit_cards = {
    'Swam': 10000,
    'SuSu': 5000,
    'Kyaw': 7500
}
for credit_card in credit_cards.items():
    print(credit_card)
# Set
setA = {2,3.5,6,1,4.5,100}
for num in setA:
    print(f'Set : {num}')

# range တစ်ခုသတ်မှတ်ပြီး statement ကို looping ပတ်ရင် range() ကိုသုံးသည်။
# range() သည် လိုအပ်မှ ဖန်တီးလိုက်သော int num generator တစ်ခုဖြစ်သည်။
# list တစ်ခုကို ဖန်တီးပြီးသုံးနိုင်သော်လည်း memory waste ဖြစ်နိုင်သည်။
# ဒါကြောင်း range() ကို သုံးပြီး for loop ကို control နိုင်သည်။

# range(start, end, step)
for i in range(0, 10):
    print(f'Hello world, {i}')

for i in range(0, 10, 2):
    print(f'Step : {i}')

# range() သည် C++ for loop နဲ့ ဆင်သည်
# for (int i=0; i<10; i++) {
#     cout << i << endl;
# }