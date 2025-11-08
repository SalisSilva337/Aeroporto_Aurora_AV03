from config.db import criar_conexao
from services.passageiro_service import *
from services.admin_passageiro_service import *
from pages.usuario import cadastro, login,area_do_usuario
from pages.admin import area_do_admin
import os


conn = criar_conexao()

while True:
    gerar_admin_padrao()
    # os.system("cls")
    print("BEM VINDO AO AEROPORTO AURORA")
    print(" 1.Cadastrar-se \n 2.Logar \n 0.Sair do Sistema")
    opc = int(input("digite uma opcao: "))

    if opc == 1:
        cadastro()
    elif opc == 2:
        user = login()
        if user:
            print("Logado com sucesso!")
            if user[2] == "admin@email.com":
                area_do_admin()
            else:
                print(f"Bem-vindo, {user[1]}! \n")
                area_do_usuario(user)
        else:
            print("Email ou senha incorretos")
    elif opc == 0:
        break
if conn:
   conn.close()
   print("conexao fechada.")