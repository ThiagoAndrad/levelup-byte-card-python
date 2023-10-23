import mysql.connector

# Conectar ao servidor MySQL
conn = mysql.connector.connect(
    host="localhost",  # substitua pelo seu host
    user="root",  # substitua pelo seu usuário
    password=""  # substitua pela sua senha
)

# Criar um objeto cursor para executar comandos SQL
cursor = conn.cursor()

# Nome do schema a ser criado e usado
schema_name = 'byte_card'

try:
    # Apagar o schema se ele existir
    cursor.execute(f"DROP SCHEMA IF EXISTS {schema_name}")

    # Criar o schema
    cursor.execute(f"CREATE SCHEMA {schema_name}")

    # Usar o schema
    cursor.execute(f"USE {schema_name}")

    # Criar a tabela "cartoes"
    create_cartoes_table_query = """
    CREATE TABLE cartoes (
        id bigint unsigned NOT NULL AUTO_INCREMENT,
        numero varchar(30) NOT NULL,
        cvv varchar(3) NOT NULL,
        limite double(15,2) NOT NULL,
        validade date NOT NULL,
        cliente varchar(255) NOT NULL,
        status varchar(100) NOT NULL,
        PRIMARY KEY (id)
    )
    """
    cursor.execute(create_cartoes_table_query)

    # Inserir dados na tabela "cartoes"
    insert_data_cartoes_query = """
    INSERT INTO cartoes (id, numero, cvv, limite, validade, cliente, status)
    VALUES
        (1, '8888 2222 3333 4444', '564', 9999.00, '2023-08-26', 'Gal Costa', 'ATIVO'),
        (2, '7777 2222 3333 4444', '564', 6750.00, '2022-10-08', 'Luiz Gonzaga', 'INATIVO'),
        (3, '5555 6666 3333 4444', '014', 22500.00, '2025-10-14', 'Pixinguinha', 'ATIVO'),
        (4, '5555 2222 3333 4444', '312', 5000.00, '2024-10-16', 'Tom Jobim', 'ATIVO'),
        (5, '1111 2222 3333 4444', '564', 10000.00, '2024-10-01', 'Elis Regina', 'ATIVO'),
        (6, '3333 4444 5555 6666', '123', 12000.00, '2026-12-11', 'Leny Andrade', 'ATIVO')
    """
    cursor.execute(insert_data_cartoes_query)

    # Criar a tabela "compras"
    create_compras_table_query = """
    CREATE TABLE compras (
        id bigint unsigned NOT NULL AUTO_INCREMENT,
        valor double(15,2) NOT NULL,
        data datetime NOT NULL,
        estabelecimento varchar(1000) NOT NULL,
        categoria varchar(255) NOT NULL,
        cartao_id bigint unsigned NOT NULL,
        PRIMARY KEY (id),
        KEY cartao_fk (cartao_id),
        CONSTRAINT cartao_fk FOREIGN KEY (cartao_id) REFERENCES cartoes (id)
    )
    """
    cursor.execute(create_compras_table_query)

    # Inserir dados na tabela "compras"
    insert_data_compras_query = """
    INSERT INTO compras (id, valor, data, estabelecimento, categoria, cartao_id)
    VALUES
        (1, 100.00, '2023-09-15 09:42:03', 'Padaria', 'Alimentação', 1),
        (2, 500.00, '2023-06-18 17:42:03', 'Kart - Marios', 'Lazer', 1),
        (3, 1010.78, '2023-08-11 17:42:03', 'Mario & Luigi Ltda', 'Casa', 1),
        (4, 3723.32, '2023-09-13 18:42:03', 'Bossa Instrumentos', 'Lazer', 2),
        (5, 3000.00, '2023-09-17 18:42:03', 'Hospital Música da Alma', 'Saúde', 6),
        (6, 400.00, '2023-07-09 09:19:19', 'Samba Laboatório', 'Saúde', 1),
        (7, 500.00, '2023-07-18 17:42:03', 'Shopping - Centro de Compras', 'Lazer', 1),
        (8, 800.00, '2023-09-09 09:23:16', 'Restaurante Água do Mar', 'Alimentação', 2)
    """
    cursor.execute(insert_data_compras_query)

    # Confirmar as alterações no banco de dados
    conn.commit()

except mysql.connector.Error as err:
    print(f"Erro: {err}")

finally:
    # Fechar o cursor e a conexão
    cursor.close()
    conn.close()
