from Modules import RockPaperScissor
import random

Box = {
    'rock' : RockPaperScissor.rock,
    'paper' : RockPaperScissor.paper,
    'scissor' : RockPaperScissor.scissor
}

# Display user input
user_input = input('Enter rock, paper, scissor : ')
print(f'You are {user_input}')
print(Box[user_input])

# Display system input
Rock_Paper_Scissor = ['rock', 'paper', 'scissor']
system = random.choice(Rock_Paper_Scissor)
print(f'The system is {system}')
print(Box[system])

# Process the game
Process_box = {
    'rock' : {
        'rock': 'We are draw',
        'paper': 'The system wins',
        'scissor': 'You win'
    },
    'paper' : {
        'rock': 'You win',
        'paper': 'We are draw',
        'scissor': 'The system wins'
    },
    'scissor' : {
        'rock': 'The system wins',
        'paper': 'You win',
        'scissor': 'We are draw'
    }
}
print(Process_box[user_input][system])