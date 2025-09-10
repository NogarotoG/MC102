###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Corredor RPG
# Nome: Gustavo Nogaroto
# RA:280893
###################################################

# Leitura do corredor
corredor = input()

# Leitura dos valores dos dados e simulação do jogo
posicao = 0
vidas = 3
dados = []
indice_dado = 0


try:
    while True:
        dados.append(int(input()))
except EOFError:
    pass


requisitos_vitoria = {
    '1': 3,
    '2': 5,
    '3': 6
}

# Impressão da saída
while vidas > 0:
    if indice_dado >= len(dados):
        break

    movimento = dados[indice_dado]
    indice_dado += 1
    posicao += movimento

    if posicao >= len(corredor):
        print("O jogador chegou ao fim!")
        break

    local = corredor[posicao]

    if local in "123":
        if indice_dado >= len(dados):
            break

        combate = dados[indice_dado]
        indice_dado += 1

        if combate >= requisitos_vitoria[local]:
            corredor = corredor[:posicao] + '.' + corredor[posicao+1:]
        else:
            vidas -= 1
            posicao = 0

else:
    print("O jogador perdeu.")