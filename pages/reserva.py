from services.admin.admin_reserva_service import *
import os
import datetime 
from services.user.reserva_service import *

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def listar_reservas():
    listar_reservas_service()

def cadastrar_reserva():
    cls()
    print("Área de Cadastro da reserva")
    id_voo = int(input("Digite o ID do voo: ").strip())
    while id_voo == "":
        print("O modelo não pode ser vazio.")
        id_voo = input("Digite o voo: ").strip()

    classe = input("Digite a classe: ").strip().capitalize()
    metodo_pagamento = input("Digite o metodo de pagamento: ").strip().capitalize()
    quantidade_passageiros = int(input("Digite a classe: ")).strip()
    data_dia = int(input("digite o dia do voo: "))
    data_mes = int(input("Digite o mês do voo: "))
    data_ano = int(input("Digite o ano do voo: "))
    data = datetime(data_ano,data_mes,data_dia)
    cadastrar_reserva(id_voo, classe, metodo_pagamento, quantidade_passageiros, data)   

def deletar_reserva():
    id_reserva = input("Digite seu ID da reserva: ")
    deletar_reserva_service(id_reserva)
    

