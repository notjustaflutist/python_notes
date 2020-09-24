def validate(code_string):
    s = "missing "
    p1 = code_string.find("(")
    p2 = code_string.find(")")

    if "def" not in code_string:
        return s + "def"
    elif ":" not in code_string:
        return s + ":"
    elif "(" and ")" not in code_string:
        return s + "paren"
    # elif "()" in code_string:
    #    return s +"param"
    elif p1 == p2 + 1:
        return s + "param"
    elif "    " not in code_string:
        return s + "indent"
    elif "validate" not in code_string:
        return "wrong name"
    elif "return" not in code_string:
        return s + "return"
    else:
        return True


