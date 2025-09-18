class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Titular da conta: {self._titular} | Saldo da conta: {self._saldo}'
    
    @property
    def titular(self):
        return f' -> Titular: {self._titular}'

    @property
    def saldo(self):
        return self._saldo

    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True
    
conta1 = ContaBancaria('Lucas', 40000)
conta2 = ContaBancaria('Caio', 12000)
conta3 = ContaBancaria('Carlos', 200)
conta4 = ContaBancaria('Catherine', 50000)

print(conta4.titular)
print(conta4._titular)

print(f'Antes de Ativar a conta: {conta3._ativo}')
ContaBancaria.ativar_conta(conta3)
print(f'Depois de Ativar a conta: {conta3._ativo}')

print(conta1, conta2)