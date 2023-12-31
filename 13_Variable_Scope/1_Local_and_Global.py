# Local variable and Global variable
# Local variable ကို Global မှာလာသုံးလို့ မရ။
# Global variable ကို Local မှာလာသုံးလို့ ရ။

name = 'Swam Htet' # Global variable

def greet():
    name = 'Kyaw Kyaw' # Local variable
    print(f"(Local) Hello {name}") # using local variable

greet()
print(f"(Global) Hello {name}") # using global variable
# Local variable ကို Global မှာလာသုံးလို့ မရတဲ့ အတွက် NameError: name 'name' is not defined ဆိုပြီး ပြနေမှာပါ။