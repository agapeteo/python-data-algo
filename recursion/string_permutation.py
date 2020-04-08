def _string_permutation(prefix, in_str, permutations):
    if in_str:
        for char_idx in range(len(in_str)):
            new_prefix = prefix + in_str[char_idx]
            str_before = in_str[:char_idx]
            str_after = ""
            if char_idx != len(in_str) - 1:
                str_after = in_str[char_idx + 1:]
            new_str = str_before + str_after

            _string_permutation(new_prefix, new_str, permutations)
    else:
        permutations.append(prefix)
    return permutations


def string_permutation(in_str):
    return _string_permutation("", in_str, [])


print(string_permutation("abcde"))
print(len(string_permutation("abcde")))
