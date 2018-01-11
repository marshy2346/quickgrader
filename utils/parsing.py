import os

def replace_vars(var_path, stylesheet_path): 
    """
    Replaces all variable declarations in a Qt Stylesheet and replaces them with
    variables contained in provided var file.

    Expected Format:
    @VariableName = Value

    :param str var_path: path to vars file containing the declarations
    :param str stylesheet_path: path to target stylesheet
    :returns: 0 on success, -1 on failure
    """
    if not os.path.isfile(var_path) or not os.path.isfile(stylesheet_path):
        return -1

    with open(var_path, 'r') as var_decls, open(stylesheet_path, 'r') as stylesheet:
        lines = var_decls.readlines()
        stylesheet_content = stylesheet.read()

        for l in lines:
            tokens = l.split()
            if len(tokens) >= 3 and tokens[0].startswith("@") and tokens[1] == "=":
                stylesheet_content = stylesheet_content.replace(tokens[0], tokens[2])

        return stylesheet_content
        
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
    
