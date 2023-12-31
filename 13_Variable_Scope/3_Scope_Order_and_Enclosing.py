
x = 'global x' # Global variable

def outer():
    x = 'outer x'

    def inner():
        # nonlocal x
        x = 'inner x' # Local variable
        print(x)
        # Local variable ကို ဖျက်လိုက်တဲ့ အခါ enclosing (outer x) ကို ယူတယ်။
        # Enclosing variable ကို ဖျက်လိုက်တဲ့ အခါ global (global x) ကို ယူတယ်။
        # Local > Enclosing > Global
    
    inner()
    print(x)
    # inner() အတွက် Enclosing varibale၊ အခု outer() အတွက် Local variable ကို ဖျက်လိုက်တော့၊ ဒီ outer() ပါ Global variable ကို လှမ်းယူတယ်။

outer()

# inner() သည် outer() ရဲ့ အတွင်းမှာရှိသည်။
# inner() ရဲ့ အမြင်ကကြည့်မယ်ဆိုရင် x သည် local variable၊ အပြင် x သည် enclosing variable ဖြစ်တယ်။
# ဒါကြောင့် inner() အတွက် scope order သည် Local > Enclosing > Global ဖြစ်တယ်။
# Built-in လည်းရှိသေးသည်။
# Buitl-in သည် Python file မှာကတည်းက ပါလာတဲ့ print, list, and dict စတဲ့ keywords တွေဖြစ်တယ်။
# Local > Enclosing > Global > Built-in

# inner() မှာ လည်း Local variable ရှိရက်သာနဲ့ Enclosing variable ကို သုံးချင်ရင် keyword (nonlocal) ကိုသုံးရတယ်။