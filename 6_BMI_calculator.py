#
# Vinh Tony
# 2024/11/06
# BMI calculator
#
 
while True: 
    weight= float(input('Enter your weight: '))
    height= float((input('ENter your height in meters: ')))
    
    bmi= weight / height**2
    
    print(f'Your BMI is: {bmi}')
    
    answer= input('Continue? (yes/no): ')
    if answer == "no": 
        break

 
 