from config.db import criar_conexao
from config.crypt import checar_password, criptografar


def cadastrar_passageiro (nome, email, senha, telefone):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        senha = criptografar(senha)
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
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = "SELECT * FROM passageiro"
        cursor.execute(query)
        passageiros = cursor.fetchall()
        if passageiros:
            for p in passageiros:
                print(str(p))
        else:
            print("Nenhum passageiro encontrado")
    except Exception as e:
        print(f"Erro ao encontrar passageiros: {e}")
    finally:
        cursor.close()
        conn.close()


def logar_passageiro(email, password):
    
    con = criar_conexao()
    cursor = con.cursor()
    try:
        query = "SELECT * FROM passageiro WHERE email=%s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()
        if user and checar_password(password, bytes(user[4])):
            return user
        return None
    except Exception as e:
        print(e)
