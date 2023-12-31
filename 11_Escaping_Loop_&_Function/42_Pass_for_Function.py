# Pass သည် function တွေအတွက် break နဲ့ loop တွေလိုပဲ။
# pass သည် looping တွေမှာလည်းသုံးလို့ရသည်။

# Like continue
def func(n):
    if n > 0:
        if n == 5 or n == 3:
            pass
        else:
            print(n, end=' ')
        func(n-1)

func(10)

print()

# Like break
def func1(n):
    if n > 0:
        print(f'{n} is greater than 0')
    else:
        pass

func1(-4)

print()

# Leave function nothing
def nothing():
    pass

nothing()