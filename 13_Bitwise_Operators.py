# Decimal and Binary
# Decimal is the value with base 10 (0,1,2,3,4,...,15)
# Binary is the value with base 2 (0,1)
# Decimal and Binary can be converted into each other (5 --> 0101)
# Decimal | Binary
#   0-9   | 8 4 2 1
#   1     | 0 0 0 1
#   2     | 0 0 1 0
#   3     | 0 0 1 1
#   4     | 0 1 0 0

# Bitwise operators calculate the binary value not decimal value
# Bitwise AND ==> (&)
# Bitwise OR ==> (|)
# Bitwise XOR ==> (^)
# Bitwise NOT ==> (~)
# Bitwise Left shift ==> (<<)
# Bitwise Right shift ==> (>>)

# Bitwise AND
x = 2       # 0 0 1 0 
y = 3       # 0 0 1 1
print(x & y)# 0 0 1 0 convert to decimal is 2
            # Used AND
x = 30      # 1 1 1 1 0
y = 20      # 1 0 1 0 0
print(x & y)# 1 0 1 0 0 convert to decimal is 20
            # Used AND

# Bitwise OR
x = 2       # 0 0 1 0
y = 3       # 0 0 1 1
print(x | y)# 0 0 1 1 convert to decimal is 3
            # Used OR

# Bitwise XOR
# XOR သည် နှစ်ခုတူညီနေရင် 0 return ပြန်တယ်။
x = 2       # 0 0 1 0
y = 3       # 0 0 1 1
print(x ^ y)# 0 0 0 1 convert to decimal is 1
            # Used XOR

# Bitwise NOT
x = 6
print(~x) # 0 1 1 0 ==> -(0 1 1 0 + 1) ==> -(0 1 1 1) convert to decimal is -7

# Bitwise Shifts (left and right)
# binary(2) <<(left shift)(2)
# 0 0 1 0 << 0 0 ==> 0 0 1 0 0 0 (0 0 နှစ်ခုကို ဘယ်ဘက်ကနေတွန်းပို့ ပေးလိုက်တာ)
             # 8 4 2 1 base 2
x = 2        # 0 0 1 0
             # 32 16 8 4 2 1 base 2 (left shift)
print(x << 2)# 0  0  1 0 0 0 convert to decimal is 8

# binary(2) >>(right shift)(2)
# 0 0 >> 0 0 1 0 ==> 0 0 0 0 1 0 (0 0 နှစ်ခုကို ညာဘက်ကနေတွန်းပို့ ပေးလိုက်တာ)
             # 8 4 2 1 base 2
y = 2        # 0 0 1 0
             # 8 4 2 1 0 0 base 2 (right shift)
print(y >> 2)# 0 0 0 0 1 0 convert to decimal is 0

# left shift သည် binary တွန်းပို့ခံရလျှင် decimal base ပြောင်းလဲမှုရှိသည်။
# right shift သည် binary ကို ညာဘက်ကနေတွန်းပို့ခံရတဲ့ အတွက်ကြောင့် decimal base ပြောင်းလဲမှုမရှိပါ။