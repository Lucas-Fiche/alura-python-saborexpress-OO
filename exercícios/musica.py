class Musica:

    musicas = []

    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def __str__(self):
        return f' Nome: {self.nome} | Artista: {self.artista} | Duração: {self.duracao}'
    
    def listar_musicas():
        for musica in Musica.musicas:
            print(f' Nome: {musica.nome} | Artista: {musica.artista} | Duração: {musica.duracao}')

logo_eu = Musica('Logo Eu', 'Jorge e Mateus', 2)
# logo_eu.nome = 'Logo Eu'
# logo_eu.artista = 'Jorge e Mateus'
# logo_eu.duracao = 2

eu_te_devoro = Musica('Eu te Devoro', 'Djavan', 5)
# eu_te_devoro.nome = 'Eu te Devoro'
# eu_te_devoro.artista = 'Djavan'
# eu_te_devoro.duracao = 5

amei_te_ver = Musica('Amei te Ver', 'Thiago Iorc', 4)
# amei_te_ver.nome = 'Amei te Ver'
# amei_te_ver.artista = 'Thiago Iorc'
# amei_te_ver.duracao = 4

Musica.listar_musicas()
