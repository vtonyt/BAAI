#
# Vinh Tony
# Take two number and print bigger one
#
 

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
# Print bigger number
print(f"Bigger : {bigger}")
