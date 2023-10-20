# Operators ==> operations
# operations ==> Arithmetic, Logical, ...etc

# Operators ==> In-fix operators and Pre-fix operators
# In-fix operators have 2 operands(1+3) and also called Binary Operators
# Pre-fix operators are called Unary Operators (i++)

# Operators
# Arithmetic Operators (Addition(+), Substraction(-), Multiplication(*), Division(/,//,%), Exponential(**))
# Logical Operators (not, and, or)
# Assignment Operators (=)
# Bitwise Operators (&&, ||)
# Comparicon Operators (<, >, ==, !=, <=, >=)

# Arithmetic Operators
print(2+3)
print(5-2)
print(2.6+3.4)
print(6.5-2.3)
print(2*3)
print(2.0*3.5)

# Division (float quotient(/), floor quotient(//), modulo(%))
# float quotient သည် ရိုးရိုး စာလဒ်ကို ထုတ်ပေးသည်။
print(10/2) # floating number
print(4/3)

# floor quotient သည် ပျက်သည်အထိ မစားထားတဲ့ စာလဒ်ကို ထုတ်ပေးသည်။
print(10//3) # decimal number ရဲ့ floor တန်ဖိုးကို ပဲယူတယ်။
print(5//3)
print(10//2)

# modulo သည် စားကြွင်းကို ထုတ်ပေးသည်။
print(10%3) # integer number စားကြွင်းကို ထုတ်ပေးသည်။
print(4%2)

# Exponential သည် ထပ်ကိန်းဖြစ်သည်
print(2 ** 3)
print(5 ** 2)

# Operators Procedure (BEDMAS)
# Operators တွေကို အောက်ပါအတိုင်းအစဉ်လိုက် တွက်ချက်တယ်။
# B - Brackets or ()
# E - Exponential
# DM - Division and Multiplication
# AS - Addition and Substraction

# AS - Addition and Substraction
# Substract First, Addition Second
print(3+2-1) # 4
print(5+2-1+10-3) # 13

# DM - Division and Multiplication
# Just consider Left to Right
print(6/2*4) # 12.0
print(6*2/4) # 3.0

# Brackets and Exponential
print(2**3+(2+2)) # 12

# Combine all of these
print(2 ** 3 + 4 * 5 / 2 + 6 - 3 - 1 + 10 / 5 + 5 * 3 + (1+2))
