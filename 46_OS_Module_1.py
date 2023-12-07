import os
# 1
# getcwd() get current working directory
# print(os.getcwd())
# return

# 2
# chdir(path) change directory
# os.chdir('C:\\Users\\kenwa\\Desktop')
# no return

# 3
# listdir() list directory
# os.chdir('C:\\Users\\kenwa\\Desktop')
# print(os.listdir()) # show current directory items
# return

# 4
# mkdir(path) Make directory (top folder)
# os.chdir('C:\\Users\\kenwa\\Desktop')
# os.mkdir('Testing_folder') # create folder in current directory
# print(os.listdir())
# no return

# 5
# makedirs(paths) Make directories (root folders)
# os.chdir('C:\\Users\\kenwa\\Desktop')
# os.makedirs('Books\\English\\Grammar_Books') # create from top to root folders in current directory
# print(os.listdir())
# no return

# Folder တွေကို ဖျက်တဲ့အခါ သတိထားပါ။ Recycle Bin ထဲ့ကို ရောက်မနေဘဲ့ အပြီးဖျက်သွားလို့ပါ။

# 6
# rmdir(folder) Remove directory (can remove only one)
# os.chdir('C:\\Users\\kenwa\\Desktop')
# os.rmdir('New folder') # Remove folder in current directory
# print(os.listdir())
# no return

# 7
# removedirs(folders) Remove directories (can remove from top to root)
# os.chdir('C:\\Users\\kenwa\\Desktop')
# os.removedirs("Books\\English\\Grammar_books") # Remove folders from top to root in current directory
# print(os.listdir())
# no return

# 8
# rename(old, new) Rename directory
# os.chdir('C:\\Users\\kenwa\\Desktop')
# os.rename('Test', 'Test2') # Rename folder exists in current directory
# print(os.listdir())
# no return