from config.db import criar_conexao


def cadastrar_aviao (modelo,capacidade):
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

def listar_avioes(): 
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = "SELECT id_aviao, modelo, capacidade FROM aviao"
        cursor.execute(query)
        avioes = cursor.fetchall()
        if avioes:
            print("Lista de Passageiros")
            for a in avioes:
                print(f" ID:{a[0]} \n Nome:{a[1]} \n Email:{a[2]} \n Telefone:{a[3]}\n")
        else:
            print("Nenhum passageiro encontrado")
    except Exception as e:
        print(f"Erro ao encontrar passageiros: {e}")
    finally:
        cursor.close()
        conn.close()


def deletar_aviao():
    listar_avioes()
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = "DELETE FROM aviao WHERE id_aviao = %s"
        id = int(input("qual aviao voce deseja deletar (pelo id)?"))
        cursor.execute(query,(id,))
        conn.commit()
        print("Aviao deletado com sucesso")
    except Exception as e:
        print(f"erro ao deletar aviao: {e}")
    finally:
        cursor.close()
        conn.close()
