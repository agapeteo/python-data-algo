def max_int(in_list):
    result = None
    for v in in_list:
        if result < v:
            result = v
    return result


def sort(in_list):
    counting_list_size = max(in_list) + 1
    counting_list = [None] * counting_list_size

    for idx_by_value in in_list:
        cur_list = counting_list[idx_by_value]
        if cur_list:
            cur_list.append(idx_by_value)
        else:
            cur_list = [idx_by_value]
            counting_list[idx_by_value] = cur_list

    cur_idx = 0
    for cur_list in counting_list:
        if not cur_list:
            continue

        for cur_value in cur_list:
            in_list[cur_idx] = cur_value
            cur_idx += 1


some_list = [4, 3, 2, 3, 15]
sort(some_list)

print(some_list)
