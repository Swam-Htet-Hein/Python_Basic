# Special Methods for classes
# __init__ constructor
# __str__ object ကို တိုက်ရိုက်ယူသုံးတဲ့အခါ ကိုယ်ထုတ်ပြစေချင်တဲ့ string ကိုပြပေးတယ်။
# __len__ object ကို len() သုံးလိုက်တဲ့အခါ ဘာကိုဖော်ပြချင်သလဲဆိုတာ သတ်မှတ်လို့ရတယ်။
# __dir__ class အတွင်းမှာရှိတဲ့ user-defined variable, methods တွေ၊ built-in variable, methods တွေကို ပြတယ်။
# __eq__ object နှစ်ခုကိုစစ်ဆေးရာမှာ ဘယ်ဟာကိုစစ်ပြီး၊ ဘယ်ဟာကိုတော့မစစ်ရဘူးလို့ သတ်မှတ်လိုက်တယ်။
class Book:
    def __init__(self, name, author, pages) -> None:
        self.name = name
        self.author = author
        self.pages = pages
    
    def display_info(self):
        print(f"Name:{self.name}|Author:{self.author}|Pages:{self.pages}")

    def __str__(self):
        return f'The name of the book is {self.name}'

    def __len__(self):
        return self.pages
    
    def __eq__(self, others):
        if self.name == others.name and self.author == others.author:
            return True
        else:
            return False

book1 = Book('Monte Cristo', 'IDK', 200)
# print(book1) # <__main__.Book object at 0x000001A5BED72D10>
print(book1) # The name of the book is Monte Cristo

book2 = Book("I don't care", 'IDK', 100)
print(book2) # The name of the book is I don't care

print(len(book1)) # 200
print(len(book2)) # 100

print(book1.__dir__())
print(type(book1.__dir__())) # <class 'list'>

book3 = Book('Hello', 'Jhon', 300)
book4 = Book('Hello', 'Jhon', 400)
print(id(book3))
print(id(book4))
# print(book3 == book4) # False # default special method အတိုင်းသာ ညီပြရမယ်ဆိုရင် memory address နဲ့ပဲ နှိုင်းယှဉ်ကြလိမ့်မယ်။
# overloading လို့ခေါ်တဲ့ default special method တွေကို ကိုယ်တိုင်ပြုပြင်ပြောင်းလဲခြင်း လုပ်လို့ရတယ်။
print(book3 == book4) # True (default ကို ပြုပြင်ပြောင်းလဲလိုက်တဲ့အတွက် operator(==) က name နဲ့ author ကိုပဲ စစ်ဆေးတော့တာ။)
