import bcrypt
from config.db import criar_conexao

def gerar_admin_padrao_service():
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM passageiro WHERE email = %s", ('admin@email.com',))
        admin = cursor.fetchone()
        if not admin:
            salt = bcrypt.gensalt()               # custo padrão 12
            hashed = bcrypt.hashpw("admin123".encode('utf-8'), salt).decode('utf-8')
            cursor.execute(
                "INSERT INTO passageiro (nome, email, telefone, senha) VALUES (%s, %s, %s, %s)",
                ("admin","admin@email.com","0000000", hashed)
            )
            conn.commit()
            print("Admin gerado com sucesso!")
        else:
            pass
    except Exception as e:
        print("erro:", e)
    finally:
        cursor.close()
        conn.close()


def listar_passageiros_service(): 
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = "SELECT id_passageiro, nome, email, telefone FROM passageiro"
        cursor.execute(query)
        passageiros = cursor.fetchall()
        if passageiros:
            print("Lista de Passageiros\n")
            for p in passageiros:
                if p[1] != "admin" and p[2] != "admin@email.com":
                    print(f" ID:{p[0]} \n Nome:{p[1]} \n Email:{p[2]} \n Telefone:{p[3]}\n")
        else:
            print("Nenhum passageiro encontrado")
    except Exception as e:
        print(f"Erro ao encontrar passageiros: {e}")
    finally:
        cursor.close()
        conn.close()


def deletar_passageiro_service(id):
    listar_passageiros_service()
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = "DELETE FROM passageiro WHERE id_passageiro = %s"
        cursor.execute(query,(id,))
        conn.commit()
        print("Passageiro deletado com sucesso")
    except Exception as e:
        print(f"erro ao deletar passageiro: {e}")
    finally:
        cursor.close()
        conn.close()



   