def two_in_binary():
    return 0b10


def two_in_binary_2():
    return int("10", 2)


def number_to_binary_str(in_number):
    return format(in_number, "b")


def number_to_binary_str_2(in_number):
    return "{0:b}".format(in_number)


def check_bit(idx, in_number):
    mask = 1 << idx
    return mask & in_number != 0


def set_bit(idx, in_number):
    mask = 1 << idx
    return mask | in_number


def clear_bit(idx, in_number):
    mask = ~(1 << idx)
    return in_number & mask


def toggle_bit(idx, in_number):
    mask = 1 << idx
    return in_number ^ mask


def is_even(in_number):
    return in_number & 1 == 0


print(two_in_binary())
print(two_in_binary_2())
print(number_to_binary_str(7))
print(number_to_binary_str(5))
print(check_bit(1, int("110", 2)))
print(check_bit(1, int("100", 2)))

print(set_bit(1, int("101", 2)))  # 7

print(clear_bit(1, int("111", 2)))  # 5

print(toggle_bit(1, int("111", 2)))  # 5

print(is_even(1))
print(is_even(3))
print(is_even(2))
print(is_even(10))
