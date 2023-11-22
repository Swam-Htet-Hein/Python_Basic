# Continue ==> skip the selected loop
# continue can only be used within a loop

for i in range(10):
    if i == 2 or i == 5 or i == 6:
        continue
        print('Hello') # skip this statement
    else:
        print(f'i : {i}', end=' | ')
        # i : 0 | i : 1 | i : 3 | i : 4 | i : 7 | i : 8 | i : 9 |