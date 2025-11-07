from config.db import criar_conexao
from services.passageiro_service import inserir_passageiro
import os

conn = criar_conexao()
while True:
    os.system("cls")
    print("1.Cadastrar-se\n0.Sair do Sistema")
    opc = int(input("digite uma opcao: "))

    if opc == 1:
        nome = input("digite seu nome: ").capitalize()
        email = input("digite seu email: ")
        telefone = input("digite seu telefone: ")
        inserir_passageiro(nome,email,telefone)
    elif opc == 0:
        break
if conn:
   conn.close()
   print("conexao fechada.")