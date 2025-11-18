from services.admin.admin_voo_service import *
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


def ler_duracao():
    while True:
        try:
            duracao_horas = ler_inteiro("Digite a duração do voo (horas): ", minimo=0)
            duracao_min = ler_inteiro("Digite a duração do voo (minutos): ", minimo=0, maximo=59)

            return f"{duracao_horas:02}:{duracao_min:02}:00"
        except:
            print("Erro inesperado, tente novamente.")


def cadastrar_voo():
    print("Área de Cadastro do Voo")

    id_aviao = int(input("Digite o ID do avião: "))
    local_partida = input("Digite o local de partida: ").upper()
    local_destino = input("Digite o local de destino: ").upper()
    duracao = ler_duracao()

    cadastrar_voo_service(id_aviao, local_partida, local_destino, duracao)


def listar_voo():
    listar_voo_service()


def deletar_voo():
    listar_voo_service()
    id_voo = int(input("Qual voo você deseja deletar (ID)? "))
    deletar_voo_service(id_voo)


def alterar_voo():
    listar_voo_service()

    id_voo = int(input("Qual voo você deseja alterar (ID)? "))
    id_aviao = int(input("Digite o novo ID do avião: "))
    local_partida = input("Novo local de partida: ").upper()
    local_destino = input("Novo local de destino: ").upper()
    duracao = ler_duracao()

    alterar_voo_service(id_voo, id_aviao, local_partida, local_destino, duracao)
