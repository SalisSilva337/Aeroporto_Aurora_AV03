from services.admin.admin_aviao_service import *
import os


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def cadastrar_aviao():
    cls()
    print("Área de Cadastro do Avião")

    modelo = input("Digite o modelo do avião: ").strip().capitalize()
    while modelo == "":
        print("O modelo não pode ser vazio.")
        modelo = input("Digite o modelo do avião: ").strip().capitalize()

    capacidade = int(input("Digite a capacidade do avião: "))

    cadastrar_aviao_service(modelo, capacidade)


def listar_avioes():
    cls()
    listar_avioes_service()


def deletar_aviao():
    cls()
    listar_avioes_service()

    id_aviao = int(input("Qual avião você deseja deletar (pelo ID)? "))

    deletar_aviao_service(id_aviao)


def alterar_aviao():
    cls()
    listar_avioes_service()

    id_aviao = int(input("Qual avião você deseja alterar (pelo ID)? "))

    modelo = input("Qual o novo modelo do avião? ").strip().capitalize()
    while modelo == "":
        print("O modelo não pode ser vazio.")
        modelo = input("Qual o novo modelo do avião? ").strip().capitalize()

    capacidade = int(input("Qual a nova capacidade máxima do avião? "))

    alterar_aviao_service(modelo, capacidade, id_aviao)
