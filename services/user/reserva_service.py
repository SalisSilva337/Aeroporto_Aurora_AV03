from config.db import criar_conexao

def cadastrar_reserva_service (ID_voo, classe, metodo_pagamento, Quantidade_Passageiros, Data):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = "INSERT INTO voo (ID_voo, classe, metodo_pagamento, Quantidade_Passageiros, Data) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(query,(ID_voo, classe, metodo_pagamento, Quantidade_Passageiros, Data))
        conn.commit()
        print("Reserva cadastrada")
    except Exception as e:
        print(f"Erro ao cadastrar reserva: {e}")
    finally:
        cursor.close()
        conn.close()


def deletar_reserva_service(id):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = "DELETE FROM reserva WHERE id_reserva = %s"
        cursor.execute(query,(id,))
        conn.commit()
        print("Reserva deletada com sucesso")
    except Exception as e:
        print(f"erro ao deletar reserva: {e}")
    finally:
        cursor.close()
        conn.close()