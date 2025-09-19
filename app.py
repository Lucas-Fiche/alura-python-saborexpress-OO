from modelos.restaurante import Restaurante

restaurante1 = Restaurante('Praça', 'Gourmet')
restaurante1.receber_avaliacao('Lucas', 10)
restaurante1.receber_avaliacao('Caio', 8)
restaurante1.receber_avaliacao('José', 2)

def main():
    Restaurante.listar_restaurantes()
    

if __name__ == '__main__':
    main()