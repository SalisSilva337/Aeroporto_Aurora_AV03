from services.user.passageiro_service import *
from services.admin.admin_passageiro_service import *
import os

def cls():
    os.system("cls" if os.name == "nt" else "clear")


def listar_passageiros():
    cls()
    listar_passageiros_service()


def deletar_passageiro():
    cls()
    listar_passageiros_service()

    id_pass = int(input("Qual passageiro você deseja deletar (pelo ID)? "))

    deletar_passageiro_service(id_pass)
