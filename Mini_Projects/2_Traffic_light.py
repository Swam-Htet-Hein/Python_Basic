light = ''
Is_there_police = False

if light == 'Green':
    print('Go')
elif light == 'Red':
    if Is_there_police:
        print('Stop and Wait')
    else:
        print('Go')
elif light == 'Yellow':
    if Is_there_police:
        print('Stop and Wait')
    else:
        print('Go faster')
else:
    print('It\'s your bussiness, I don\'t care')