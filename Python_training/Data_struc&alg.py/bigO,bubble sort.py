



# Bubble sort: 
# It runs in quadratic time O(n^2). it is slow.
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n-i-1): # n-i-1 tells us how many items we still need to check.
            # Traverse the list from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print(arr[i], end=" ")


#------------------------------------------
print("--------------------------------------------")
# However, sort() or sorted() is more efficient and popular when it comes to sorting larger data


num = [1,2,521,47,85,83,45,3,9]

num.sort()
print(num)


# So just use sort() over bubble sort()