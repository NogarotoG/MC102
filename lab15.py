###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 15 - Guardiões da Galáxia
# Nome:Gustavo Nogaroto
# RA:280893 
###################################################

def captura(mapa, i, j, visitados, saltos): #Função captura: Verificação de limites: A função primeiro verifica se a posição (i, j) está dentro dos limites do mapa.
    if i < 0 or i >= len(mapa) or j < 0 or j >= len(mapa[0]):
        return 0
    if (i, j) in visitados:
        return 0
    if mapa[i][j] == '#':
        return 0
    
    visitados.add((i, j))
    total = 0
   # Posições visitadas ou bloqueadas: Se a posição já foi visitada ou é um bloqueio (#), retorna 0.
    if mapa[i][j] == '*':
        total += 1
    elif mapa[i][j].isdigit():
        # Encontrar a posição correspondente do salto
        for x in range(len(mapa)):
            for y in range(len(mapa[x])):
                if mapa[x][y] == mapa[i][j] and (x != i or y != j): #(poderia ser qualquer letra, matematicamente (x,y) para mapa e melhor) )
                    # Teleportar para (x, y)
                    total += captura(mapa, x, y, visitados, saltos)
                    break
            else:
                continue
            break
    
    # Movimentos nas quatro direções (recursão)
    total += captura(mapa, i+1, j, visitados, saltos) # Movimento para baixo
    total += captura(mapa, i-1, j, visitados, saltos) # Movimento para cima
    total += captura(mapa, i, j+1, visitados, saltos) # Movimento para direita
    total += captura(mapa, i, j-1, visitados, saltos) # Movimento para esquerda
    
    return total

# Leitura da entrada
n = int(input())
mapa = [list(input()) for _ in range(n)]

# Encontrar a posição inicial da nave (N)
pos_i, pos_j = 0, 0
for i in range(n):
    for j in range(len(mapa[i])):
        if mapa[i][j] == 'N':
            pos_i, pos_j = i, j
            break

# Simulação do jogo
visitados = set()
saltos = {}  # Não é necessário pré-processar os saltos, pois são tratados na recursão
#Evita loops infinitos:
#(i) O conjunto visitados garante que cada posição seja verificada apenas uma vez.
#(ii) Os saltos são tratados de forma que a nave não fique presa em um ciclo de teletransporte.
itens = captura(mapa, pos_i, pos_j, visitados, saltos)

#saída
print(itens)

#A função captura é chamada com a posição inicial, um conjunto vazio de posições visitadas e um dicionário vazio para saltos (não utilizado diretamente, pois os saltos são tratados dentro da função).
#O código é recursivo.Ele explora todas as direções possíveis a partir de N, conta os itens * e trata corretamente os saltos e bloqueios.