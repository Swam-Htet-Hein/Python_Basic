# Comparison operators
# Less than ==> (<)
# Greater than ==> (>)
# Less than equal ==> (<=)
# Greater than equal ==> (>=)
# Equal to ==> (==)
# Not equal to ==> (!=)
# Equal to (identity) ==> (is)
# Not equal to (identity) ==> (is not)

# The output data-type of comparison operators is Boolean(True, False)

a = 5
b = 2

print(a < b) # 5 < 2 False
print(a > b) # 5 > 2 True

a = 3
b = 3

print(a < b) # 3 < 3 False
print(a > b) # 3 > 3 False
print(a <= b) # 3 < 3 or 3 == 3 True
print(a >= b) # 3 > 3 or 3 == 3 True
print(5 >= 3) # True

print(a == b) # 3 == 3 True
print(a != b) # 3 != 3 False
print(3 != 4) # True

# is, is not are identity operators
# It can use to check the objects of a class that are same identity or not.
lit1 = [1,2,3]
lit2 = [1,2,3]
print(lit1 == lit2) # "==" checks the items in the box (True)
print(lit1 is lit1) # "is" checks the identity of the objects (False)
print(lit1 is lit2) 
print(id(lit1)) # id() method use to find the memory address of an object
print(id(lit2))