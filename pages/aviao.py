from services.admin.admin_aviao_service import *



def cadastrar_aviao():
    print("Area de Cadastro do Aviao")
    modelo = input("digite o modelo do aviao: ").capitalize()
    capacidade = input("digite a capacidade do aviao: ")
    cadastrar_aviao_service(modelo,capacidade)

def listar_avioes():
    listar_avioes_service()

def deletar_aviao():
    listar_avioes_service()
    id = int(input("qual aviao voce deseja deletar (pelo id)?"))
    deletar_aviao_service(id)


def alterar_aviao():
    listar_avioes_service()
    id = int(input("qual aviao voce deseja alterar (pelo id)?"))
    deletar_aviao_service(id)