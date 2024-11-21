
import numpy as np

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)

# Create a numpy array
array = np.array([4, 5, 6, 7, 8, 9, 10])

# Call the bubble_sort function
bubble_sort(array)
