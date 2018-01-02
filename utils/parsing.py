def get_uin(filename):
    """
    Very naive implementation to get the uin from the filename

    :param filename: the student file
    :return: the uin
    """
    uin = ""
    n = 0
    skip = True
    for c in filename:
        if n == 4:
            break
        if c.isdigit():
            if skip:
                skip = False
            else:
                uin += c
                n += 1
    if uin == "":
        return filename
    else:
        return uin

