# main code ကနေ function ထဲကို တန်ဖိုးတွေထည့်သုံး ချင်ရင် Function() မှာ parameter ထည့်ကြေညာရတယ်။

def Func(a, b):
    return a + b

def YesNo(answer):
    if answer == 'Yes':
        return 'You typed Yes'
    elif answer == 'No':
        return 'You typed No'
    else:
        print('You typed nothing')

# return function ဖြစ်တဲ့အတွက် တန်ဖိုးအစားသုံးရမယ်။
add = Func(1, 2) # Func ရဲ့ ()ထဲမှာ ရေးထားတဲ့ဟာကို parameter လို့ခေါ်ပြီး အခု ခေါ်သုံးထားတဲ့ ()ထဲမှာရေးထားတဲ့ဟာကို argument လို့ခေါ်တယ်။
print(add)

user_input = input('Enter Yes or No : ')
result = YesNo(user_input)
print(result)