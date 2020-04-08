def power_set(in_set):
    result_set = []
    for cur_elem in in_set:
        result_set_len = len(result_set)
        for cur_set_idx in range(result_set_len):
            new_set = result_set[cur_set_idx].copy()
            new_set.append(cur_elem)
            result_set.append(new_set)

        result_set.append([cur_elem])

    result_set.append([])

    return result_set


print(power_set([1, 2, 3]))
