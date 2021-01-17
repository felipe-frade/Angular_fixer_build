import config as con
import variables as var
import file_manager as fl

import comands as cmd

import variables_pt_br as br
import variables_en_us as us

def config():
    config = fl.read_this(var.PATH + "\\config.txt")

    if(len(config[0]) > 0):
        if(len(config[0]) == 7):

            for t in config[0]:
                config[0][var.count] = strip_config(t)
                var.count += 1
            var.recount()

            var.infos = config[0]

            chose_language()

        else:
            print(var.msg_config_errado)
    else:
        print(var.msg_config_sem)
        # ask about the configuration 

def strip_config(config: str):
    return config.split(":")[1].replace('\n', '')

def chose_language():
    if(int(var.infos[5]) in [1,2] and int(var.infos[6]) == 1):
        var.language = int(var.infos[5])
    else:
        language = int(input(var.msg_escolha_idioma))

        while(language not in [1, 2]):
            cmd.clear_shell()
            language = int(input(var.msg_idioma))
        
        var.language = language