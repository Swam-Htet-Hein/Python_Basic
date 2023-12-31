import os
# Directory နဲ့ Folder ကို အတူတူမှတ်နိုင်သည်။
# Directory သည် လမ်းကြောင်း(path)ကို ပြောတာဖြစ်ပြီ၊ Folder သည် လမ်းကြောင်းရဲ့ Name ကိုပြောတာဖြစ်သည်။
os.chdir("C:\\Users\\kenwa\\Desktop\\Learn Python\\Top_Folder")
path = os.getcwd()

# Theory
# os.walk(path) သည် ပန်းခြံထဲ နေရာအစုံကို လမ်းလျှောက်တာနဲ့ တူသည်။
# Top Folder ကို ပန်းခြံတစ်ခုလို့ သတ်မှတ်ကြည့်မယ်။
# Top Folder ထဲမှာ Directories(Folders) တွေ၊ Files တွေရှိတယ်။
# အဲဒီ Folders, Files တွေကို အရင်ကြည့်တယ်။
# အကုန်ကြည့်ပြီးရင် Folders နဲ့ Files နှစ်ခုထဲကမှ Folderတွေထဲကို ဝင်ကြည့်ပြန်တယ်။
# အဲဒီ Folder တစ်ခုချင်းစီမှလည်း Folders တွေ၊ Files တွေ ထပ်ရှိပြန်ရင်လည်း Files တွေကို ကြည့်ပြီး Folder တွေထဲကိုဝင်ကြည့်ပြန်တယ်။
# ဒါကြောင့် နာမည်က walk ဖြစ်တယ်။

# Practical
# (Current Directory, Directories(Folders), Files) ဆိုပြီး tuple data-type နဲ့ store ပြီးပြန်ထုတ်တယ်။
# အဲ့ဒါကို Unpack လုပ်ပြီး For loop ကို အသုံးချရမယ်။
# Path ရဲ့ ထိဆုံးက Folder မှာရှိတဲ့ Directories တွေ၊ Files တွေကို ထုတ်ပြတယ်။
# ပြီးရင် Directories တွေထဲက Folders တွေ၊ Files တွေကို ထပ်ထုတ်ပြတယ်။
# ထပ်ရှိသေးရင် အဲ့ဒီFolders ထဲက File တွေကို ထပ်ထုတ်ပြပြန်တယ်။
# Current Directory ရဲ့အထဲမှာရှိတဲ့ Folders , files တွေကို list အနေနဲ့ ထုတ်ပြတယ်။
for current, directories, files in os.walk(path):
    print()
    print(f"Current Directory : {current}")
    print(f"Directories : {directories}")
    print(f"Files : {files}")
    print()

"""

Current Directory : C:\Users\kenwa\Desktop\Learn Python\Top_Folder
Directories : ['sub1', 'sub2', 'sub3']
Files : ['text1', 'text2']


Current Directory : C:\Users\kenwa\Desktop\Learn Python\Top_Folder\sub1
Directories : ['sub_sub']
Files : ['sub_text1', 'sub_text2', 'sub_text3']


Current Directory : C:\Users\kenwa\Desktop\Learn Python\Top_Folder\sub1\sub_sub
Directories : []
Files : ['Hello']


Current Directory : C:\Users\kenwa\Desktop\Learn Python\Top_Folder\sub2
Directories : []
Files : []


Current Directory : C:\Users\kenwa\Desktop\Learn Python\Top_Folder\sub3
Directories : []
Files : []

"""