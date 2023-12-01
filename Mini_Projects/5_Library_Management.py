# Show lists
# Register books
# Remove books
# Search books
# Quit Library

book_lists = ['Hello', 'World']

# Register books
def register_function():
    print(book_lists)
    while True:
        user_add = input("Enter books (exit) : ")
        if user_add == 'exit':
            break
        else:
            book_lists.append(user_add)
            print(f"You added {user_add}")
    print(book_lists)

# Remove books
def remove_function():
    for i in book_lists:
        print(f"[{book_lists.index(i)}] : {i}")
    book_index = [book_lists.index(i) for i in book_lists]
    while True:
        user_remove = int(input('Enter book index to remove (-1 to exit) : '))
        if user_remove in book_index:
            print(f"You removed {book_lists[user_remove]}")
            book_lists.pop(user_remove) 
            for i in book_lists:
                print(f"[{book_lists.index(i)}] : {i}")         
        elif user_remove == -1:
            break
        else:
            print(f"Index {user_remove} is not found in the list.")
    for i in book_lists:
        print(f"[{book_lists.index(i)}] : {i}")

# Search books
def search_function():
    while True:
        user_search = input('Enter book name (0 to exit): ')
        if user_search in book_lists:
            print(f"[{book_lists.index(user_search)}] : {user_search}")
        elif user_search == '0':
            break
        else:
            print(f"{user_search} is not found in the list.")

print("Welcome to Library")
print("------------------")
while True :
    # Request from user
    print("# Show")
    print("# Register")
    print("# Remove")
    print("# Search")
    print("# Quit")
    print("------------------")
    user_input = input(': ')
    if user_input == 'Show':
        # Show lists
        for i in book_lists:
            print(f"[{book_lists.index(i)}] : {i}")
        print()
    elif user_input == 'Register':
        register_function()
        user_input = input('Do you want to do other things (yes)(no): ')
        if user_input == 'yes':
            continue
        else:
            break
    elif user_input == 'Remove':
        remove_function()
        user_input = input('Do you want to do other things (yes)(no): ')
        if user_input == 'yes':
            continue
        else:
            break
    elif user_input == 'Search':
        search_function()
        user_input = input('Do you want to do other things (yes)(no): ')
        if user_input == 'yes':
            continue
        else:
            break
    elif user_input == 'Quit':
        # Quit Library
        break
    else:
        print('Something wrong!')
