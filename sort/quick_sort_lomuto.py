def partition(input_list, low_idx, high_idx):
    pivot_value = input_list[high_idx]
    i = low_idx

    for j in range(i, high_idx):
        if input_list[j] <= pivot_value:
            input_list[i], input_list[j] = input_list[j], input_list[i]
            i = i + 1
    input_list[high_idx], input_list[i] = input_list[i], input_list[high_idx]
    return i


def _sort_range(input_list, low_idx, high_idx):
    if low_idx >= high_idx:
        return

    partition_idx = partition(input_list, low_idx, high_idx)
    _sort_range(input_list, low_idx, partition_idx - 1)
    _sort_range(input_list, partition_idx + 1, high_idx)


def sort(input_list):
    if not input_list or len(input_list) < 2:
        return
    _sort_range(input_list, 0, len(input_list) - 1)


def test():
    input_list = [1, 2, 3, 4, 5]
    sort(input_list)
    assert input_list == [1, 2, 3, 4, 5]

    input_list = [5, 4, 3, 2, 1]
    sort(input_list)
    assert input_list == [1, 2, 3, 4, 5]

    input_list = [4, 2, 0, 5, 1]
    sort(input_list)
    assert input_list == [0, 1, 2, 4, 5]

    input_list = [1, 9, 3, 5, 4, 1]
    sort(input_list)
    assert input_list == [1, 1, 3, 4, 5, 9]

    input_list = [5, 5, 3, 5, 7, 5, 5]
    sort(input_list)
    assert input_list == [3, 5, 5, 5, 5, 5, 7]

    input_list = [5, 5, 7, 8, 5, 3, 5, 1, 2, 3]
    sort(input_list)
    assert input_list == [1, 2, 3, 3, 5, 5, 5, 5, 7, 8]


if __name__ == "__main__":
    test()
