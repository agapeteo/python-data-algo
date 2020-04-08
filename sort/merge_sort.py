def merge(input_list, tmp_list, low_idx, mid_idx, high_idx):
    for i in range(low_idx, high_idx + 1):
        tmp_list[i] = input_list[i]

    left_idx = low_idx
    right_idx = mid_idx + 1
    cur_idx = left_idx

    while left_idx <= mid_idx and right_idx <= high_idx:
        if tmp_list[left_idx] <= tmp_list[right_idx]:
            input_list[cur_idx] = tmp_list[left_idx]
            left_idx = left_idx + 1
        else:
            input_list[cur_idx] = tmp_list[right_idx]
            right_idx = right_idx + 1
        cur_idx = cur_idx + 1

    remaining = mid_idx - left_idx
    for i in range(0, remaining + 1):
        input_list[cur_idx + i] = tmp_list[left_idx + i]


def merge_sort_range(input_list, tmp_list, low_idx, high_idx):
    if low_idx >= high_idx:
        return

    mid_idx = low_idx + (high_idx - low_idx) / 2
    merge_sort_range(input_list, tmp_list, low_idx, mid_idx)
    merge_sort_range(input_list, tmp_list, mid_idx + 1, high_idx)

    merge(input_list, tmp_list, low_idx, mid_idx, high_idx)


def merge_sort(input_list):
    if len(input_list) < 2:
        return

    tmp_list = [None] * len(input_list)
    merge_sort_range(input_list, tmp_list, 0, len(input_list) - 1)


some_list = [9, 1, 3, 1, 5, 8]
merge_sort(some_list)
print (some_list)
