# Assignment operators assign value from right to left

# Assign value ==> (=)
x = 20 # x is assigned by value 20 and now is 20
print(f'line 5 : {x}')
# value can be any data-type (int, float, str, bool, etc...)

# Add and assign value ==> (+=)
x += 20 # x is added and assigned by value 20 and now is 20 + 20 = 40
print(f'line 10 : {x}')

# Substract and assign value ==> (-=)
x -= 10 # x is substracted and assigned by value 10 and now is 40 - 10 = 30
print(f'line 14 : {x}')

# Multiply and assign value ==> (*=)
x *= 2 # x is multiplied and assigned by value 2 and now is 30 * 2 = 60
print(f'line 18 : {x}')

# Divide and assign value ==> (/=)
x /= 3 # x is divided and assigned by value 3 and now is 60 / 3 = 20
print(f'line 22 : {x}')

# Floor divide and assign value ==> (//=)
x //= 3 # x is floor divided and assigned by value 3 and now is 20 // 3 = 6
print(f'line 26 : {x}')

# Modulus and assign value ==> (%=)
x %= 4 # x is divided, return modulus value and assigned by value 4 and now is 6 % 4 = 2
print(f'line 30 : {x}')