from services.admin.admin_reserva_service import *
import os
from datetime import datetime
from services.user.reserva_service import *
from pages.voo import listar_voo

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def listar_reservas():
    listar_reservas_service()

def ler_opcao(msg, minimo, maximo):
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

def cadastrar_reserva(user):
    cls()
    print("Área de Cadastro da reserva")
    listar_voo()
    id_voo = int(input("Digite o id do voo: "))
    while id_voo == "":
        print("O id do voo não pode ser vazio.")
        id_voo = int(input("Digite o id do voo: "))
    
    # classe select
    print("Qual opcao de classe? ")
    print("1.Economica")
    print("2.Executiva")
    print("3.Primeira Classe")
    opc_classe = ler_opcao("Selecione uma opcao de classe: ", 1, 3)
    if opc_classe == 1:
        classe = "Economica"
    elif opc_classe == 2:
        classe = "Executiva"
    elif opc_classe == 3:
        classe = "Primeira Classe"

    #pagamento select
    print("Qual opcao de pagamento? ")
    print("1.PIX")
    print("2.DEBITO")
    print("3.CREDITO")
    opc_metodo_pagamento = ler_opcao("Selecione uma opcao de metodo de pagamento: ",1,3)
    if opc_metodo_pagamento == 1:
        metodo_pagamento = "PIX"
    elif opc_metodo_pagamento == 2:
        metodo_pagamento = "DEBITO"
    elif opc_metodo_pagamento == 3:
        metodo_pagamento = "CREDITO"
    quantidade_passageiros = int(input("Digite a quantidade de passageiros: "))
    hoje = datetime.today()
    data = datetime(hoje.year,hoje.month,hoje.day)
    cadastrar_reserva_service(id_voo, user, classe, metodo_pagamento, quantidade_passageiros, data)   

def deletar_reserva(user):
    deletar_reserva_service(user[0])
    

