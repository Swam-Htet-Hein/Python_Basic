def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

while True:
    print('\nSimple Calculator\n 1. add\n 2. substract\n 3. multiply\n 4. divide')
    user_input = int(input('Enter 1, 2, 3, 4 : '))
    if user_input == 1:
        first = int(input('Enter first : '))
        second = int(input('Enter second : '))
        print(f'{first} + {second} = {add(first, second)}')
        user_input = input('Do you want to continue? (yes, no): ')
        if user_input == 'yes':
            continue
        else:
            break
    elif user_input == 2:
        first = int(input('Enter first : '))
        second = int(input('Enter second : '))
        print(f'{first} - {second} = {substract(first, second)}')
        user_input = input('Do you want to continue? (yes, no): ')
        if user_input == 'yes':
            continue
        else:
            break
    elif user_input == 3:
        first = int(input('Enter first : '))
        second = int(input('Enter second : '))
        print(f'{first} * {second} = {multiply(first, second)}')
        user_input = input('Do you want to continue? (yes, no): ')
        if user_input == 'yes':
            continue
        else:
            break
    elif user_input == 4:
        first = int(input('Enter first : '))
        second = int(input('Enter second : '))
        print(f'{first} / {second} = {divide(first, second)}')
        user_input = input('Do you want to continue? (yes, no): ')
        if user_input == 'yes':
            continue
        else:
            break
    elif user_input == 0:
        break
    else:
        print('Invalid answer!')