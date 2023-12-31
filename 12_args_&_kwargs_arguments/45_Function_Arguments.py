def greet(name, age):
    print(f'Hello {name}, You are {age} years old.')

# Positional arguments
greet('Swam', 21)
greet(21, 'Swam')
# Positional arguments သည် function parameter အစဉ်လိုက်အတိုင်းပဲ တန်ဖိုးအစားသွင်းတယ်။

# Keyword arguments
greet(name='Kyaw', age=30)
greet(age=30, name='Kyaw')
# Keyword arguments သည် function parameter ထဲက varible name တွေကို keyword အနေနဲ့ သုံးပြီး တန်ဖိုးအစားသွင်းတယ်။

# *args ==> Multiple positional arguments
# Positional arguments လိုမျိုး parameter တွေသတ်မှတ်ထားမှ အဲဒီ parameter ထဲကို တန်ဖိုးအစားလို့ ရတာမဟုတ်တော့ဘဲ။
# ကိုယ်ကြိုက်သလောက် arguments တွေကို ပေးပြီး၊ အဲဒီ arguments တွေကို tuple ထဲမှာ store လုပ်ပြီး function ထဲမှာအသုံးပြုလို့ရတယ်။
def test(*num): # *args သည် standard ဖြစ်သည်။
    print(num) # (1, 2, 3, 4, 5)
    print(type(num)) # <class 'tuple'>
test(1,2,3,4,5)

def add(*operands):
    result = 0
    for i in operands:
        result += i
    return result
print(add(1,2,3,4,5)) # 15

# **kwargs ==> Multiple keyword arguments
# **kwargs သည် arguments ကို key, value နဲ့ ယူပြီး၊ dictionary data-type နဲ store သည်။
def student_info(**kwargs):
    print(kwargs) # {'name': 'Swam', 'age': 21, 'school': 'Python'}
    print(type(kwargs))
    print(f'Name : {kwargs["name"]}')
    print(f'Age : {kwargs["age"]}')
    print(f'School : {kwargs["school"]}')
student_info(name = 'Swam', age = 21, school = 'Python')

# Positional arguments, Multiple Positional arguments and Multiple Keyword arguments တွေကို Function တစ်ခုတည်းမှာပဲ အသုံးချချင်ရင် order of arguments ကို နားလည်ရမယ်။
# Order of Arguments
# 1. Positional arguments
# 2. Multiple Positional arguments
# 3. Multiple Keyword arguments
def combine(x, y, z, *args, **kwargs):
    print(x, y, z)
    print(args)
    print(kwargs)
combine('Swam', 40, True, 'Hello', 3.5, False, num = 23, width = '720px')