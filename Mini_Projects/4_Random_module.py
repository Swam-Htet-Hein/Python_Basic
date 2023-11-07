from random import choice

header = """

  _    _ ______          _____      ____  _____     _______       _____ _      
 | |  | |  ____|   /\   |  __ \    / __ \|  __ \   |__   __|/\   |_   _| |     
 | |__| | |__     /  \  | |  | |  | |  | | |__) |     | |  /  \    | | | |     
 |  __  |  __|   / /\ \ | |  | |  | |  | |  _  /      | | / /\ \   | | | |     
 | |  | | |____ / ____ \| |__| |  | |__| | | \ \      | |/ ____ \ _| |_| |____ 
 |_|  |_|______/_/    \_\_____/    \____/|_|  \_\     |_/_/    \_\_____|______|
                                                                               
                                                                               

"""
head = """

  _    _ ______          _____  
 | |  | |  ____|   /\   |  __ \ 
 | |__| | |__     /  \  | |  | |
 |  __  |  __|   / /\ \ | |  | |
 | |  | | |____ / ____ \| |__| |
 |_|  |_|______/_/    \_\_____/ 
                                
                                

"""
tail = """

  _______       _____ _      
 |__   __|/\   |_   _| |     
    | |  /  \    | | | |     
    | | / /\ \   | | | |     
    | |/ ____ \ _| |_| |____ 
    |_/_/    \_\_____|______|
                             
                             

"""
print(header)
coin = ['head', 'tail']
user_input = input('Head or Tail: ')
pc_generated = choice(coin)
if user_input == pc_generated:
    if pc_generated == 'head':
        print(head)
    else:
        print(tail)
    print('You win!!')
else:
    if pc_generated == 'head':
        print(head)
    else:
        print(tail)
    print('You lose!!')