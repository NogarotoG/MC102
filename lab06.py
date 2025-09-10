###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 06 - Roleta da Sorte
# Nome: Gustavo Nogaroto 
# RA: 280893 
###################################################

# Leitura de dados
n = int(input().strip())  
objetos = []
for _ in range(n):
    linha = input().strip().split(maxsplit=1)
    objetos.append((int(linha[0]), linha[1]))  # (ID, Nome)

k = int(input().strip())  
forcas = list(map(int, input().strip().split())) 

# Verificação se é possível realizar o sorteio
if k > n:
    print("Não foi possível realizar o sorteio")
else:
    sorteados = set()  # IDs já sorteados
    resultado = []     # Lista com os prêmios sorteados
    posicao_atual = -1 # Inicia antes do primeiro prêmio

    for forca in forcas:
        atual_forca = forca

        while True:
            # Calcula a nova posição de forma circular
            posicao_atual = (posicao_atual + atual_forca) % n
            premio_id, premio_nome = objetos[posicao_atual]

            # Verifica se o prêmio já foi sorteado
            if premio_id not in sorteados:
                sorteados.add(premio_id)
                resultado.append(f"{premio_id}-{premio_nome}")
                break
            else:
                # Reduz força se possível
                if atual_forca > 1:
                    atual_forca -= 1
                else:
                    atual_forca = 1  # Continua com força 1

    # Impressão da saída
    print(' '.join(resultado))
