class Carro:
    def __init__(self, modelo, marca , cor, ano):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.vendido =  False
    
    def __str__(self):
        return f'Nome do Carro: {self.modelo} | Marca do Carro: {self.marca} | Cor do carro: {self.cor} | Ano do Carro: {self.ano} | Vendido: {self.vendido}'

carro1 = Carro('Tcross', 'Volkswagen' , 'Cinza', '2020')
carro2 = Carro('Camaro', 'Fiat', 'Amarelo', '2025')

print(carro1)
print(carro2)