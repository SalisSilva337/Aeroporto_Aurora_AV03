from config.db import criar_conexao
from services.passageiro_service import *
from services.admin_service import *
import os


conn = criar_conexao()
while True:
    gerar_admin_padrao()
    # os.system("cls")
    print(" 1.Cadastrar-se \n 2.Logar \n 0.Sair do Sistema")
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
                print("Area do Admin")
                print(" 1.Listar Passageiros \n 2.Deletar Passageiro \n 3.Criar Voo \n 4.Ver Detalhes dos Voos \n 5.Alterar Voo \n 6.Deletar Voo \n 0.Sair do Sistema")
                adm_opc = int(input("Digite uma opcao: "))
                if adm_opc == 1:
                    listar_passageiros()
                elif adm_opc == 2:
                    deletar_passageiro()
                elif adm_opc == 3:
                    listar_passageiros()
                elif adm_opc == 4:
                    listar_passageiros()
            else:
                print(f"Bem-vindo, {user[1]}!")
        else:
            print("Email ou senha incorretos")
    elif opc == 0:
        break
if conn:
   conn.close()
   print("conexao fechada.")