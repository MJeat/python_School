# Insertion sort: 
#Insertion sort is a simple sorting algorithm. Here's how it works:

#It starts with the second element and compares it with the first.
#If the second element is smaller, it's placed before the first.
#Then, it moves to the third element, compares it with the first and second, and places it in the correct position among them.
#This process continues for each element, ensuring that each new element is inserted into its proper place among the already sorted elements.
#Finally, the array is sorted.


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
arr = [64, 25, 12, 22, 11]
insertion_sort(arr)
print("Sorted array is:", arr)

