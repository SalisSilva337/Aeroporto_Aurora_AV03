from config.db import criar_conexao


def inserir_passageiro (nome, email, telefone):
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO passageiro (nome, email, telefone) VALUES (%s,%s,%s)"
        cursor.execute(query,(nome,email,telefone))
        conn.commit()
        print("Passageiro Cadastrado")
    except Exception as e:
        print(f"Erro ao cadastrar passageiro: {e}")
    finally:
        cursor.close()
        conn.close()