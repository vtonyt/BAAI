#
# Vinh Tony
# 2024/11/06
# standard deviation
#

def my_sd(input):
    print(f'Input: {input}')
    lenght = len(input)
    sum = 0
    output = 0
    mean = statistics.mean(input)
    print(f"Mean : {mean}")
    for x in input:
        sum += (int(x) - mean)**2
    sum = sum /lenght
    output = math.sqrt(sum)
    return output

answer = my_sd([1,2,3])
print(f'Answer: {answer}')