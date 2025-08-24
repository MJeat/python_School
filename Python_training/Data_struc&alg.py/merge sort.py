# merge sort: is a way to sort a list by splitting it into smaller lists, sorting those, and then merging them back together in order.
# runtime complexity: O(n logn)


# Example with a Small Pile of Cards
#Let's say you have these cards: [5, 3, 8, 1, 2, 7, 4, 6].

#Divide: Split the pile into smaller and smaller piles:

#[5, 3, 8, 1, 2, 7, 4, 6]
#[5, 3, 8, 1] and [2, 7, 4, 6]
#[5, 3] and [8, 1] and [2, 7] and [4, 6]
#[5] and [3] and [8] and [1] and [2] and [7] and [4] and [6]
#Sort and Combine:

#Compare [5] and [3]. Combine them into [3, 5].
#Compare [8] and [1]. Combine them into [1, 8].
#Compare [2] and [7]. Combine them into [2, 7].
#Compare [4] and [6]. Combine them into [4, 6].
#Now you have [3, 5], [1, 8], [2, 7], and [4, 6].
#Compare [3, 5] and [1, 8]. Combine them into [1, 3, 5, 8].
#Compare [2, 7] and [4, 6]. Combine them into [2, 4, 6, 7].
#Finally, compare [1, 3, 5, 8] and [2, 4, 6, 7]. Combine them into [1, 2, 3, 4, 5, 6, 7, 8].


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    # Compare elements from both halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # If there are remaining elements in the left half, add them
    while i < len(left):
        sorted_arr.append(left[i])
        i += 1

    # If there are remaining elements in the right half, add them
    while j < len(right):
        sorted_arr.append(right[j])
        j += 1

    return sorted_arr

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
