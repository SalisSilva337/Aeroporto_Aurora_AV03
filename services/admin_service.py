from config.db import criar_conexao

def gerar_admin_padrao():
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuario WHERE email = 'admin@email.com'")
        admin = cursor.fetchone()
        if not admin:
            cursor.execute("INSERT INTO usuario (email, password) VALUES (%s, %s)", ('admin@email.com', 'admin123'))
            conn.commit()
            print("Admin gerado com sucesso!")
        else:
            print("admin ja existe")
    except Exception as e:
        print("erro")     
    finally:
        cursor.close()
        conn.close()