from config.db import criar_conexao
from config.crypt import checar_password, criptografar


def cadastrar_passageiro (nome, email, senha, telefone):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        senha = criptografar(senha)
        query = "INSERT INTO passageiro (nome, email, senha, telefone) VALUES (%s,%s,%s,%s)"
        cursor.execute(query,(nome, email, senha, telefone))
        conn.commit()
        print("Passageiro Cadastrado")
    except Exception as e:
        print(f"Erro ao cadastrar passageiro: {e}")
    finally:
        cursor.close()
        conn.close()

def logar_passageiro(email, password):
    
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = "SELECT * FROM passageiro WHERE email=%s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()
        if user and checar_password(password, bytes(user[4])):
            return user
        return None
    except Exception as e:
        print(e)
    finally: 
        conn.close()
        cursor.close()



def email_existe(email):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM passageiro WHERE email = %s", (email,))
        existe = cursor.fetchone() is not None
        return existe
    except Exception as e:
        print(e)
    finally:
        conn.close()
        cursor.close()
    
