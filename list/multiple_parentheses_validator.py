def map_for(some_list):
    m = {}
    for i in range(len(some_list)):
        m[some_list[i]] = i
    return m


def validate(open_list, close_list, input_str):
    open_map = map_for(open_list)
    close_map = map_for(close_list)

    stack = []
    for each_char in input_str:
        if each_char in open_map:
            stack.append(each_char)
        elif each_char in close_map:
            if len(stack) == 0:
                return False
            top_char = stack.pop()
            if close_map[each_char] != open_map[top_char]:
                return False
    return len(stack) == 0


def test():
    open_list = ["{", "[", "("]
    close_list = ["}", "]", ")"]

    assert (validate(open_list, close_list, "to ((be)) or (not) to be")), "should be valid"
    assert (validate(open_list, close_list, "to ([be]) or {not} to be")), "should be valid"
    assert (not validate(open_list, close_list, "to ( [be] {or} not }")), "should not be valid"
    assert (not validate(open_list, close_list, ")(")), "should not be valid"
    assert (not validate(open_list, close_list, "to (be) }{ or not")), "should not be valid"


if __name__ == "__main__":
    test()
