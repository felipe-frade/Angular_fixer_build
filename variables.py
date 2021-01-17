import os

# constants
PATH = os.path.dirname(os.path.abspath(__file__))
MANAGER_PATH = PATH + '\\fixer_manager.py'

# variaveis
infos = []
count = 0
language = 1
tempo = 0

# menssagens
msg_config_errado = 'Acho que tem algo de errado com seu arquivo de configuração!\nI think there is something wrong with your configuration file!'
msg_config_sem = 'Sem arquivo de configuração... tsc tsc tsc\nNo configuration file ... tsc tsc tsc'

msg_escolha_idioma = "Qual o idioma desejado?\nChoose a linguage\n1 - pt-br\n2 - en-us\n"
msg_idioma = "Mas eai? Tem que ser um dos dois!\nShame on you! Choose one of them.\n1 - pt-br\n2 - en-us\n"

def recount():
    count = 0