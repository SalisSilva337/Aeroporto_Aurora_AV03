from config.db import criar_conexao

def cadastrar_reserva_service(id_voo, user, classe, metodo_pagamento, quantidade_passageiros, data):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = "INSERT INTO reserva (id_voo, id_passageiro,classe, metodo_pagamento, quantidade_passageiros, data) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,(id_voo, user[0],classe, metodo_pagamento, quantidade_passageiros, data))
        conn.commit()
        print("Reserva cadastrada")
    except Exception as e:
        print(f"Erro ao cadastrar reserva: {e}")
    finally:
        cursor.close()
        conn.close()


def deletar_reserva_service(id_passageiro):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = "DELETE FROM reserva WHERE id_passageiro = %s"
        cursor.execute(query,(id_passageiro,))
        conn.commit()
        print("Reserva deletada com sucesso")
    except Exception as e:
        print(f"erro ao deletar reserva: {e}")
    finally:
        cursor.close()
        conn.close()