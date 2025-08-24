print("# Application 1:")

# Application 1: Conversion from Kilograms to Pounds and Pounds to Kilograms
# Description: Display two conversion tables side by side — one converting kilograms to pounds, and the other converting pounds to kilograms.

kg = 1
pound = 20

print("Kilograms   Pounds   |   Pounds   Kilograms")
while kg < 10 and pound <= 50:
    pounds = kg * 2.2  
    kilograms = pound * 0.45  
    
    print(kg,"          ", f"{pounds:.1f}", "    |   ",pound, "    " ,kilograms)
        # Added extra 5 space in the " ", conversion of kg to pounds
        # Added extra "  " with extra spaces to align between pound and kilograms

    kg += 2 # Added '=' between + and 2 
    pound += 5



# ------------------------------------------------------------------------------------------
print("------------------------------------------------------------------------------------------")
print("# Application 3:")
# ------------------------------------------------------------------------------------------
# Application 3: Count Positive and Negative Numbers and Compute the Average
# Description: The program should count how many positive and negative numbers were input, compute their total, and find their average (excluding zeros). 
    # It stops when 0 is input.

count_positive = 0
count_negative = 0
total = 0
count = 0

while True:
    num = int(input("Enter an integer, the input ends if it is 0: "))
    
    if num == 0: # Added extra "="
        break
    
    if num > 0:
        count_positive += 1
    elif num < 0:
        count_negative += 1
    
    total += num
    count += 1

average = total / count
print("Positive numbers:", count_positive)
print("Negative numbers:", count_negative)
print("Total:", total)
print("Average:", round(average, 2)) # Added round to round up the result of average to 2 decimal numbers 


# ------------------------------------------------------------------------------------------
print("------------------------------------------------------------------------------------------")
print("# Application 4:")
# ------------------------------------------------------------------------------------------
# Application 4: Conversion from Kilograms to Pounds
# Description: Display a table that converts kilograms to pounds (1 kg = 2.2 pounds), starting from 1 and incrementing by 2 (i.e., 1, 3, 5, ...).

kg = 1

while kg <= 20:
    pounds = kg * 2.2  
    print(kg, "     ", round(pounds,2)) # Rounding up pounds result to 2 decimal numbers
    kg += 2  # Added extra "=" between + and 2

