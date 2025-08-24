# Quick sort: is a sorting algorithm that repeatedly selects a pivot element to partition the array into two parts, with elements less than the pivot on one side and elements greater than the pivot on the other, then recursively sorts the sub-arrays.

# Quick sort is indeed one of the most popular and widely used sorting algorithms due to its efficiency and simplicity. It is often preferred for its average-case time complexity of 
#𝑂(𝑛log𝑛), which is very efficient for large datasets. 

#Additionally, quick sort is an in-place sorting algorithm, meaning it does not require extra space proportional to the size of the input array, which is another advantage.




# We need to set the pivot. Any number or data within the array.


# Time Complexity
#Average Case: 
    #𝑂(𝑛log⁡𝑛)
    #O(nlogn)
#Worst Case: 
    #𝑂(𝑛2)
    #O(n 2) (This occurs when the smallest or largest element is always chosen as the pivot, leading to unbalanced partitions.)



#---------------------------------------------------------
def quicksort(arr):
    if len(arr) <= 1:   # This means that if within the array, 
                            # there is none or 1 element or value, just return that value immediately cuz there's no need to sort when there's none or one element. 
                                # so if you dont say this block of code, it will gives error when there is no element or one element 
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Choosing the middle element as the pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort(arr)
print(sorted_arr)

#----------------------------------------------------------------
print("----------------------------------------------------------------")
# Exercise1: 




def quick_sort(arr2):
    if len(arr2) <= 1:
        return arr2
    else:
        pivot_point = arr2[len(arr2)//2] # If you change pivot_point = arr2[len(arr2)//2] to pivot_point = len(arr2)//2, you are calculating the middle index of the array but not selecting the corresponding element,
                                            #which is not what you want. You need to use arr2[len(arr2)//2] to select the actual pivot element from the array arr2.
                                                # The result from this line is the index of a value to be the pivot point
        left = [x for x in arr2 if x < pivot_point]
        mid = [x for x in arr2 if x == pivot_point]
        right = [x for x in arr2 if x > pivot_point]
        return quick_sort(left) + mid+  quick_sort(right)
    





array = [3, 6, 8, 10, 1, 2, 1]
sorted_array = quick_sort(array)

print(sorted_array)

#----------------------------------------------------------------
print("----------------------------------------------------------------")
# Exercise2: 

def quicksort2(arrr):
    if len(arrr) <= 1:
        return arrr
    else:
        pivott = arrr[len(arrr)//2]
        leftt = [y for y in arrr if y < pivott]
        midd = [y for y in arrr if y == pivott]
        rightt = [y for y in arrr if y > pivott]
        return quicksort2(leftt) + midd + quicksort2(rightt)


arrayy = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
print(quicksort2(arrayy))


#----------------------------------------------------------------
print("----------------------------------------------------------------")


#Note that the recursion method including quick method is not only used for numbers, but can only use for words and letters. It will be sorted alphabetically.
