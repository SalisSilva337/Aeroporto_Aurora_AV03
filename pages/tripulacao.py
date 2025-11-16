from services.admin.admin_tripulacao_service import *
from services.admin.admin_voo_service import listar_voo_service
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

def inserir_tripulacao():
    print("Área de Cadastro da Tripulação")
    listar_voo_service()
    id_voo = ler_inteiro("Digite o ID do voo: ", minimo=1)
    inserir_tripulacao_ao_voo_service(id_voo)

def remover_tripulacao():
    listar_tripulacao_service()
    id_trip = ler_inteiro("Qual tripulação você deseja remover (pelo ID)? ", minimo=1)
    remover_tripulacao_service(id_trip)

def listar_tripulacao():
    listar_tripulacao_service()
