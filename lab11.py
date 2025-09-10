# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Organizando a Agenda da Semana
# Nome:Gustavo Nogaroto 
# RA:280893

# Leitura da agenda inicial
agenda = [input().split() for _ in range(5)]

# Mapeamento dos dias da semana para índice
dias = {
    "Segunda": 0,
    "Terça": 1,
    "Quarta": 2,
    "Quinta": 3,
    "Sexta": 4
}

# Função para imprimir a agenda
def print_agenda(agenda):
    print(' '.join([j.ljust(10) for j in ['Horário', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']]))
    horario = list(range(8, 19))
    for i in range(10):
        saida = [(str(horario[i]) + '-' + str(horario[i+1])).ljust(10)]
        saida += [agenda[j][i].ljust(10) for j in range(5)]
        print(' '.join(saida))

# Leitura de dados
n = int(input())

# Processamento de dados
for _ in range(n):
    comando = input().split()

    if comando[0] == "Remover":
        dia = dias[comando[1]]
        hora_ini = int(comando[2])
        hora_fim = int(comando[3])
        for i in range(hora_ini - 8, hora_fim - 8):
            agenda[dia][i] = "Livre"

    elif comando[0] == "Adicionar":
        atividade = comando[1]
        duracao = int(comando[2])
        alocado = False

        for dia in range(5):
            for inicio in range(11 - duracao):  # - duracao garante que não ultrapasse o limite
                bloco = agenda[dia][inicio:inicio+duracao]
                if all(h == "Livre" for h in bloco):
                    for i in range(inicio, inicio+duracao):
                        agenda[dia][i] = atividade
                    alocado = True
                    break
            if alocado:
                break

        if not alocado:
            print(f"Não foi possível alocar a atividade {atividade}")

# Saída de dados
print_agenda(agenda)
