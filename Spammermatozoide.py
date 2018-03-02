import re

mensagem_inicial = """


    ____ ___  ____ _  _ _  _ ____ ____ _  _ ____ ___ ____ ___  ____ _ ___  ____ 
    [__  |__] |__| |\/| |\/| |___ |__/ |\/| |__|  |  |  |   /  |  | | |  \ |___ 
    ___] |    |  | |  | |  | |___ |  \ |  | |  |  |  |__|  /__ |__| | |__/ |___ 
                                                                                

                       ____      Codado por: Natanael Antonioli
       ______     ___.'  o `.    "Esse software tá uma porra"
      /~----,\___/,--.   ,_ |    https://twitter.com/_natanael666
            `-----'   `---'`     https://github.com/NatanaelAntonioli/spammermatozoide

    1)Selecione todo o texto que deseja filtrar (CTRL+A em navegadores)
    2)Salve-o em um arquivo de nome "list.txt" no mesmo diretório do script.
    3)Pressione enter quando estiver pronto.
    4)O resultado final será enviado para "list-parsed.txt".
        """

print (mensagem_inicial)
input("")
line = tr = open('list.txt', 'r').read() 
match = re.findall(r'[\w\.-]+@[\w\.-]+', line)
f = open('list-parsed.txt', 'w')
for i in match:
    i = i.lower()
    print(" ", i)
    f.write(i + '\n')
f.close()
