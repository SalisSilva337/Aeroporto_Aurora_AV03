from config.db import criar_conexao
from services.passageiro_service import *

import os

conn = criar_conexao()


while True:
    # os.system("cls")
    print("1.Cadastrar-se\n2.Logar\n0.Sair do Sistema")
    opc = int(input("digite uma opcao: "))

    if opc == 1:
        print("Area de Cadastro")
        nome = input("digite seu nome: ").capitalize()
        email = input("digite seu email: ")
        telefone = input("digite seu telefone: ")
        senha = input("digite sua senha: ")
        inserir_passageiro(nome,email,senha,telefone)
    
    elif opc == 2:
        print("Area de Login")
        email = input("digite seu email: ")
        senha = input("digite sua senha: ")
        if nome == "admin" and email == "admin@email.com" and senha == "admin123":
            listar_passageiros()
    elif opc == 0:
        break
if conn:
   conn.close()
   print("conexao fechada.")