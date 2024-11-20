
def find_missing_num(arr, n):
    # Calculate the expected sum of numbers from 1 to n (inclusive)
    total_sum = (n * (n + 1)) // 2
    
    # Calculate the sum of elements in the array
    array_sum = sum(arr)
    
    # The missing number is the difference between the expected total sum and the actual sum
    missing_number = total_sum - array_sum
    
    return missing_number


# Input array with numbers 1 to 10, except 8
arr = [1, 2, 3, 4, 5, 6, 7, 9, 10]

# n is the total count of numbers including the missing one
missing_num = find_missing_num(arr, len(arr) + 1)

print("The missing number is:", missing_num)
print("Length of the array:", len(arr))
print(arr[0])