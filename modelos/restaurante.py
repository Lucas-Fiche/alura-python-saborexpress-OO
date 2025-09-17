class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
          for restaurante in Restaurante.restaurantes:
               print(f'Nome: {restaurante.nome} | Categoria: {restaurante.categoria} | Ativo: {restaurante.ativo}')  
        
restaurante_praca = Restaurante('Praça', 'Gourmet')
# restaurante_praca.nome = 'Praça'
# restaurante_praca.categoria = 'Italiana'

restaurante_pizza = Restaurante('Pizza Express', 'Italiana')
# restaurante_pizza.nome = 'Pizza Place'
# restaurante_pizza.categoria = 'Fast Food'

#print(dir(restaurante_praca))
#print(vars(restaurante_praca))

Restaurante.listar_restaurantes()