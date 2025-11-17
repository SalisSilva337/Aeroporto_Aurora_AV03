from services.admin.admin_tripulacao_service import *
from services.admin.admin_voo_service import listar_voo_service
import os 

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def inserir_tripulacao():
    print("Área de Cadastro da Tripulação")
    listar_voo_service()
    id_voo = int(input("Digite o ID do voo: "))
    inserir_tripulacao_ao_voo_service(id_voo)

def remover_tripulacao():
    listar_tripulacao_service()
    id_trip = int(input("Qual tripulação você deseja remover (pelo ID)? "))
    remover_tripulacao_service(id_trip)

def listar_tripulacao():
    listar_tripulacao_service()
