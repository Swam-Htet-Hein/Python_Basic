# အကယ်၍ Local မှာ Local variable ရှိလျက်သားနဲ့ မသုံးချင်ဘူး Global variable ပဲသုံးချင်ရင် keyword 'global' သုံးပြီ၊ ကိုယ်သုံးချင်တဲ့ Global vaiable name ကို ရေးရုံပဲ။

Subject = 'Python' # Global variable

def study ():
    global Subject
    print(f"I am studying {Subject}")
    Subject = 'C++' # ခေါ်သုံးထားတဲ့ Global variable ကို overwrite လုပ်ရင် Local အပြင်ဘက်မှာပါ သက်ရောက်တယ်။

study()
print(f"I am studying {Subject}")

# Local to Global လုပ်ချင်ရင် တော့ Local function ကို return ပြန်မှပဲရမယ်။

# function parameter တွေသည်လည်း Local variable တွေဖြစ်တယ်။
def weather(temp):
    print(f"It's {temp}deg Cel outside.")

weather(35.9)
# print(temp) NameError: name 'temp' is not defined