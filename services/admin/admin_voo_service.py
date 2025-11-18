from config.db import criar_conexao


def cadastrar_voo_service (id_aviao, local_partida, local_destino, duracao):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = "INSERT INTO voo (id_aviao, local_partida, local_destino, duracao) VALUES (%s,%s,%s,%s)"
        cursor.execute(query,(id_aviao,local_partida, local_destino, duracao))
        conn.commit()
        print("Voo Cadastrado")
    except Exception as e:
        print(f"Erro ao cadastrar voo: {e}")
    finally:
        cursor.close()
        conn.close()


def listar_voo_service(): 
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = "SELECT id_voo, id_aviao, local_partida, local_destino, duracao FROM voo ORDER BY id_voo"
        cursor.execute(query)
        avioes = cursor.fetchall()
        if avioes:
            print("Lista de Voo\n")
            for a in avioes:
                print(f"\n ID_voo:{a[0]} \n ID_Aviao:{a[1]} \n Local Partida:{a[2]} \n Local Destino:{a[3]} \n Duracao:{a[4]}")
                print("-" * 40)
        else:
            print("Nenhum aviao encontrado")
    except Exception as e:
        print(f"Erro ao encontrar avioes: {e}")
    finally:
        cursor.close()
        conn.close()

def deletar_voo_service(id):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = "DELETE FROM voo WHERE id_voo = %s"
        cursor.execute(query,(id,))
        conn.commit()
        print("Voo deletado com sucesso")
    except Exception as e:
        print(f"erro ao deletar voo: {e}")
    finally:
        cursor.close()
        conn.close()

def alterar_voo_service(id_voo,id_aviao, local_partida, local_destino, duracao):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = "UPDATE voo SET id_aviao =%s, local_partida=%s,local_destino=%s, duracao=%s WHERE id_voo = %s"
        cursor.execute(query,(id_aviao, local_partida, local_destino, duracao,id_voo))
        conn.commit()
        print("as informacoes do Voo foram alteradas com sucesso")
    except Exception as e:
        print(f"erro ao alterar informacoes do voo: {e}")
    finally:
        cursor.close()
        conn.close()
