#
# Vinh Tony
# Repeat three times
#

max_lap = 3  # Maximum number of repeatition
curr_lap = 1

while (curr_lap <= max_lap):
    # 1. Input
    n1 = int(input("Number 1: "))
    n2 = int(input("Number 2: "))
    
    # 2. Process
    if n1 > n2:
        bigger = int(n1)
    elif n1 < n2:
        bigger = int(n2)
    else:
        bigger = "same"
    
    # 3. Output
    print(f"Bigger : {bigger}")
    
    curr_lap += 1
