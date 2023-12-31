# Break ==> stop the looping of its body
# break can only be used within a loop

for i in range(8):
    if i == 6:
        break # i က 6 ရောက်တော့ looping break လုပ်လိုက်တယ်။
    else:
        print(f'i : {i}', end='|')

print()

# Break သည် သူ့ looping ကိုပဲ သူ ရပ်တယ်။
for out in range(5):
    # out loop ကို မရပ်ပစ်ဘူး
    print(f'out : {out}')
    for inside in range(8):
        if inside == 6:
            break
        else:
            print(f'inside : {inside}', end='|')