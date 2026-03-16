##
Sorteador de Temas em Python 

Criei esse sorteador a partir do desafio de um curso em python.  
O desafio proposto:  
"Um professor quer sortear um dos seus quatro alunos para apagar o quadro.  
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela  
 o nome do escolhido."

Quando concluí o que foi solicitado no exercício, resolvi implementar novas funções.  
Então esolvi criar um sorteador de trabalhos para ser usado na Faculdade.  
O programa funciona como um sorteador que pede ao usuário os nomes do participantes  
e sem seguida os temas de trabalhos propostos pelo professor.
Usei um laço de repetição para preencher  
as duas listas (Participantes[] e Temas[]).  
Depois de preenchidas as listas, usei o módulo 'random.shuffle()' para embaralhar  
o temas dos trabalhos preenchidos pelo usuário. 
Em seguida, criei um laço de repetição para imprimir o resultado do sorteio. 

Criei uma estrutura de decisão para caso o usuário queira salvar o resultado do sorteio.  
Coloquei a estrutura de decisão dentro de um laço de repetição para se o usuário digitar  
uma opção que não exista, ele volte a perguntar se deseja ou não salvar o resultado.
