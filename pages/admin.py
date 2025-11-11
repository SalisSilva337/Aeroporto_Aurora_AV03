from pages.passageiro import *
from pages.aviao import *
from pages.reserva import *
from pages.voo import *
from pages.tripulacao import *

def area_do_admin():
    while True:
        print("Area do Admin")
        print(" 1.Passageiros \n 2.Reservas \n 3.Voos \n 4.Avioes \n 5.Tripulacoes \n0.Deslogar")
        adm_opc = int(input("Digite uma opcao: "))
        if adm_opc == 1:
            admin_passageiros()
        elif adm_opc == 2:
            admin_reservas()
        elif adm_opc == 3:
            admin_voos()
        elif adm_opc == 4:
            admin_avioes()
        elif adm_opc == 5:
            admin_tripulacao()
        elif adm_opc == 0:
            break

def admin_passageiros():
    print("Admin - Passageiros \n 1.Listar Passageiros \n 2.Deletar Passageiro (ID) \n 0.Voltar")
    opc_p = int(input("Digite uma opcao: "))
    if opc_p == 1:
        listar_passageiros()
    elif opc_p == 2:
        deletar_passageiro()

def admin_reservas():
    print("Admin - Reservas \n 1.Listar Reservas \n 0.Voltar")
    opc_r = int(input("Digite uma opcao: "))
    if opc_r == 1:
        listar_reservas()

def admin_voos():
    print("Admin - Voos \n 1.Listar Voos \n 2.Cadastrar Voo \n 3.Deletar Voo (ID) 4.Alterar Voo (ID) \n 0.Voltar")
    opc_v = int(input("Digite uma opcao: "))
    if opc_v == 1:
        listar_voo()
    if opc_v == 2:
        cadastrar_voo()
    if opc_v == 3:
        deletar_voo()
    if opc_v == 4:
        alterar_voo()

def admin_tripulacao():
    print("Admin - Tripulacao \n 1.Adicionar Tripulacao a um voo \n 2.Remover Tripulacao de um voo \n 0.Voltar")
    opc_t = int(input("Digite uma opcao: "))
    if opc_t == 1:
        inserir_tripulacao()
    elif opc_t == 2:
        remover_tripulacao()

def admin_avioes():
    print("Admin - Avioes \n 1.Listar Avioes \n 2.Cadastrar Aviao \n 3.Deletar Aviao (ID) 4.Alterar Aviao \n 0.Voltar")
    opc_a = int(input("Digite uma opcao: "))
    if opc_a == 1:
        listar_avioes()
    if opc_a == 2:
        cadastrar_aviao()
    if opc_a == 3:
        deletar_aviao()
    if opc_a == 4:
        alterar_aviao()