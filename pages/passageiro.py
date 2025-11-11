from services.user.passageiro_service import *
from services.admin.admin_passageiro_service import *

def cadastro():
    print("Area de Cadastro")
    nome = input("digite seu nome: ").capitalize()
    email = input("digite seu email: ")
    telefone = input("digite seu telefone: ")
    senha = input("digite sua senha: ")
    cadastrar_passageiro(nome,email,senha,telefone)


def login():
    print("Area de Login")
    email = input("digite seu email: ")
    senha = input("digite sua senha: ")
    user = logar_passageiro(email, senha)
    return user

def area_do_usuario(user):
    while True:
        print(f"Area do(a) {user[1]}, o que voce deseja fazer? \n 1.Fazer uma Reserva \n 2.Listar Voos \n 0.Deslogar") 
        user_opc = int(input("digite uma opcao: "))  
        if user_opc == 1:
            print("reservar")
        elif user_opc == 0:
            break


def login():
    print("Area de Login")
    email = input("digite seu email: ")
    senha = input("digite sua senha: ")
    user = logar_passageiro(email, senha)
    return user

def listar_passageiros():
    listar_passageiros_service()

def deletar_passageiro():
    listar_passageiros_service()
    id = int(input("qual voo voce deseja deletar (pelo id)? "))
    deletar_passageiro_service(id)



