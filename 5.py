def lower_bound(arr, x):
    low = 0
    high = len(arr)

    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] < x:
            low = mid + 1
        else:
            high = mid
    return low


def upper_bound(arr, x):
    low = 0
    high = len(arr)

    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] <= x:
            low = mid + 1
        else:
            high = mid
    return low


def is_present(arr, x):
    lb = lower_bound(arr, x)
    return lb < len(arr) and arr[lb] == x


# Example
sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17]
x = 7

print("Lower Bound of", x, ":", lower_bound(sorted_array, x))
print("Upper Bound of", x, ":", upper_bound(sorted_array, x))
print(x, "is present in array:", is_present(sorted_array, x))
