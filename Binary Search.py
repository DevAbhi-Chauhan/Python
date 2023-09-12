def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Element not found

# Example usage:
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7
result = binary_search(sorted_list, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")

# In this binary search implementation:

# 1. We start with left and right indices pointing to the first and last elements of the sorted list.

# 2. In each iteration, we calculate the mid index, which is the middle of the current search range.

# 3. We compare the element at the mid index with the target value:

# 4. If they match, we return the index where the target was found.
## If the element at mid is less than the target, we update left to mid + 1 to search in the right half of the current range.
## If the element at mid is greater than the target, we update right to mid - 1 to search in the left half of the current range.
## We repeat this process until left is greater than right, indicating that the element was not found in the list, and we return -1.