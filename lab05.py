###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Filtro de Carros
# Nome: Gustavo Nogaroto 
# RA:280893 
###################################################

# Leitura das especificações do cliente
K = int(input())
tem_ar = input()
tem_dir_hid = input()
quant_cil_li, quant_cil_ls = map(int, input().split())
tem_vid_el = input()
cap_mal_li, cap_mal_ls = map(int, input().split())
tem_camb_auto = input()
quant_cav_li, quant_cav_ls = map(int, input().split())
quant_gar_li, quant_gar_ls = map(int, input().split())
tem_abs = input()
quant_lug_li, quant_lug_ls = map(int, input().split())

# Leitura do número de modelos
N = int(input())

# Lista para armazenar os modelos selecionados
modelos_selecionados = []

# Função auxiliar para verificar característica binária
def verifica_binario(esperado, valor):
    if esperado == 'I':
        return True
    return esperado == valor

# Processamento de cada modelo
for _ in range(N):
    nome = input()
    carac_binarias = []
    carac_numericas = []

    carac_binarias.append(input())  # ar
    carac_binarias.append(input())  # dir hid
    carac_numericas.append(int(input()))  # cilindradas
    carac_binarias.append(input())  # vidros el
    carac_numericas.append(int(input()))  # porta malas
    carac_binarias.append(input())  # câmbio auto
    carac_numericas.append(int(input()))  # cavalos
    carac_numericas.append(int(input()))  # garantia
    carac_binarias.append(input())  # freios ABS
    carac_numericas.append(int(input()))  # lugares

    correspondencias = 0

    # Verificações das características
    if verifica_binario(tem_ar, carac_binarias[0]):
        correspondencias += 1
    if verifica_binario(tem_dir_hid, carac_binarias[1]):
        correspondencias += 1
    if quant_cil_li <= carac_numericas[0] <= quant_cil_ls:
        correspondencias += 1
    if verifica_binario(tem_vid_el, carac_binarias[2]):
        correspondencias += 1
    if cap_mal_li <= carac_numericas[1] <= cap_mal_ls:
        correspondencias += 1
    if verifica_binario(tem_camb_auto, carac_binarias[3]):
        correspondencias += 1
    if quant_cav_li <= carac_numericas[2] <= quant_cav_ls:
        correspondencias += 1
    if quant_gar_li <= carac_numericas[3] <= quant_gar_ls:
        correspondencias += 1
    if verifica_binario(tem_abs, carac_binarias[4]):
        correspondencias += 1
    if quant_lug_li <= carac_numericas[4] <= quant_lug_ls:
        correspondencias += 1

    # Verifica se modelo atende ao mínimo de características
    if correspondencias >= K:
        modelos_selecionados.append(nome)

# Impressão dos modelos selecionados
print("Modelos selecionados:")
for modelo in modelos_selecionados:
    print(modelo)
