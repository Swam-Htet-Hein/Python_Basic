# if statement
# if သည် True or False အပေါ်မှာ မှုတည်ပြီးဆုံးဖြတ်သည်။
a = 5
b = 3
# if သည် condition မှန်ရင် သူ့အောက်က statement ကို run မယ်။
# မမှန်ရင်တော့ skip လုပ်မယ်။
if a > b:
    print('a is greater than b')

# if else statement
a = 2
b = 3
# if else သည် if က မှန်ရင် သူ့အောက်က statement ကို run ပြီး၊ မမှန်ရင် else အောက်ဟာကို run မယ်။
if a < b:
    print('a is less than b')
else:
    print('a is greater than b')

# if elif else statement
a = 3
b = 3
# if elif else သည် if, elif တို့ရဲ့ condition ကို အရင် စစ်တယ်။
# အဲ့ဒါတွေ အကုန်မှားမှ else အောက်ကဟာကို run တယ်။
if a > b:
    print('a is greater than b')
elif a < b:
    print('a is less than b')
else:
    print('a is equal to b')