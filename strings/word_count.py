def rotate_left(in_str, count):
    chars = list(in_str)

    for k in range(count):
        first = chars[0]
        for i in range(0, len(chars) - 1):
            chars[i] = chars[i + 1]
        chars[len(chars) - 1] = first
    return ''.join(chars)


def rotate_right(in_str, count):
    chars = list(in_str)

    for k in range(count):
        last = chars[len(chars) - 1]
        for i in range(len(chars) - 1, 0, -1):
            chars[i] = chars[i - 1]
        chars[0] = last
    return ''.join(chars)


print(rotate_left("abcd", 1))
print(rotate_right("abcd", 1))
print()

print(rotate_left("abcd", 2))
print(rotate_right("abcd", 2))
print()

print(rotate_left("abcd", 4))
print(rotate_right("abcd", 4))
print()
