from services.admin.admin_voo_service import *


def cadastrar_voo():
    print("Area de Cadastro do voo")
    id_aviao = int(input("digite o id do aviao: "))
    local_partida = input("digite o local de partida: ").capitalize()
    local_destino = input("digite o local de destino: ").capitalize()
    while True:
        try:
            duracao_horas = int(input("Digite a duração do voo (em horas): "))
            duracao_min = int(input("Digite a duração do voo (em minutos): "))
            if duracao_horas < 0 or duracao_min < 0 or duracao_min >= 60:
                print("Valores inválidos! Minutos devem estar entre 0 e 59")
                continue
            duracao = f"{duracao_horas:02}:{duracao_min:02}:00"
            break
        except ValueError:
            print("Digite apenas números inteiros para horas e minutos.")
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