def merge_sorted_arrays(arr1, arr2):
    merged = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged

# Example
size1 = int(input("Enter the size of the first array: "))
arr1 = list(map(int, input("Enter the elements of the first array separated by space: ").split()))

size2 = int(input("Enter the size of the second array: "))
arr2 = list(map(int, input("Enter the elements of the second array separated by space: ").split()))

merged_array = merge_sorted_arrays(arr1, arr2)

print("Merged sorted array:", merged_array)
