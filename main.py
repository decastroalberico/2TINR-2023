# -*- coding: utf-8 -*-
"""
A module for demonstrating a dictionary and how to print its contents.
"""

dicionario = {1254: ["Alberico", "Professor"]}

def exibir():
    for chave, lista in dicionario.items():
        print("Cod. do Funcionario...", chave)
        print("Nome..................", lista[0])
        print("Cargo.................", lista[1])

exibir()
