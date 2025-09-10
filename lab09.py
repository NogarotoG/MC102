# MC102 - Algoritmos e Programação de Computadores
# Laboratório 09 - Anotador de Markdown
# Nome:Gustavo Nogaroto     
# RA:280893


# Leituras das especificações das formatações
italicos = input().strip().split()
negritos = input().strip().split()
cabecalhos = input().strip().split()
listas = list(map(int, input().strip().split()))

# Dicionário de cabecalhos (linha: nível)
cabecalho_dict = {}
for item in cabecalhos:
    linha, nivel = map(int, item.split(','))
    cabecalho_dict[linha] = nivel


# Leitura do texto e impressão do texto formatado 
n = int(input())

texto = [input() for _ in range(n)]

# Transformar listas em sets para buscas rápidas (foi fragmentado os topicos em relacão ao topico geral para facilitar)
italicos_set = set(italicos)
negritos_set = set(negritos)
listas_set = set(listas)

# Funcão para aplicar -formatacão de palavras-
def formatar_palavras(linha, italico, negrito):
    palavras = linha.split()
    for i in range(len(palavras)):
        palavra_original = palavras[i]
        palavra_limpa = palavra_original.strip('.,')
        palavra_lower = palavra_limpa.lower()

        if palavra_lower in negrito:
            nova = f"**{palavra_limpa}**"
        elif palavra_lower in italico:
            nova = f"*{palavra_limpa}*"
        else:
            continue

        if palavra_original.endswith('.') or palavra_original.endswith(','):
            nova += palavra_original[-1]
        palavras[i] = nova
    return ' '.join(palavras)

# Aplica as formatacões
i = 0
linha_atual = 1
while i < len(texto):
    linha = texto[i]

    # Formatação de cabecalho
    if linha_atual in cabecalho_dict:
        nivel = cabecalho_dict[linha_atual]
        linha = '#' * nivel + ' ' + linha

    # Verifica se a -linha atual- é o -início de uma lista-
    if linha_atual in listas_set:
        j = i
        contador = 1
        while j < len(texto) and texto[j].startswith('- '):
            # Retira o "- " e insere o número
            nova_linha = f"{contador}. {texto[j][2:]}"
            # Aplica formatacão de palavras
            nova_linha = formatar_palavras(nova_linha, italicos_set, negritos_set)
            texto[j] = nova_linha
            contador += 1
            j += 1
        i = j
        linha_atual = i + 1
        continue

    # Se -não- for -lista-, apenas aplicar -formatação de palavras-
    linha = formatar_palavras(linha, italicos_set, negritos_set)
    texto[i] = linha
    i += 1
    linha_atual += 1

# Impressão do texto formatado
for linha in texto:
    print(linha)
    
#obs: no textos ao longo do codigo foi utilizado para resumir a sentenca usando "-a-" e "-b-" (leiasse a depois b) para que facilitasse a leitura e construção do codigo ao longo do caminho.
