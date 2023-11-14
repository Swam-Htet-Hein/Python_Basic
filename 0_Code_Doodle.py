import random
from Modules import RockPaperScissor

P1 = None # P1 is human
P2 = None # P2 is computer
P1_score = 0
P2_score = 0
Game_on = True

# RockPaperScissorBox
Box = {
    'rock': RockPaperScissor.rock,
    'paper': RockPaperScissor.paper,
    'scissor': RockPaperScissor.scissor
}
# Process The Game
Process_Box = {
    'rock': {
        'rock': ('We are draw', 0),
        'paper': ('System wins', -1),
        'scissor': ('You wins', 1)
    },
    'paper': {
        'rock': ('You wins', 1),
        'paper': ('We are draw', 0),
        'scissor': ('System wins', -1)
    },
    'scissor': {
        'rock': ('System wins', -1),
        'paper': ('You wins', 1),
        'scissor': ('We are draw', 0)
    }
}

P1 = input('Enter rock, paper, scissor : ')
print(f'You are {P1}')
print(Box[P1])
P2 = random.choice(['rock', 'paper', 'scissor'])
print(f'The system is {P2}')
print(Box[P2])

print(Process_Box[P1][P2][0])