def validate(input_str, open_str="(", closed_str=")"):
    counter = 0
    for c in input_str:
        if c == open_str:
            counter += 1
        elif c == closed_str:
            if counter == 0:
                return False
            counter -= 1
    return counter == 0


def test_validation():
    assert (validate("to ((be)) or (not) to be")), "should be valid"
    assert (not validate("to ((be)(or) not")), "should be not valid"
    assert (not validate(")(")), "should be not valid"
    assert (not validate("to (be)) or (")), "should be not valid"


if __name__ == "__main__":
    test_validation()
