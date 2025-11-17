from pages.passageiro import *
from pages.aviao import *
from pages.reserva import *
from pages.voo import *
from pages.tripulacao import *
import os

def cls():
    os.system("cls" if os.name == "nt" else "clear")


def ler_opcao(msg, minimo, maximo):
    while True:
        try:
            valor = int(input(msg))
            if valor < minimo or valor > maximo:
                print(f"Opção inválida! Digite um número entre {minimo} e {maximo}.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")


def area_do_admin():
    while True:
        cls()
        print("=== Área do Admin ===")
        print(" 1. Passageiros")
        print(" 2. Reservas")
        print(" 3. Voos")
        print(" 4. Aviões")
        print(" 5. Tripulações")
        print(" 0. Deslogar")

        adm_opc = ler_opcao("Digite uma opção: ", 0, 5)

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
    cls()
    while True:   
        print("=== Admin - Passageiros ===")
        print(" 1. Listar Passageiros")
        print(" 2. Deletar Passageiro (ID)")
        print(" 0. Voltar")

        opc_p = ler_opcao("Digite uma opção: ", 0, 2)

        if opc_p == 1:
            listar_passageiros()
        elif opc_p == 2:
            deletar_passageiro()
        elif opc_p == 0:
            break


def admin_reservas():
    cls()
    while True:
        print("=== Admin - Reservas ===")
        print(" 1. Listar Reservas")
        print(" 0. Voltar")

        opc_r = ler_opcao("Digite uma opção: ", 0, 1)

        if opc_r == 1:
            listar_reservas()
        elif opc_r == 0:
            break


def admin_voos():
    cls()
    while True:   
        print("=== Admin - Voos ===")
        print(" 1. Listar Voos")
        print(" 2. Cadastrar Voo")
        print(" 3. Deletar Voo (ID)")
        print(" 4. Alterar Voo (ID)")
        print(" 0. Voltar")

        opc_v = ler_opcao("Digite uma opção: ", 0, 4)

        if opc_v == 1:
            listar_voo()
        elif opc_v == 2:
            cadastrar_voo()
        elif opc_v == 3:
            deletar_voo()
        elif opc_v == 4:
            alterar_voo()
        elif opc_v == 0:
            break


def admin_tripulacao():
    cls()
    while True:
        print("=== Admin - Tripulação ===")
        print(" 1. Adicionar tripulação a um voo")
        print(" 2. Remover tripulação de um voo")
        print(" 3. Ver todas as tripulações")
        print(" 0. Voltar")

        opc_t = ler_opcao("Digite uma opção: ", 0, 3)

        if opc_t == 1:
            inserir_tripulacao()
        elif opc_t == 2:
            remover_tripulacao()
        elif opc_t == 3:
            listar_tripulacao()
        elif opc_t == 0:
            break


def admin_avioes():
    cls()
    while True:
        print("=== Admin - Aviões ===")
        print(" 1. Listar Aviões")
        print(" 2. Cadastrar Avião")
        print(" 3. Deletar Avião (ID)")
        print(" 4. Alterar Avião")
        print(" 0. Voltar")

        opc_a = ler_opcao("Digite uma opção: ", 0, 4)

        if opc_a == 1:
            listar_avioes()
        elif opc_a == 2:
            cadastrar_aviao()
        elif opc_a == 3:
            deletar_aviao()
        elif opc_a == 4:
            alterar_aviao()
        elif opc_a == 0:
            break
