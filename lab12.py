###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - A Grande Caçada aos Tesouros Perdidos
# Nome: Gustavo Nogaroto    
# RA: 280893
###################################################

# Leitura da entrada
M, N = map(int, input().split())
matriz = []
for _ in range(M):
    linha = input().strip().split()
    matriz.append(linha)
P = int(input())

# Se P for ímpar, então o maior perímetro possível é P - 1 (condição logica)
if P % 2 != 0:
    P -= 1

max_tesouros = 0

#  m_(ij) de ----prefixo---- para contar tesouros o mais rapido 
prefixo = [[0] * (N + 1) for _ in range(M + 1)]
for i in range(M):
    for j in range(N):
        prefixo[i + 1][j + 1] = prefixo[i + 1][j] + prefixo[i][j + 1] - prefixo[i][j]
        if matriz[i][j] == 'X':
            prefixo[i + 1][j + 1] += 1

# Função para contar tesouros em um retângulo usando +  -----prefixos-------
def contar_tesouros(l1, c1, l2, c2):
    return (
        prefixo[l2 + 1][c2 + 1]
        - prefixo[l1][c2 + 1]
        - prefixo[l2 + 1][c1]
        + prefixo[l1][c1]
    )

# Testar ∀ retangulos 
for i in range(M):
    for j in range(N):
        for i2 in range(i, M):
            for j2 in range(j, N):
                altura = i2 - i + 1
                largura = j2 - j + 1
                perimetro = 2 * (altura + largura)
                if perimetro <= P:
                    tesouros = contar_tesouros(i, j, i2, j2)
                    if tesouros > max_tesouros:
                        max_tesouros = tesouros
#Saída
print(max_tesouros)
