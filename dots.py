def add_dots(string):
    nstring = ""
    for i in range(len(string)):
        if i != len(string) - 1:
            nstring += string[i] + "."
        else:
            nstring += string[i]
    return nstring


def short_add_dots(s):
    return ".".join(s)


def remove_dots(string):
    new_string = string.split(".")
    restring = ""
    for i in range(len(new_string)):
        restring = restring + new_string[i]
    return restring


def short_remove_dots(s):
    return s.replace(".", "")


s = "potato"
d = add_dots(s)
print(add_dots(s))
print(remove_dots(d))

t = "gopher"
print(short_add_dots(t))
u = short_add_dots(t)
print(short_remove_dots(u))