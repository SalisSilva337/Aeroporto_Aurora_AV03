from config.db import criar_conexao
from services.passageiro_service import *
from services.admin_service import gerar_admin_padrao
import os


conn = criar_conexao()
while True:
    # os.system("cls")
    gerar_admin_padrao()
    print("1.Cadastrar-se\n2.Logar\n0.Sair do Sistema")
    opc = int(input("digite uma opcao: "))

    if opc == 1:
        print("Area de Cadastro")
        nome = input("digite seu nome: ").capitalize()
        email = input("digite seu email: ")
        telefone = input("digite seu telefone: ")
        senha = input("digite sua senha: ")
        cadastrar_passageiro(nome,email,senha,telefone)

    elif opc == 2:
        print("Area de Login")
        email = input("digite seu email: ")
        senha = input("digite sua senha: ")
        user = logar_passageiro(email, senha)
        if user:
            print("Logado com sucesso!")

            if user[2] == "admin@email.com":
                listar_passageiros()
            else:
                print(f"Bem-vindo, {user[1]}!")
        else:
            print("Email ou senha incorretos.")
    elif opc == 0:
        break
if conn:
   conn.close()
   print("conexao fechada.")