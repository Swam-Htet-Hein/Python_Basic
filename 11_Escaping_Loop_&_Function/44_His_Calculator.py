def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def multi(x, y):
    return x * y
def div(x, y):
    return x / y

print("1. add\n2. substract\n3. multiply\n4. divide")

while True:
    user_input = int(input('Enter 0=exit, 1, 2, 3, 4 : '))
    if user_input in (1,2,3,4):
        first = int(input('Enter first : '))
        second = int(input('Enter second : '))
        if user_input == 1:
            print(f'{first}+{second}={add(first, second)}')
            user_input = input('Do you want to continue? yes, no :')
            if user_input == 'yes':
                continue
            else:
                break
        elif user_input == 2:
            print(f'{first}-{second}={sub(first, second)}')
            user_input = input('Do you want to continue? yes, no :')
            if user_input == 'yes':
                continue
            else:
                break
        elif user_input == 3:
            print(f'{first}*{second}={multi(first, second)}')
            user_input = input('Do you want to continue? yes, no :')
            if user_input == 'yes':
                continue
            else:
                break
        elif user_input == 4:
            print(f'{first}/{second}={div(first, second)}')
            user_input = input('Do you want to continue? yes, no :')
            if user_input == 'yes':
                continue
            else:
                break
    elif user_input == 0:
        break
    else:
        print("Invalid answer!!")