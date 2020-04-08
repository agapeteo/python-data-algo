

def reverse(input_str):
    if not input_str:
        return input_str

    str_arr = list(input_str)
    i = 0
    j = len(str_arr) - 1
    while i < j:
        swap(str_arr, i, j)
        i = i + 1
        j = j - 1

    return ''.join(str_arr)


def swap(str_arr, left_idx, right_idx):
    left_char = str_arr[left_idx]
    right_char = str_arr[right_idx]
    str_arr[left_idx] = right_char
    str_arr[right_idx] = left_char
