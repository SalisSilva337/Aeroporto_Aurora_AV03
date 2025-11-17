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
            if minimo is not None and valor < minimo:
                print(f"Valor não pode ser menor que {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"Valor não pode ser maior que {maximo}.")
                continue
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
    
    while True:  
        cls() 
        print("=== Admin - Passageiros ===")
        print(" 1. Listar Passageiros")
        print(" 2. Deletar Passageiro (ID)")
        print(" 0. Voltar")

        opc_p = ler_opcao("Digite uma opção: ", 0, 2)

        if opc_p == 1:
            listar_passageiros()
            input("Pressione ENTER para continuar...")
        elif opc_p == 2:
            deletar_passageiro()
            input("Pressione ENTER para continuar...")
        elif opc_p == 0:
            break


def admin_reservas():
    while True:
        cls()
        print("=== Admin - Reservas ===")
        print(" 1. Listar Reservas")
        print(" 0. Voltar")

        opc_r = ler_opcao("Digite uma opção: ", 0, 1)

        if opc_r == 1:
            listar_reservas()
            input("Pressione ENTER para continuar...")
        elif opc_r == 0:
            break


def admin_voos():
    while True: 
        cls()  
        print("=== Admin - Voos ===")
        print(" 1. Listar Voos")
        print(" 2. Cadastrar Voo")
        print(" 3. Deletar Voo (ID)")
        print(" 4. Alterar Voo (ID)")
        print(" 0. Voltar")

        opc_v = ler_opcao("Digite uma opção: ", 0, 4)

        if opc_v == 1:
            listar_voo()
            input("Pressione ENTER para continuar...")
        elif opc_v == 2:
            cadastrar_voo()
            input("Pressione ENTER para continuar...")
        elif opc_v == 3:
            deletar_voo()
            input("Pressione ENTER para continuar...")
        elif opc_v == 4:
            alterar_voo()
            input("Pressione ENTER para continuar...")
        elif opc_v == 0:
            break


def admin_tripulacao():
    
    while True:
        cls()
        print("=== Admin - Tripulação ===")
        print(" 1. Adicionar tripulação a um voo")
        print(" 2. Remover tripulação de um voo")
        print(" 3. Ver todas as tripulações")
        print(" 0. Voltar")

        opc_t = ler_opcao("Digite uma opção: ", 0, 3)

        if opc_t == 1:
            inserir_tripulacao()
            input("Pressione ENTER para continuar...")
        elif opc_t == 2:
            remover_tripulacao()
            input("Pressione ENTER para continuar...")
        elif opc_t == 3:
            listar_tripulacao()
            input("Pressione ENTER para continuar...")
        elif opc_t == 0:
            break


def admin_avioes():
    while True:
        cls()
        print("=== Admin - Aviões ===")
        print(" 1. Listar Aviões")
        print(" 2. Cadastrar Avião")
        print(" 3. Deletar Avião (ID)")
        print(" 4. Alterar Avião")
        print(" 0. Voltar")

        opc_a = ler_opcao("Digite uma opção: ", 0, 4)

        if opc_a == 1:
            listar_avioes()
            input("Pressione ENTER para continuar...")
        elif opc_a == 2:
            cadastrar_aviao()
            input("Pressione ENTER para continuar...")
        elif opc_a == 3:
            deletar_aviao()
            input("Pressione ENTER para continuar...")
        elif opc_a == 4:
            alterar_aviao()
            input("Pressione ENTER para continuar...")
        elif opc_a == 0:
            break
