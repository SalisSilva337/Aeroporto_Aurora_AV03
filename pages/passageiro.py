from services.user.passageiro_service import *
from services.admin.admin_passageiro_service import *
import os


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def ler_inteiro(msg, minimo=None, maximo=None):
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
    while email == "":
        print("E-mail não pode ser vazio.")
        email = input("Digite seu email: ").strip()

    telefone = input("Digite seu telefone: ").strip()
    while telefone == "":
        print("Telefone não pode ser vazio.")
        telefone = input("Digite seu telefone: ").strip()

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
        print(" 1. Fazer uma Reserva")
        print(" 2. Listar Voos")
        print(" 0. Deslogar")

        opc = ler_inteiro("Digite uma opção: ", minimo=0, maximo=2)

        if opc == 1:
            print("reservar")
            input("\nPressione ENTER para continuar...")
        elif opc == 2:
            print("listar voos")
            input("\nPressione ENTER para continuar...")
        elif opc == 0:
            break


def listar_passageiros():
    cls()
    listar_passageiros_service()


def deletar_passageiro():
    cls()
    listar_passageiros_service()

    id_pass = ler_inteiro("Qual passageiro você deseja deletar (pelo ID)? ", minimo=1)

    deletar_passageiro_service(id_pass)
