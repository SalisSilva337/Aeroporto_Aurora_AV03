from config.db import criar_conexao


def inserir_tripulacao_ao_voo_service (id_voo):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = "INSERT INTO tripulacao (id_voo) VALUES (%s)"
        cursor.execute(query,(id_voo))
        conn.commit()
        print("Tripulacao Cadastrada")
    except Exception as e:
        print(f"Erro ao cadastrar tripulacao: {e}")
    finally:
        cursor.close()
        conn.close()

def listar_tripulacao_service(): 
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = "SELECT t.id_tripulacao, a.Nome_Aviao AS Aviao, v.Local_Partida, v.Local_Destino FROM Tripulacao t JOIN Voo v ON t.id_voo = v.id_voo JOIN Aviao a ON v.id_aviao = a.id_aviao"
        cursor.execute(query)
        resultados = cursor.fetchall()
        if resultados:
            print("\n Lista de Tripulações em cada Voo\n")
            for linha in resultados:
                print(f"ID Tripulação: {linha[0]}")
                print(f"Avião: {linha[1]}")
                print(f"Local de Partida: {linha[2]}")
                print(f"Local de Destino: {linha[3]}")
                print("-" * 40)
        else:
            print("Nenhuma tripulação encontrada.")
            
    except Exception as e:
        print(f"Erro ao listar tripulações: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def remover_tripulacao_service(id):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = "DELETE FROM tripulacao WHERE id_tripulacao = %s"
        cursor.execute(query,(id,))
        conn.commit()
        print("Tripulacao removida com sucesso")
    except Exception as e:
        print(f"erro ao remover tripulacao: {e}")
    finally:
        cursor.close()
        conn.close()