import bcrypt
from config.db import criar_conexao

def gerar_admin_padrao():
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM passageiro WHERE email = %s", ('admin@email.com',))
        admin = cursor.fetchone()
        if not admin:
            salt = bcrypt.gensalt()               # custo padrão 12
            hashed = bcrypt.hashpw("admin123".encode('utf-8'), salt).decode('utf-8')
            cursor.execute(
                "INSERT INTO passageiro (nome, email, telefone, senha) VALUES (%s, %s,%s,%s)",
                ("admin","admin@email.com","0000000", hashed)
            )
            conn.commit()
            print("Admin gerado com sucesso!")
        else:
            print("admin ja existe")
    except Exception as e:
        print("erro:", e)
    finally:
        cursor.close()
        conn.close()
