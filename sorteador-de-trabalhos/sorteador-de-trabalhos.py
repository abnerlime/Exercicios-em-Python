
import random

participantes = []
temas = []

for n in range(3):
    nome = input('Digite o nome: ')
    participantes.append(nome)

for n in range(3):
    tema = input('Informe o tema: ')
    temas.append(tema)

random.shuffle(temas)
for n in range(3):
    print(f'{participantes[n]} para o tema: {temas[n]}')

# Se desejar salvar o resultado do sorteio:
while True:
    opcao = int(input('Deseja salvar o resultado do sorteio? \n1 - Sim\n2 - Não\n'))
    if (opcao == 1):
        with open("Resultado_sorteio.txt", "w", encoding = "utf-8") as arquivo:
            arquivo.write("Resultado do Sorteio\nParticipante - Tema: \n")
            for n in range(len(participantes)):
                linha = f"{participantes[n]} - {temas[n]}\n"
                arquivo.write(linha)
        print("Resultado salvo em 'Resultado_sorteio.txt'!")
        break
    elif (opcao == 2):
        print('Programa finalizado!')
        break
    else:
        print('Selecione uma opção válida!')
        continue