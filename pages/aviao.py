from services.admin.admin_aviao_service import *
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


def cadastrar_aviao():
    cls()
    print("Área de Cadastro do Avião")

    modelo = input("Digite o modelo do avião: ").strip().capitalize()
    while modelo == "":
        print("O modelo não pode ser vazio.")
        modelo = input("Digite o modelo do avião: ").strip().capitalize()

    capacidade = ler_inteiro("Digite a capacidade do avião: ", minimo=1)

    cadastrar_aviao_service(modelo, capacidade)


def listar_avioes():
    cls()
    listar_avioes_service()
    input("\nPressione ENTER para continuar...")


def deletar_aviao():
    cls()
    listar_avioes_service()

    id_aviao = ler_inteiro("Qual avião você deseja deletar (pelo ID)? ", minimo=1)

    deletar_aviao_service(id_aviao)


def alterar_aviao():
    cls()
    listar_avioes_service()

    id_aviao = ler_inteiro("Qual avião você deseja alterar (pelo ID)? ", minimo=1)

    modelo = input("Qual o novo modelo do avião? ").strip().capitalize()
    while modelo == "":
        print("O modelo não pode ser vazio.")
        modelo = input("Qual o novo modelo do avião? ").strip().capitalize()

    capacidade = ler_inteiro("Qual a nova capacidade máxima do avião? ", minimo=1)

    alterar_aviao_service(modelo, capacidade, id_aviao)
