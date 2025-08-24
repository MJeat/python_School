# Selection sort: Selection sort is primarily used for educational purposes to understand the basic principles of sorting algorithms. 
#It's a simple algorithm that repeatedly selects the smallest (or largest) element from an unsorted array and swaps it with the first element, until the entire array is sorted. 
#However, in practical applications, more efficient sorting algorithms such as Python's built-in sort() method are preferred.


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage:
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array is:", sorted_arr)
