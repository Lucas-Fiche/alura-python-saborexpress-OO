class ClienteBanco:
    clientes = []
    def __init__(self, nome, idade, telefone, cpf, email):
        self._nome = nome
        self._idade = idade
        self._telefone = telefone
        self._cpf = cpf
        self._email = email
        ClienteBanco.clientes.append(self._nome)

    @classmethod
    def listar_clientes(cls):
        print('Clientes do banco >')
        for cliente in cls.clientes:
            print(cliente)

    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = cls(titular, saldo_inicial)
        return conta

cliente1 = ClienteBanco('Lucas', 24, 9999-2222, 12345678912, 'lucas@gmail.com')
cliente2 = ClienteBanco('José', 35, 9999-3333, 98765432109, 'jose@gmail.com')
cliente3 = ClienteBanco('Juliana', 18, 9999-4444, 67812394567, 'juliana@gmail.com')

ClienteBanco.listar_clientes()
conta_cliente1 = ClienteBanco.criar_conta('Ana', 2000)