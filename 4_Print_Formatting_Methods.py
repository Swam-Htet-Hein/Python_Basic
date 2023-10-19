# \n ==> new line
# \t ==> tab
print('Good Morning,\nHello\nI am Swam')
print('Hello\tworld')
print('Heading\n\tThis is paragraph')

print('I can\'t sleep well') # Escape \

# Print Formatting 3 methods
# Methods one

# %d is for int
# %s is for string
# %f is for float
# %f ရှေ့က .2 သည် ဒဿမနေရာ သတ်မှတ်ခြင်းဖြစ်သည်။
# %b is for boolean
print('I have %.2f%s' %(99.55, '$'))
name = 'Swam Htet Hein'
age = 21
score = 99.55
print('Hello, I\'m %s. I\'m %d years old. My score is %.2f.' %(name, age, score))

# Method two

print('Hello, I am {}. I am {}. My score is {}'.format(name, age, score))
# Index numbers in format method starts with 0
print('Hello, I am {1}. I am {2}. My score is {0}'.format(name, age, score))
# Variable name ကို အထဲမှာ ကြေညာပြီး format method နဲ့ assign လုပ်တယ်။
print('I live in {place}. I have {possess}.'.format(place="Mandalay", possess="Car"))

# Method three (popular these days)

print(f'Hello, My name is {name}. I am {age} years old. My score is {score}.')

# Summary
# Method 1 - Just like C Programming use % inside of print and assign outside of print.
# Method 2 - Use format method to assign.
# Method 3 - Popular these days, use f before ''.