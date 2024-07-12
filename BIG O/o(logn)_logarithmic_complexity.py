# -*- coding: utf-8 -*-
"""O(logn):Logarithmic complexity.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1k_lYUONYg1ov_8kfhlTZcXbMLWRFmNIp
"""

sorted_list = [4, 8, 10, 14, 27, 31, 42, 52]  # A sorted list of numbers

def binary_search(arr, target):
    left, right = 0, len(arr) - 1  # Initialize the left and right pointers

    while left <= right:  # Continue searching while the search space is valid
        mid = left + (right - left) // 2  # Find the middle index to avoid overflow

        # Check if target is present at mid
        if arr[mid] == target:
            return mid  # Target found at index mid

        # If target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1  # Adjust the left pointer to search in the right half

        # If target is smaller, ignore the right half
        else:
            right = mid - 1  # Adjust the right pointer to search in the left half

    # If we reach here, the element was not present
    return -1  # Target not found in the array

# Example usage
target_number = 42
result = binary_search(sorted_list, target_number)

if result != -1:
    print(f"Element {target_number} found at index {result}")
else:
    print(f"Element {target_number} not found in the array")

