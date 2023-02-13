from Modelo import Filme, Serie, Playlist

vigadores = Filme('Vigadores - guerra infinita', 2018, 160)
end_game = Filme('Vigadores - fim de jogo',2019,160)

teen_wolf = Serie('teen wolf', 2018, 5)
discovery = Serie('star trek - discovery', 2019, 4)

lista_de_programas = [vigadores, end_game, teen_wolf, discovery]

playlist_fim_de_semana = Playlist('Playlist1', lista_de_programas)


for programa in playlist_fim_de_semana:
    print(programa)

print(f'Tamanho: {len(playlist_fim_de_semana)}')
