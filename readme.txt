# Pacman
Baseado no clássico Pacman, que marcou a geração que cresceu nos anos 80, criamos esse projeto, que busca simular, de maneira análoga, o jogo tão estrelado nas últimas décadas.

# Criado por:
- Arthur Tamm
- Guilherme Lemos
- Vitor Caixeta

# Files
- O codigo está separado em diferentes pastas e arquivos. Primeiramente, temos a pasta assets que contém os recursos de imagem, som e fonte do jogo. Em seguida, está a pasta 'Maps' que contém os mapas disponíveis no jogo. 

- Outra pasta que criamos é a 'Sprites', que contém arquivos de todas as classes criadas no jogo, sendo elas: Coin, para as moesas; Ghost, para os fantasmas; Pacman, para o próprio Pacman; Wall, para as barreiras do mapa do jogo.

- Já nos arquivos em python, o primeiro é o "assets", que carrega os recursos sonoros, de imagem e de som do jogo. Em seguida, temos o "settings" que contempla as informações de tamanho, como o tamanho da tela e dos sprites. 

- Os arquivos "init_screen", possui o código da tela final do menu início. Já os arquivos "final_screen" e "win_screen" possuem, respectivamente, os códigos de Gameover, em caso de derrota na partida, e de vitória.

- O arquivo "game_screen" possui a lógica do jogo em si, indicando o que deve acontecer a cada movimento realizado. 

- Por último, mas não menos importante, temos o arquivo "Main" que deve ser executado quando desejar-se jogar o jogo. Esse é o código que apenas gerencia o que vai ser rodado em cada estado do jogo.


# Referências

- Tutorial de pygame kidscancode : https://www.youtube.com/watch?v=3UxnelT9aCo&list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw&index=37

- Tutorial de animação de rotação pygame: https://www.youtube.com/watch?v=eGsMMpAglIg
