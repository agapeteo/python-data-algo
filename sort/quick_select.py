def _quick_select(top_idx, in_list, low_idx, hi_idx):
    pivot_value = in_list[hi_idx]
    i = low_idx

    for j in range(i, hi_idx):
        if in_list[j] <= pivot_value:
            in_list[i], in_list[j] = in_list[j], in_list[i]
            i += 1
    in_list[i], in_list[hi_idx] = in_list[hi_idx], in_list[i]

    if top_idx != i:
        if top_idx < i:
            return _quick_select(top_idx, in_list, low_idx, i - 1)
        return _quick_select(top_idx, in_list, i + 1, hi_idx)

    return in_list[i]


def quick_select(top_idx, in_list):
    return _quick_select(top_idx, in_list, 0, len(in_list) - 1)


some_list = [1, 2, 9, 7, 4]
print(quick_select(0, some_list))
print(quick_select(1, some_list))
print(quick_select(2, some_list))
print(quick_select(3, some_list))
print(quick_select(4, some_list))
