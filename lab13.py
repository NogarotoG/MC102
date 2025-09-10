###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Agência de Marketing
# Nome: Gustavo Nogaroto
# RA: 280893
###################################################

# Leitura da entrada  
custo_maximo = float(input().strip())
num_influenciadores = int(input().strip())
influenciadores = []
for _ in range(num_influenciadores):
        linha = input().strip().split(',')
        custo = float(linha[0])
        seguidores = list(map(int, linha[1:]))
        influenciadores.append({"custo": custo, "seguidores": seguidores})

# foi fornecido no problema.

# Estratégia Ingênua
def estrategia_ingenua(influenciadores, custo_maximo):
    total_custo = 0
    seguidores_alcancados = set()
    candidatos = sorted(influenciadores, key=lambda i: (i["custo"], -len(i["seguidores"])))

    for i in candidatos:
        if total_custo + i["custo"] <= custo_maximo:
            total_custo += i["custo"]
            seguidores_alcancados.update(i["seguidores"])

    return total_custo, len(seguidores_alcancados)

#Ordena os influenciadores por: Custo mais baixo primeiro, Maior número de seguidores (em caso de empate no custo)
#Contrata influenciadores em ordem até atingir o custo máximo,Retorna o custo total e número de seguidores únicos alcançados


# Estratégia Atual
def estrategia_atual(influenciadores, custo_maximo):
    total_custo = 0
    seguidores_alcancados = set()

    def custo_beneficio(i):
        return i["custo"] / len(i["seguidores"])

    candidatos = sorted(influenciadores, key=lambda i: (custo_beneficio(i), -len(i["seguidores"])))

    for i in candidatos:
        if total_custo + i["custo"] <= custo_maximo:
            total_custo += i["custo"]
            seguidores_alcancados.update(i["seguidores"])

    return total_custo, len(seguidores_alcancados)

#Calcula o custo-benefício (custo por seguidor) de cada influenciador
#Melhor custo-benefício (menor valor primeiro),Maior número de seguidores (em caso de empate)
#Contrata em ordem até atingir o custo máximo,Retorna o custo total e número de seguidores únicos


# Estratégia Nova
def estrategia_nova(influenciadores, custo_maximo):
    total_custo = 0
    seguidores_alcancados = set()
    disponiveis = influenciadores[:]

    while True:
        melhores = []
        for i in disponiveis:
            novos = set(i["seguidores"]) - seguidores_alcancados
            if len(novos) > 0:
                custo_residual = i["custo"] / len(novos)
                melhores.append((custo_residual, -len(i["seguidores"]), i))

        if not melhores:
            break

        melhores.sort()
        contratado = None

        for _, _, i in melhores:
            if total_custo + i["custo"] <= custo_maximo:
                contratado = i
                break

        if contratado is None:
            break

        total_custo += contratado["custo"]
        seguidores_alcancados.update(contratado["seguidores"])
        disponiveis.remove(contratado)

    return total_custo, len(seguidores_alcancados)

#Em cada iteração:Calcula o custo residual (custo por novo seguidor) para cada influenciador disponível
#Menor custo residual, Maior número total de seguidores (em caso de empate)
#Contrata o melhor influenciador que ainda cabe no orçamento,Atualiza o conjunto de seguidores alcançados,Remove o influenciador contratado da lista de disponíveis
#O processo se repete até não haver mais influenciadores com seguidores novos ou orçamento esgotado


# Impressão da saída    
c1, s1 = estrategia_ingenua(influenciadores, custo_maximo)
print("Estratégia Ingênua: {:.1f}, {}".format(c1, s1))

c2, s2 = estrategia_atual(influenciadores, custo_maximo)
print("Estratégia Atual: {:.1f}, {}".format(c2, s2))

c3, s3 = estrategia_nova(influenciadores, custo_maximo)
print("Estratégia Nova: {:.1f}, {}".format(c3, s3))

#foi fornecido a impressão de saida, mas de forma basica, apenas complementado o que foi dado.

