# Dictionary comprehension သည် list comprehension အတိုင်းပဲ code line တွေအများကြီး ရေးရမဲ့ အစား code line နည်းနည်းနဲ့ run လို့ရအောင်လုပ်ပေးတယ်။
# {expression for member in iterable-obj}
# expression နဲ့ member သည် key, value ဖြစ်ရမည်။
exam_results = {
    'Swam': 100,
    'Kyaw': 60,
    'Myat': 35,
    'SuSu': 90,
    'Paing': 40
}
# ဘာmethod မှမသုံးဘဲ exam_results ပဲသုံးရင် key တန်ဖိုးပဲထုတ်ပေးမှဖြစ်တဲ့ အတွက် .items() ကိုသုံးပေးရတယ်။
copy_exam_result = {
    name : mark for name, mark in exam_results.items()
#   expression  for members    in iterable-obj
}
print(copy_exam_result) # {'Swam': 100, 'Kyaw': 60, 'Myat': 35, 'SuSu': 90, 'Paing': 40}

over_40_mark = {
    name : mark for name, mark in exam_results.items() if mark > 40
#   expression  for members    in iterable-obj       if condition
}
print(over_40_mark) # {'Swam': 100, 'Kyaw': 60, 'SuSu': 90}

moderate_mark = {
    name : mark + 10 for name, mark in exam_results.items() if mark < 40
#   modified exp;    for members    in iterable-obj         if condition
}
print(moderate_mark) # {'Myat': 45}

import random
names = ['Swam', 'Kyaw', 'Myat', 'Thu']
exam_results = {
    name : random.randint(1, 100) for name in names
}
print(exam_results)