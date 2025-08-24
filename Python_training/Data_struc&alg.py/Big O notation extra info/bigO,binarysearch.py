# Binary search: is a search algorithm that finds the position of a target value within a sorted array. 
# half of the array is eliminated during each "step". 

# Binary search is great with large elements, large data set

# runtime complexity: O(log n)
# The more and more data set, the more efficient. Cuz we divide the array by half. Every time we divide, it makes it easier for us to iterate smaller proportion. Finally, find our target value.



# First, we begin in the middle.
# Then, we check to see if our value is indeed in the middle or not, which is rly rare.
    #After that, we check whether our target value is greater or lesser than the middle value that we chose. Then, eliminate the half part that we no need. 
# Third, we have half. Half the half we got. LOL

#  Is our target greater or lesser than the middle that we choose?
#Eliminate the half we dont need

#---------------------------------------------------------------------------------------------
# It is recommended to use function for binary search such as:


def binary_search (sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1           #Minus 1 is to tell python to start at zero (begin_index)

    while begin_index <= end_index:
        midpoint =  (end_index+begin_index)//2      # Position
        midpoint_value = sequence[midpoint]         # Retrieve the midpoint_value
        
        if midpoint_value == item:
            return midpoint             # return the position of the midpoint
        
        elif item < midpoint_value:         # Ignore the right half
            end_index = midpoint -1   

        else:       # Ignore the left half
            begin_index = midpoint +1


    return None         # In case there is no value within the array or list
    
sequence_a = [1,2,3,4,5,6,7,8,9]
item_a = 3

print(binary_search(sequence_a,item_a))  # The number in the output is the index or the location of the target value within the array
      
#--------------------------------------------------------------------------
# If you dont use function, (which will be harder if you need to use binary search frequently) use this straight forward method:

sequence_b = [1,2,3,4,5,6,7,8,9]
sequence_b.sort() # Need this when there is zero at the back
target = 4


start_from = 0 
end = len(sequence_b)-1

result = -1

while start_from<= end:
    mid_point = (start_from + end)//2
    mid_point_val = sequence_b[mid_point] # try to delete this. wanna see what's gon happen

    if mid_point_val == target:
        result = mid_point
        print('Target found!')
        break
    elif mid_point_val < target:
        start_from = mid_point + 1 
        
    else:
        end = mid_point -1

else:
    result = -1     # In the context of binary search, 
                    #the value result = -1 serves as a sentinel value to indicate that the target element was not found in the array.
            

print(f'Target {target} found at index: {result}')



#---------------------------------------------------------------------------------------------------------------------------
print("---------------------------------------------------------------------------------------------------------------------------")
#Exercise:
# This should return 5,6,7 as indices containing number 15 in the array



def binary_search2(sequences, target):
    begining = 0
    ending = len(sequences) - 1
    result = []

    while begining <= ending:
        middle = (begining + ending) // 2
        middle_val = sequences[middle]

        if target == middle_val:
            # Find all occurrences of the target by checking left and right from the middle
            left = middle
            right = middle
            while left >= 0 and sequences[left] == target:
                result.append(left)
                left -= 1
            while right < len(sequences) and sequences[right] == target:
                if right != middle:  # To avoid adding middle twice
                    result.append(right)
                right += 1
            result.sort()  # Ensure the result is in sorted order
            return result  # Return the list of indices

        elif target < middle_val:
            ending = middle - 1
        else:
            begining = middle + 1

    return None

numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
number_to_find = 15

print(binary_search2(numbers, number_to_find))  # This should return [5, 6, 7]






