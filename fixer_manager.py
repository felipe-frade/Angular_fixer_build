# autor: felipe pereira

import os
import tkinter
from glob import glob
from time import sleep

import variables as var
import config as con
import comands as cmd
import input_manager as im
import file_manager as fl

from variables_pt_br import Messages as br 
from variables_en_us import Messages as us

mes = br()

# CONFIGURATION ***************************

def import_language():
    global mes
    if(var.language == 1):
        mes = br()
    elif(var.language == 2):
        mes = us()
    else:
        print('Sem modulo de linguagem')
    
def define_speed():
    var.tempo = int(input(mes.msg_esta_com_tempo))
    while(var.tempo not in [1,2]):
        cmd.clear_shell()
        var.tempo = int(input(mes.msg_esta_com_tempo))

def end():
    cmd.clear_shell()
    exit()


# CONFIGURATION ***************************

def main():
    con.config()
    import_language()
    define_speed()

    cmd.clear_shell()

    count = 1
    custom_line = ""
    while(int(count) == 1):
        locate = 0

        # enquanto ele não encontrar o caminho
        while(locate == 0):
            project = input(mes.msg_name_project)
            print('# Searching for project (' + project + ') in(' + var.PATH + ')...')
            if os.path.isdir(var.PATH + '\\' + project):
                var.PATH = var.PATH + '\\' + project
                locate = 1
            else:
                print('# Folder not found!')

        end()
        # percorre o projeto todo a busca dos arquivos
        for root, dirs, files in os.walk(var.PATH):
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
                        fl.write_this(file_path, "".join(all_lines))
                        fix.close()
        
        count = input('\nDo you wanna continue?\n1 - yes\n2 - no\n')
    print('\nBye!')

main()