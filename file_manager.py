import error

def read_this(file_path):
    result = [[], []]

    try:
        fix = open(file_path, "r+")
        result[0] = fix.readlines()    
    except:
        result[1] = "Não achei o arquivo"

    return result

def write_this(file_path, all_lines):
    f = open(file_path, "w")
    f.write(all_lines)
    f.close()