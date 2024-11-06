#
# Vinh Tony
# 2024/11/06
# calculate interest
#

# 1. Function
def calculate_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

# 2. Call function
y = calculate_interest(1000, 5, 2)

# 3. Output
print("The interest is:", y)