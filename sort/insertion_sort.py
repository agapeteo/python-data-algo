def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


test_arr = [9, 1, 4, 7]
insertion_sort(test_arr)

print(test_arr)
