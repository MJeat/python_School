# Interpolation search: improvement over binary search best used for sorted "uniformly" distributed data. 

            # Uniformly distributed: [1,2,3,…,998,999,1000]
            # Non-uniformly distributed: [1,2,2,2,3,10,50,1000]

# It makes educated guess on where the value might be on the calculated probe results
# If probe is incorrect, we narrow the search and try again, and a new probe is calculated

# Imagine you have a row of jellybeans numbered from 1 to 100, and you need to find the jellybean with the number 50. Here’s how interpolation search makes its guess:

#Looking at the Ends: It starts by looking at the jellybeans at the beginning (number 1) and the end (number 100) of the row.
#Using the Numbers: Knowing the jellybeans are numbered from 1 to 100, it guesses that the jellybean with the number 50 is somewhere in the middle. 
    #But it doesn't just guess the exact middle (like binary search). Instead, it estimates the position based on how far 50 is from the numbers at the ends.


#average case: 0(log (log(n)))
# Worst case: 0(n) [values increase exponentially]


def interpolation_search(sequences, target):
    begin = 0
    end = len(sequences) - 1
    
    while begin <= end and sequences[begin] <= target <= sequences[end]:
        probe_position = begin + int((end - begin) * ((target - sequences[begin]) / (sequences[end] - sequences[begin])))
        
        if sequences[probe_position] == target:
            return probe_position
        elif sequences[probe_position] < target:
            begin = probe_position + 1
        else:
            end = probe_position - 1
    
    return -1

sequences = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 4
result = interpolation_search(sequences, target)
if result != -1:
    print(f'Element is found at index {result}')
else:
    print("Nothing is found.")

#----------------------------------------------------------------------
print("----------------------------------------------------------------------")
# Exercise 1:

def interpolation_search2(array, target2):
    begin = 0
    end = len(array)- 1 

    while begin <= end and array[begin] <= target2 <= array[end]:
        probe = begin + int((end - begin) * (target2 - array[begin]) / (array[end] - array[begin]))


        if array[probe] == target2:
            return probe
        elif array[probe] < target2:
            begin = probe + 1

        else:
            end = probe -1 
    return -1 

test = [
        ([1,2,3,4,5,6,7,8,9],8),
        ([10,20,30,40,50,60,70,80,90], 70),
        ([3, 6, 9, 12, 15, 18, 21], 3)
        ]


for array, target2 in test:
    result2 = interpolation_search2(array, target2)
    print(f"Searching for {target2} in {array}: Index {result2}")


#----------------------------------------------------------------------
print("----------------------------------------------------------------------")
# Exercise 2:
# Interpolation Search with Edge Cases
# Task:
# Enhance the interpolation search algorithm to handle additional edge cases, such as lists with all identical elements and lists where the target value is not within the range of the list values. 
# Write a function that performs the search and returns the index of the target value if found, or -1 if not found.

def interpolation_search3(array3, target3):
    begining = 0
    ending = len(array3)-1 

    while begining <= ending and array3[begining] <= target3 <= array3[ending]:

        #Use this block of code when its edge cases:
        #-------------------------------------
        if array3[begining] == array3[ending]:
            if array3[begining] == target3:
                return begining
            else:
                return -1
        #-------------------------------------



        pos = begining + int((ending-begining)*(target3-array3[begining])/(array3[ending]-array3[begining]))

        if array3[pos] == target3:
            return pos 
        elif array3[pos] < target3:
            begining = pos + 1
        else:
            ending = pos -1 
    return -1

test_cases_with_edge_cases = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 4),   # Target within range
    ([10, 10, 10, 10, 10], 10),         # All elements identical
    ([100, 200, 300, 400, 500], 600),   # Target outside range
    ([5, 15, 25, 35, 45, 55, 65], 65),  # Target at the end
    ([20, 30, 40, 50, 60], 15)          # Target below the range
]

for array3, target3 in test_cases_with_edge_cases:
    result3 = interpolation_search3(array3, target3)

    print(f"Searching for {target3} in {array3}: Index: {result3}")

        