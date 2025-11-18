from config.db import criar_conexao


def cadastrar_aviao_service(modelo,capacidade):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = "INSERT INTO aviao (modelo, capacidade) VALUES (%s,%s)"
        cursor.execute(query,(modelo, capacidade))
        conn.commit()
        print("Aviao Cadastrado")
    except Exception as e:
        print(f"Erro ao cadastrar aviao: {e}")
    finally:
        cursor.close()
        conn.close()

def listar_avioes_service(): 
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = "SELECT id_aviao, modelo, capacidade FROM aviao ORDER BY id_aviao"
        cursor.execute(query)
        avioes = cursor.fetchall()
        if avioes:
            print("Lista de Avioes\n")
            for a in avioes:
                print(f" ID_Aviao:{a[0]} \n Modelo:{a[1]} \n Capacidade:{a[2]} \n")
                print("-" * 40)
        else:
            print("Nenhum aviao encontrado")
    except Exception as e:
        print(f"Erro ao encontrar avioes: {e}")
    finally:
        cursor.close()
        conn.close()


def deletar_aviao_service(id):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = "DELETE FROM aviao WHERE id_aviao = %s"
        cursor.execute(query,(id,))
        conn.commit()
        print("Aviao deletado com sucesso")
    except Exception as e:
        print(f"erro ao deletar aviao: {e}")
    finally:
        cursor.close()
        conn.close()


def alterar_aviao_service(modelo,capacidade,id):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = "UPDATE aviao SET modelo =%s, capacidade=%s WHERE id_aviao = %s"
        cursor.execute(query,(modelo,capacidade,id))
        conn.commit()
        print("as informacoes do Aviao foram alteradas com sucesso")
    except Exception as e:
        print(f"erro ao alterar informacoes do aviao: {e}")
    finally:
        cursor.close()
        conn.close()