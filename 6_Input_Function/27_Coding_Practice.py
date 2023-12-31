# TODO 1 : ask users length
# TODO 2 : ask users height
# TODO 3 : convert length and height to int cause it's str
# TODO 4 : calculate area of square
length = int(input('Enter length: '))
height = int(input('Enter height: '))
area = length * height
print('The area of square is {}'.format(area))

# BMI Calculator
weight = float(input('Enter you weight (pound) : '))
height = float(input('Enter your height (feet) : '))

BMI = (weight * 703) / ((height*12)*(height*12))

if BMI < 18.5 :
    print("Your BMI is %.2f and you are underweight! Eat More!" %BMI)
elif BMI >= 18.5 and BMI <= 24.9 :
    print("Your BMI is %.2f and you are in good shape! Good Work!" %BMI)
elif BMI > 25 :
    print("Your BMI is %.2f and you are overweight! Eat Less!" %BMI)
else:
    print('Somethings went wrong, please try again!')