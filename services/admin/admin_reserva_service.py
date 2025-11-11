from config.db import criar_conexao


def listar_reservas_service(): 
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = "SELECT id_reserva, id_passageiro, id_voo, classe, metodo_Pagamento, Quantidade_Passageiros, data FROM reserva"
        cursor.execute(query)
        reservas = cursor.fetchall()
        if reservas:
            print("Lista de Passageiros\n")
            for r in reservas:
                print(f" ID Reserva:{r[0]} \n ID passageiro:{r[1]} \n ID voo:{r[2]} \n Classe:{r[3]}\n Metodo de Pagamento:{r[4]}\n Quantidade de Passageiros:{r[5]}\n Data:{r[6]}\n")
        else:
            print("Nenhuma reserva encontrado")
    except Exception as e:
        print(f"Erro ao encontrar reservas: {e}")
    finally:
        cursor.close()
        conn.close()