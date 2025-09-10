###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 08 - Estudando Cifras
# Nome:Gustavo Nogaroto
# RA:280893
###################################################

# Leitura de dados
entrada = input()

# Lista de notas em ordem -cíclica-
notas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
vizinho = {
    'A': ['G', 'B'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'F'],
    'F': ['E', 'G'],
    'G': ['F', 'A']
}

# Função para extrair -acordes da string-
def extrair_acordes(s):
    i = 0
    acordes = []
    while i < len(s):
        acorde = s[i]  # nota base: usado mais adiante 
        i += 1
        if i < len(s) and s[i] in ['#', 'b']:
            acorde += s[i]
            i += 1
        if i < len(s) and s[i] in ['m', 'M']:
            acorde += s[i]
            i += 1
        acordes.append(acorde)
    return acordes

# Função para extrair a -nota base de um acorde-
def nota_base(acorde):
    return acorde[0]

# Processamento de dados
acordes = extrair_acordes(entrada)
resultado = [acordes[0]]
ultima_nota = nota_base(acordes[0])

for acorde in acordes[1:]:
    nota = nota_base(acorde)
    if nota == ultima_nota or nota in vizinho[ultima_nota]:
        continue
    resultado.append(acorde)
    ultima_nota = nota

# Saída de dados
print(" ".join(resultado))