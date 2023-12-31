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
        'rock': ('We are draw', 0, 0),
        'paper': ('Player 2 wins', -1, 1),
        'scissor': ('You wins', 1, -1)
    },
    'paper': {
        'rock': ('You wins', 1, -1),
        'paper': ('We are draw', 0, 0),
        'scissor': ('Player 2 wins', -1, 1)
    },
    'scissor': {
        'rock': ('Player 2 wins', -1, 1),
        'paper': ('You wins', 1, -1),
        'scissor': ('We are draw', 0, 0)
    }
}

while Game_on:
    # input human
    P1 = input('Enter rock, paper, scissor : ')
    print(f'You are {P1}')
    print(Box[P1])
    # input computer
    P2 = random.choice(['rock', 'paper', 'scissor'])
    print(f'The Player 2 is {P2}')
    print(Box[P2])

    # process and display winner
    print(Process_Box[P1][P2][0])

    # add or substract score
    P1_score += Process_Box[P1][P2][1]
    if P1_score == -1:
        P1_score = 0
        print(f'Player 1 score is : {P1_score}')
    else:
        print(f'Player 1 score is : {P1_score}')
    
    P2_score += Process_Box[P1][P2][2]
    if P2_score == -1:
        P2_score = 0
        print(f'Player 2 score is : {P2_score}')
    else:
        print(f'Player 2 score is : {P2_score}')
    
    # stop or continue looping on condition
    if P1_score == 3:
        print(f'Player 1 wins , the score is {P1_score}')
        print(f'Player 2 fails, the score is {P2_score}')
        Game_on = False # Game ကို အဆုံးသတ်ခြင်းဖြစ်သည်။
    elif P2_score == 3:
        print(f'Player 2 wins , the score is {P2_score}')
        print(f'Player 1 fails , the score is {P1_score}')
        Game_on = False
    else:
        print('Nobody wins next round')