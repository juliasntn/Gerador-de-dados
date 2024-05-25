# Populando Banco de Dados MySQL com Dados Falsos Usando Python e Faker

Este repositório contém um script Python para popular um banco de dados MySQL com dados falsos utilizando a biblioteca Faker. O objetivo é gerar dados de teste realistas para a tabela `usuarios` no banco de dados `cadastros`.

## Pré-requisitos

Antes de executar o script, certifique-se de ter os seguintes componentes instalados:

1. Python 3.x
2. MySQL Server
3. Bibliotecas Python: `pymysql` e `Faker`

Você pode instalar as bibliotecas necessárias usando pip:

```sh
pip install pymysql faker
```

## Configuração do Banco de Dados

Certifique-se de que o MySQL Server esteja rodando e que você tenha um banco de dados chamado `cadastros` com uma tabela `usuarios`. A tabela `usuarios` deve ter a seguinte estrutura:

```sql
CREATE DATABASE cadastros;

USE cadastros;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    data_nascimento DATE NOT NULL,
    endereco TEXT NOT NULL,
    telefone VARCHAR(20) NOT NULL
);
```

## Configuração do Script

Atualize os parâmetros de conexão com o banco de dados no script conforme necessário:

```python
conexao = pymysql.connect(
    host='SERVIDOR',  # Endereço do servidor MySQL
    user='root',          # Nome de usuário do MySQL
    password='root',      # Senha do MySQL
    database='cadastros'  # Nome do banco de dados
)
```

## Executando o Script

Para executar o script, utilize o seguinte comando:

```sh
python populate_database.py
```

## Script Python

Aqui está o script completo (`populate_database.py`):

```python
import pymysql
from faker import Faker

fake = Faker('pt-BR')

for i in range(100):
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
```

## Notas

- **Conexão por Iteração:** O script cria uma nova conexão com o banco de dados em cada iteração do loop. Isso pode ser otimizado abrindo a conexão antes do loop e fechando-a após o loop.
- **Rollback em Caso de Erro:** Em caso de erro durante a inserção dos dados, o script faz um rollback para garantir que a transação seja revertida.
- **Número de Registros:** O script está configurado para inserir 100 registros. Você pode ajustar este valor conforme necessário.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou abrir issues para relatar problemas.
