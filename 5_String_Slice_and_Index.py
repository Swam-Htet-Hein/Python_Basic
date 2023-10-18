name = "Swam Htet"
address = "Mandalay"
# String ဆိုတာ characters တွေကို စုစည်းထားတဲ့ အရာဖြစ်တယ်။
# string_name[index start with zero]
print(name[0], end='')
print(name[1], end='')
print(name[2], end='')
print(name[3], end=' ')

print(name[5], name[6], name[7], name[8])

# Index slicing (slice method)
lists = "Coffee Milk Sugar"

print(lists[0:6]) # The last one is exclusive
print(lists[7:11])
print(lists[12:17])
print(lists[0:6:1]) # this is default step
print(lists[0:6:2]) # start : end : step
print(lists[-1]) # when you use minus, it will reverse the string
print(lists[-10:-6]) # can also use reverse method to slice
print(lists[-17:-11])
print(lists[0:-6])
print()
print(lists[:]) # just put colon to show all characters
print(lists[7:]) # start from the index you've selected
print(lists[:6]) # reverse from the index you've selected remember the exclusive number
print()
print(lists[::]) # take default step
print(lists[::2]) # take 2 steps all the string
print(lists[::-1]) # take 1 oppsite step to all string
reverse = lists[0:6]
print(reverse[::-1]) # if you want to take a reverse step you've selected use this.