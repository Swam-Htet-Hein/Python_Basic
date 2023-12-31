# Path တွေသည် file လမ်းကြောင်းတွေပေါင်းလို့ရသည်။
import os
current_path = os.getcwd()
print(current_path)
second_path = 'Top_Folder'
final_path = os.path.join(current_path, second_path)
print(final_path)

# os.path မှာလည်းသုံးလို့ရတဲ့ function , method တွေရှိတယ်။
print(os.path.basename(final_path)) # directory တစ်ခုရဲ့နောက်ဆုံး file name ကိုဖော်ပြတယ်။ 
print(os.path.dirname(final_path)) # Top_Folder ရဲ့ အရှေ့ကဟာကို ဖော်ပြတယ်။
print(os.path.exists(current_path)) # ကိုယ်ထည့်လိုက်တဲ့ path က တကယ်ရှိသလားဆိုတာကို ဖော်ပြတယ်။

# os.path ထဲမှာ dir နဲ့ file ရှာတဲ့အခါမှာလည်းအသုံးပြုလို့ရတယ်။
print(os.path.isdir('Top_Folder')) # Top_Folder သည် Folder တစ်ခုဖြစ်တဲ့အတွက် True ပြတယ်။
print(os.path.isfile('Top_Folder')) # Top_Folder သည် File တစ်ခုမဖြစ်တဲ့အတွက် False ပြတယ်။
print(os.getcwd())
print(os.path.isfile('0_Code_Doodle.py')) # .py သည် File တစ်ခုဖြစ်တဲ့အတွက် True ပြတယ်။

print(os.path.splitext(current_path)) # dir and file ကို ခွဲပေးတာဖြစ်ပါတယ်။