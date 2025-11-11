from services.admin.admin_voo_service import *


def cadastrar_voo():
    print("Area de Cadastro do voo")
    id_aviao = int(input("digite o modelo do voo: "))
    local_partida = input("digite o local de partida: ").capitalize()
    local_destino = input("digite o local de destino: ").capitalize()
    duracao = input("digite a duracao do voo: ")
    cadastrar_voo_service(id_aviao, local_partida, local_destino,duracao)

def listar_voo():
    listar_voo_service()

def deletar_voo():
    listar_voo_service()
    id = int(input("qual voo voce deseja deletar (pelo id)? "))
    deletar_voo_service(id)

def alterar_voo():
    listar_voo_service()
    id_voo = int(input("qual voo voce deseja alterar (pelo id)? "))
    id_aviao = input("qual o novo modelo do aviao? ")
    local_partida = input("qual o novo local de partida? ")
    local_destino = input("qual o novo local de destino? ")
    duracao = input("qual a nova duracao da viagem que voce deseja por no voo? ")
    alterar_voo_service(id_voo, id_aviao, local_partida, local_destino, duracao)