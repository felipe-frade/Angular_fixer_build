# autor: felipe pereira
import os
from glob import glob
from time import sleep

# variables
path = os.path.dirname(os.path.abspath(__file__))

# function
def write_this(file_path, all_lines):
    f = open(file_path, "w")
    f.write(all_lines)
    f.close()

count = 1
custom_line = ""
while(int(count) == 1):
    locate = 0

    # enquanto ele não encontrar o caminho
    while(locate == 0):
        project = input('\n# Please tell me the name of the project\n')
        print('# Searching for project (' + project + ') in(' + path + ')...')
        if os.path.isdir(path + '\\' + project):
            path = path + '\\' + project
            locate = 1
        else:
            print('# Folder not found!')

    # percorre o projeto todo a busca dos arquivos
    for root, dirs, files in os.walk(path):
        for fil in files:
            if("node_modules" not in root):
                if("angular.json" in fil or "environment.ts" in fil or "index.html" in fil):
                    file_path = root + '\\' + fil
                    fix = open(file_path, 'r+')
                    all_lines = fix.readlines()
                    index_line = 0
                    
                    print("\n# I am on this file:\n" + file_path)
                if("angular.json" in fil):
                    # percorre as linhas
                    for line in all_lines:
                        
                        # gancho
                        if("outputPath" in line):
                            print("# I found this guy: \n" + line)
                            print("# These guy is where your project will be placed after building")
                            print("# Do you wanna replace for something or do I continue the process on my on?")
                            types = input('\n# 1 - I want to do it manually\n# 2 - Do your magic\n')
                            
                            # se o usuário quer mudar manualmente ou deixar por minhha conta
                            if int(types) == 1:
                                custom_line = input('# Then, what the path?\n# ex..:(C:\\xampp\\htdocs\\projeto)\n')
                            if int(types) != 1:
                                custom_line = root + '\\dist'

                            all_lines[index_line] = line[:line.find(':') + 1] + ' "' + custom_line.replace("\\", "\\\\") + '",\n'

                        index_line = index_line + 1

                if("index.html" in fil):
                    # percorre as linhas
                    for line in all_lines:

                        # gancho
                        if("<base" in line):
                            custom_line = custom_line.replace("\\", "/")
                            all_lines[index_line] = line[:line.find('href=') + 5] + '"' + custom_line.replace("C:/xampp/htdocs", "http://localhost") + '/">\n'
                            print("# I found this guy: \n" + line)
                            print("# I'll replace for this one: \n" + all_lines[index_line])

                        index_line = index_line + 1

                        
                    
                if("angular.json" in fil or "environment.ts" in fil or "index.html" in fil):
                    write_this(file_path, "".join(all_lines))
                    fix.close()
    
    count = input('\nDo you wanna continue?\n1 - yes\n2 - no\n')
print('\nBye!')