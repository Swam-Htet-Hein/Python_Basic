# Set Data-type သည် immutable ဖြစ်သော်လည်း method() တွေသုံးပြီး add and remove လုပ်လို့ရတယ်။

# add method
my_set = set()
# add new items into set by using add()
# add() can only take one argument
my_set.add('apple')
my_set.add('orange')
my_set.add('banana')
print(my_set)

# remove or discard method
my_set = {1,2,3,4,5,6}
print(my_set)
my_set.remove(1)
print(my_set)
my_set.discard(3)
print(my_set)

# Union, Interset, Different
set_A = {1, 2, 4, 7, 9, 11}
set_B = {1, 2, 3, 4, 5, 9}

# Union သည် အစုနှစ်ခုလုံး ကို တစ်ခုတည်းဖြစ်အောင် ပေါင်းစည်းပေးသည်။
Set_Union = set_A.union(set_B) # union() သည် return method ဖြစ်သည်။
print(Set_Union) # {1, 2, 3, 4, 5, 7, 9, 11}

# Intersetion သည် အစုနှစ်ခုထဲ့မှ တူညီတဲ့ အရာကို ပေါင်းစပ်ပေးသည်။
Set_Interset = set_A.intersection(set_B)
print(Set_Interset) # {1, 2, 4, 9}
Set_Interset = set_B.intersection(set_A)
print(Set_Interset) # {1, 2, 4, 9}

# Different သည် ခြားနားခြင်းဖြစ်သည်။
# set_A ထဲ့က အရာက set_B ထဲ့က အရာနဲ့ မတူတဲ့ အရာကို ထုတ်ပြပေးတယ်။
Different_set = set_A.difference(set_B)
print(Different_set) # {11, 7}
# set_B ထဲ့က အရာက set_A ထဲ့က အရာနဲ့ မတူတဲ့ အရာကို ထုတ်ပြပေးတယ်။
Different_set = set_B.difference(set_A)
print(Different_set) # {3, 5}