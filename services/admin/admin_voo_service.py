from config.db import criar_conexao


def cadastrar_voo (nome, email, senha, telefone):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = "INSERT INTO voo (nome, email, senha, telefone) VALUES (%s,%s,%s,%s)"
        cursor.execute(query,(nome, email, senha, telefone))
        conn.commit()
        print("Passageiro Cadastrado")
    except Exception as e:
        print(f"Erro ao cadastrar passageiro: {e}")
    finally:
        cursor.close()
        conn.close()
