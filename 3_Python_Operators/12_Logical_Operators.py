# Logical Operators (and, or, not)
# 'and' and 'or' are In-fix operators which mean they have two operands
# 'not' is Pre-fix operator also known as unary operator

# AND table
# False and False ==> False
# False and True ==> False
# True and False ==> False
# True and True ==> True
# AND only True when two operands are True
is_18 = True
have_experience = True
got_job = is_18 and have_experience
# အသက်၁၈နှစ်လည်းပြည့်ရမယ်၊ လုပ်သက်အတွေ့အကြုံလည်းရှိရမယ်။
print(f'Did they hire you? : {got_job}')

# OR table
# False or False ==> False
# False or True ==> True
# True or False ==> True
# True or True ==> True
# OR True when one of two operands is True
is_student = True
have_coupon = False
got_promotion = is_student or have_coupon
# ကျောင်းသား၊သူ ဖြစ်သလား၊ ကူပွန်ရှိသလား။ နှစ်ခုထဲက တစ်ခုဖြစ်ရမယ်။
print(f'Did you get the promotion? : {got_promotion}')

# NOT table
# not False ==> True
# not True ==> False
Yes = True
No = False
# True နဲ့ False ကို ပြောင်းပြန်လှန်လိုက်တာပါ။
print(not Yes) 
print(not No)