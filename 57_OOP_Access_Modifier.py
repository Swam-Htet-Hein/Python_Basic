"""
    Access modifiers in Python are a way to control the visibility and accessibility of class members.
    There are three types of access modifiers in Python:
    (public(default), protected and private)
"""

class person:
    def __init__(self, name, age, id) -> None:
        # name, age ရဲ့ရှေ့မှာဘာမှမထားထားရင်default အနေနဲ့ public variable တွေဖြစ်တယ်။
        self.name = name
        # varible ကို protected ပြောင်းချင်ရင် single underscore(_) ချရမယ်။
        self._age = age
         # variable ကို private ပြောင်းချင်ရင် variableရှေ့မှာ double underscore(__) ချရမယ်။
        self.__id = id
        # __id သည် private ဖြစ်သွားတဲ့အတွက် class အတွင်းမှာသာ ယူသုံးလို့ရတော့သည်။
    def status(self):
        print(f"Name:{self.name} | Age:{self._age} | ID:{self.__id}")
    
    # private variable လည်းရှိသလို၊ private methods တွေလည်းရှိသည်။
    def __birth_year(self):
        current = 2023
        return current - self._age
    # private methods တွေကိုလည်း getter, setter တွေသုံးပြီး access လုပ်ရသည်။
    def get_birth_year(self):
        print(self.__birth_year())

"""
    public(default) - class အတွင်းမှာရော၊ အပြင်မှာရော ကြိုက်သလိုသုံးလို့ရသည်။
    private(double underscore) - class ရဲ့ private property ဖြစ်တဲ့အတွက် class အတွင်းမှာပဲသုံးလို့ရသည်။
    protected(single underscore) - class အတွင်းမှာရော၊ class ကနေအမွေဆက်ခံထားတဲ့ child class မှာရောသုံးလို့ရသည်။
    အပြင်မှာလည်းပဲသုံးလို့ရသည်။ သို့သော် အလေ့အကျင့်ကောင်းမဟုတ်တဲ့အတွက် မသုံးသင့်ပါ။
"""
class student(person):
    def show_status(self):
        print(f"Name:{self.name} | Age:{self._age}") # ID:{self.__id}

first = person('Aung Kyaw', 21, '#330')
# public variable တွေကိုအပြင်မှာကြိုက်သလိုသုံးလို့ရသည်။
# print(first.name)
# print(first.age)
# print(first.id)
# private variable တွေကိုတော့ getter, setter ကနေပဲသုံးလို့ရသည်။
first.status()
# first.__birth_year() private method တွေကို တိုက်ရိုက်သုံးမရတော့။ 
first.get_birth_year()

second = student('Mya Mya', 18, "#898")
second.show_status() # __id သည် private variable ဖြစ်တဲ့အတွက် access မဖြစ်ပါ။
second.get_birth_year() # ____birth_year() သည်လည်း private method ဖြစ်တဲ့အတွက် access မဖြစ်ပါ။