dicionario = {1254:["Alberico", "Professor"]}

def exibir():
    for chave, lista in dicionario.items():
        print("Cod. do Funcionario...", chave)
        print("Nome..................", lista[0])
        print("Cargo.................", lista[1])
