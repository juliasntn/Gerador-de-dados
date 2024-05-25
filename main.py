import pymysql
from faker import Faker

fake = Faker('pt-BR')

for i in range (0,100):
    conexao = pymysql.connect(
        host='SERVIDOR',
        user='root',
        password='root',
        database='cadastros'
    )


    cursor = conexao.cursor()


    nome = fake.name()
    data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d')
    endereco = fake.address().replace('\n', ', ')
    telefone = fake.phone_number()

    sql_insert = "INSERT INTO usuarios (nome, data_nascimento, endereco, telefone) VALUES (%s, %s, %s, %s)"
    valores_insert = (nome, data_nascimento, endereco, telefone)

    try:
        cursor.execute(sql_insert, valores_insert)
        conexao.commit()
        print("Dados inseridos com sucesso.")
    except pymysql.MySQLError as e:
        print(f"Erro ao inserir dados: {e}")
        conexao.rollback()

cursor.close()
conexao.close()
