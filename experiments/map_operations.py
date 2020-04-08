d = {"one": 1, "two": 2}  # create dict with initialized data

some_dict = {}  # create empty dict

some_dict["three"] = 3  # set/update value

try:
    print some_dict["four"]  # read/get value from dict, throws KeyError if given key is absent
except KeyError:
    print "key does not exist int this dictionary"

print "one" in some_dict  # check if dict contains key, O(1)
