from Modelo import Filme, Serie

vigadores = Filme('Vigadores - guerra infinita', 2018, 160)
end_game = Filme('Vigadores - fim de jogo',2019,160)

teen_wolf = Serie('teen wolf', 2018, 5)
discovery = Serie('star trek - discovery', 2019, 4)

playlist = [vigadores, end_game, teen_wolf, discovery]


for programa in playlist:
    programa.dar_likes()

for programa in playlist:
    print(programa)

