def bubble_sort(arr):
    is_sorted = False
    last_unsorted = len(arr) - 1
    while not is_sorted:
        is_sorted = True
        for i in range(last_unsorted):
            if arr[i + 1] < arr[i]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
        last_unsorted -= 1


test_arr = [9, 1, 4, 7]
bubble_sort(test_arr)

print(test_arr)
