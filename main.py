from config.db import criar_conexao
from services.user.passageiro_service import *
from services.admin.admin_passageiro_service import gerar_admin_padrao_service
from pages.passageiro import cadastro, login,area_do_usuario
from pages.admin import area_do_admin
import os

conn = criar_conexao()
gerar_admin_padrao_service()

while True:
    os.system("cls")
    print("BEM VINDO AO AEROPORTO AURORA")
    print(" 1.Cadastrar-se")
    print(" 2.Logar")
    print(" 0.Sair do Sistema")
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
            input("Pressione ENTER para continuar")
    elif opc == 0:
        break
if conn:
   conn.close()
   print("conexao fechada.")