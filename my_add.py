#
# Vinh Tony
#2024/11/06
# my_add function to add all numbers in a list
#

# dEFINE FUNCTION
def my_add(input):
    sum = 0
    for x in input:
        sum += int(x)
    return sum

# 1. Input
input= [10,20,30]

# 2. Process 
answer= my_add(input)

# 3. Output
print(f'Answer {answer}')

# Short way to call function
print(f"Answer {my_add({1,2,3})}")