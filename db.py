import mysql.connector as myc

class conexaoDB:
    def __init__(self, host, username, password, database):
        self.connection = myc.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()
    #Inserir Novo Usuário
    def inserirUsuario(self, cpf, nome, sobrenome, telefone, email, data_nascimento):
        query = "INSERT INTO Cinema.Usuario (CPF_CNPJ, PrimeiroNome, Sobrenome, Telefone, Email, DataNascimento) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (cpf, nome, sobrenome, telefone, email, data_nascimento)
        self.cursor.execute(query, values)
        self.connection.commit()
        print("Usuário inserido com sucesso!")
    
    #Consultar Tabela
    def consultarTabela(self):
        query = "SELECT * FROM Cinema.Usuario"
        self.cursor.execute(query)
        users = self.cursor.fetchall()
        for user in users:
            print(user)

    def fecharConexao(self):
        self.cursor.close()
        self.connection.close()

# conexão ao banco de dados
host = "dbprojetologico.c24e1vlqhrlr.us-east-1.rds.amazonaws.com"
username = "professor"
password = "professor"
database = "Cinema"

db_manager = conexaoDB(host, username, password, database)
db_manager.inserirUsuario('202100011708', 'Matheus', 'Nascimento', '79999452215', 'matheusgenil@gmail.com', '2003-04-28')
db_manager.consultarTabela()
db_manager.fecharConexao()
