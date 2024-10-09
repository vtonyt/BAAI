#
# Vinh Tony
# grade calculator
#

subjects = 1
n_subjects= int(input("How many subjects do you have? "))
grade_subjects= 0


while(n_subjects>=subjects):
    #Input
    name= input(f'Enter the name of the subject {subjects}: ')
    grade= int(input(f"Enter the grade {name}: "))
    #Process
    grade_subjects+= grade
    subjects +=1   

#Output
print(f'Your average grade is: {round(grade_subjects/(subjects-1))}')