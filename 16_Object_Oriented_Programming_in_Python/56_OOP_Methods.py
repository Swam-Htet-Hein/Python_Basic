# Instance Methods
# Class Methods
# Static Methods

# Methods တွေထဲမှာ code တွေကို စီစဉ်ရေးဆွဲပြီး အသုံးပြုလို့ရအောင်လုပ်တာကို Implementationလုပ်တယ် လို့ခေါ်တယ်။ 

class student:
    # University Name # Class Variable
    uni_name = "PKU-TU"

    def __init__(self, name, age, year):
        self.name = name
        self.age = age
        self.year = year
        
    # Instance Methods သည် instance variable ကို အသုံးပြုပြီး တွက်ချက်တာ၊ အသုံးပြုတာ လုပ်သည်။
    # Instance Methods တွင် self ပါကိုပါရမည်။
    def status(self):
        print(f"Name : {self.name} | Age : {self.age} | Year : {self.year}")

    # Instance Methods ကို ယူပြီး ပြုပြင်ပြောင်းလည်းတာတွေ လုပ်လို့ရသည်။
    # Getter and Setter လို့ခေါ်သည်။
    # Setter သည် ပြုပြင်ချိန်ညှိ့သည်။ Getter သည် ထုတ်ယူပြသည်။
    def set_age(self, age):
        # Setter သည် အခြေအနေတွေပေါ်မှုတည် ပြီးပြုပြင်ပြောင်းလည်းမှုလည်းလုပ်နိုင်သည်။
        if age > 17:
            self.age = age
            print("Successful change")
        else:
            print("Invalid Age")
    # Getter သည် လည်းအခြေအနေတွေ၊ အစီအစဉ်တွေပေါမှုတည်ပြီး ထုတ်ပြတာတွေလုပ်လို့ရတယ်။
    def get_name(self, admin):
        if admin == True:
            return self.name
        else: 
            return "Sorry, You have no right to see this."
        
    # Class Methods သည် class variable တွေကို အသုံးပြုတဲ့ Method ဖြစ်တယ်။
    @classmethod
    def set_uni_name(cls, uni_name):
        cls.uni_name = uni_name
        print("Changed Success")

    # Static Methods သည် Instance variable ကော၊ Class variable ကော မသုံးပဲ၊ သူတစ်ခုတည်းရပ်တည်တယ်။
    @staticmethod
    def static_method(greet):
        print(greet)

std1 = student("Aung Kyaw", 18, "1st year")
std2 = student("Mya Mya", 19, "2nd year")

std1.status()
std2.status()

std1.set_age(-12)
std1.status()

print(std1.get_name(True))
print(std2.get_name(False))

student.set_uni_name("YTU")
print(student.uni_name)
print(std1.uni_name)
print(std2.uni_name)

student.static_method("Nice to meet you!")
student.static_method("Hello")