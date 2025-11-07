from config.db import criar_conexao


def inserir_passageiro (nome, email, senha, telefone):
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO passageiro (nome, email, senha, telefone) VALUES (%s,%s,%s)"
        cursor.execute(query,(nome, email, senha, telefone))
        conn.commit()
        print("Passageiro Cadastrado")
    except Exception as e:
        print(f"Erro ao cadastrar passageiro: {e}")
    finally:
        cursor.close()
        conn.close()

def listar_passageiros(): 
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM passageiro"
        cursor.execute(query)
        passageiros = cursor.fetchall()
        if passageiros:
            for p in passageiros:
                print(p)
        else:
            print("Nenhum passageiro encontrado")
    except Exception as e:
        print(f"Erro ao encontrar passageiros: {e}")
    finally:
        cursor.close()
        conn.close()