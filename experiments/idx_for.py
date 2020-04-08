import os


def print_dir_content(dir_abs, tabs=0, ignore_hidden=True):
    for f in os.listdir(dir_abs):
        if ignore_hidden and f.startswith("."):
            continue

        tabs_str = "".join("\t" * tabs)
        print tabs_str + f + "/"

        full_path = os.path.join(dir_abs, f)
        if os.path.isdir(full_path):
            print_dir_content(full_path, tabs + 1)
        else:
            print "\t" + tabs_str + f


print_dir_content("/full/path/to/directory/")


# on exceptions https://thomas-cokelaer.info/tutorials/python/exceptions.html
# nice intro into classes  https://thomas-cokelaer.info/tutorials/python/classes.html
