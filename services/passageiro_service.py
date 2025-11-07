from config.db import criar_conexao

def inserir_passageiro (Nome, Email, Telefone):
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO passageiro (Nome, Email, Telefone) VALUES (%s,%s,%s)"
        cursor.execute(query,(Nome,Email,Telefone))
        conn.commit()
        print("Passageiro Cadastrado")
    except Exception as e:
        print(f"Erro ao cadastrar passageiro: {e}")
    finally:
        cursor.close()
        conn.close()