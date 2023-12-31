names = ['Swam Htet', 'Kyaw Kyaw', 'Maung Maung', 'Aye Aye', 'Mya Mya']
print(names)
select_names = names[0:3]
print(select_names)

# Nested List
# List ထဲမှာမှ list ကို ပြန်ထည့်သုံးတာကို nested list လို့ခေါ်တယ်။
classA = ['Swam', 'Aung']
classB = ['Htet', 'Kyaw']
classC = ['Aye', 'Myat']
grade10 = [classA, classB, classC] # [['Swam', 'Aung'], ['Htet', 'Kyaw'], ['Aye', 'Myat']]
print(grade10)
print(len(grade10))
print(grade10[0]) # ['Swam', 'Aung']
print(grade10[1]) # ['Htet', 'Kyaw']
print(grade10[2]) # ['Aye', 'Myat']

# Class ထဲမှာရှိတဲ့ သူတွေကို ပြန်ဆွဲထုတ်တယ်။
print(grade10[0][0])
print(grade10[0][1])
print(grade10[1][0])
print(grade10[1][1])
print(grade10[2][0])
print(grade10[2][1])