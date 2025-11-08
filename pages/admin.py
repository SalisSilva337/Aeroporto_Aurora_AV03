

def area_do_admin():
    while True:
        print("Area do Admin")
        print(" 1.Passageiros \n 2.Reservas \n 3.Voos \n 4.Avioes \n 0.Deslogar")
        adm_opc = int(input("Digite uma opcao: "))
        if adm_opc == 1:
            print("Admin - Passageiros \n 1.Listar Passageiros \n 2.Deletar Passageiro (ID) \n 0.Voltar")
            opc_p = int(input("Digite uma opcao: "))
        elif adm_opc == 2:
            print("Admin - Reservas \n 1.Listar Reservas \n 2.Deletar Reserva (ID) \n 0.Voltar")
            opc_r = int(input("Digite uma opcao: "))
        elif adm_opc == 3:
            print("Admin - Passageiros \n 1.Listar Passageiros \n 2.Deletar Passageiro \n 0.Voltar")
            opc_v = int(input("Digite uma opcao: "))
        elif adm_opc == 4:
            print("Admin - Passageiros \n 1.Listar Passageiros \n 2.Deletar Passageiro \n 0.Voltar")
            opc_a = int(input("Digite uma opcao: "))
        elif adm_opc == 0:
            break