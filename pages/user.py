from pages.reserva import cadastrar_reserva, deletar_reserva
from pages.voo import listar_voo
from services.user.passageiro_service import *
import os
import re

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def ler_opcao(msg, minimo, maximo):
    while True:
        try:
            valor = int(input(msg))
            if minimo is not None and valor < minimo:
                print(f"Valor não pode ser menor que {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"Valor não pode ser maior que {maximo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")


def cadastro():
    cls()
    print("Área de Cadastro")

    nome = input("Digite seu nome: ").strip().capitalize()
    while nome == "":
        print("Nome não pode ser vazio.")
        nome = input("Digite seu nome: ").strip().capitalize()

    email = input("Digite seu email: ").strip()
    padrao_email = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    while True:
        if email == "":
            print("E-mail não pode ser vazio.")
        elif not re.match(padrao_email, email):
            print("Formato de e-mail inválido!")
        elif email_existe(email):        
            print("Este e-mail já está cadastrado!")
        else:
            break
    telefone = int(input("Digite seu telefone: "))
    while telefone == "":
        print("Telefone não pode ser vazio.")
        telefone = int(input("Digite seu telefone: "))
        

    senha = input("Digite sua senha: ").strip()
    while senha == "":
        print("Senha não pode ser vazia.")
        senha = input("Digite sua senha: ").strip()


    cadastrar_passageiro(nome, email, senha, telefone)


def login():
    cls()
    print("Área de Login")

    email = input("Digite seu email: ").strip()
    senha = input("Digite sua senha: ").strip()

    user = logar_passageiro(email, senha)
    return user


def area_do_usuario(user):
    while True:
        cls()
        print(f"Área do(a) {user[1]}, o que você deseja fazer?")
        print(" 1.Fazer uma Reserva")
        print(" 2.Listar Voos")
        print(" 3.Cancelar Reserva")
        print(" 0.Deslogar")

        opc = ler_opcao("Digite uma opção: ", minimo=0, maximo=3)

        if opc == 1:
            cadastrar_reserva(user)
            input("Pressione ENTER para continuar...")
        elif opc == 2:
            listar_voo()
            input("Pressione ENTER para continuar...")
        elif opc == 3:
            deletar_reserva(user)
            input("Pressione ENTER para continuar...")
        elif opc == 0:
            break