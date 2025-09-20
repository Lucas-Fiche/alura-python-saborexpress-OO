from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante1 = Restaurante('Praça', 'Gourmet')

bebida1 = Bebida('Suco de Laranja', 5.0 , 'Grande')
bebida1.aplicar_desconto()

prato1 = Prato('Pãozinho', 2.0, 'Pão australiando com manteiga')
prato1.aplicar_desconto()

sobremesa1 = Sobremesa('Sorvete', 4.5, 'Gelado', 'Pequeno', 'Sorvete da Baccio')

restaurante1.adicionar_no_cardapio(bebida1)
restaurante1.adicionar_no_cardapio(prato1)
restaurante1.adicionar_no_cardapio(sobremesa1)


def main():
    restaurante1.exibir_cardapio
    

if __name__ == '__main__':
    main()


