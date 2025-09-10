###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Quadrados Mágicos em uma Matriz
# Nome:Gustavo Nogaroto
# RA:280893
###################################################

# Leitura de dados
m = int(input()) #poderia ser qualquer outra letra de entrada utilizaremos (m) e (K)
matriz = []

for _ in range(m):
    linha = list(map(int, input().split()))
    matriz.append(linha)

# Função para verificar se uma sub_m 3x3 é mágica
def eh_quadrado_magico(i, j):
    # Extrai os 9 elementos da sub_m 3x3 com canto superior esquerdo em (i, j)
    quad = [matriz[i + x][j:j + 3] for x in range(3)]

    # Soma mágica de referência: soma da primeira linha
    soma = sum(quad[0])

    # Verifica linhas(1), colunas(2) e diagonais(3) 
    
    #(1) 
    for k in range(3):
        if sum(quad[k]) != soma:
            return False

    #(2)
    for k in range(3):
        if quad[0][k] + quad[1][k] + quad[2][k] != soma:
            return False

    #(3)
    if quad[0][0] + quad[1][1] + quad[2][2] != soma:
        return False
    if quad[0][2] + quad[1][1] + quad[2][0] != soma:
        return False

    return True

# Processamento de dados
contador = 0

# Percorre todas as possíveis sub_m (fragmentação) 3x3 dentro da matriz m x m
for i in range(m - 2):
    for j in range(m - 2):
        if eh_quadrado_magico(i, j):
            contador += 1

# Saída de dados
print(f"Número de quadrados mágicos: {contador}")
