from services.admin.admin_tripulacao_service import *

def inserir_tripulacao():
    print("Area de Cadastro da tripulacao")
    id_voo = input("digite o id do voo: ").capitalize()
    inserir_tripulacao_ao_voo_service(id_voo)


def remover_tripulacao():
    listar_tripulacao_service()
    id = int(input("qual tripulacao voce deseja remover de um voo (pelo id)? "))
    remover_tripulacao_service(id)