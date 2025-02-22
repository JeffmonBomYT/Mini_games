#REVER SISTEMA DE SOMA DE DADOS
from random import randint

def roll(lados, quant):
    results = []
    for x in range(quant):
        results.append(randint(1, lados))
    return results

while True:
  print('/-----------------------/')
  print("O que deseja rolar?")
  print('1 - D4 \n2 - D6 \n3 - D8 \n4 - D10 \n5 - D12 \n6 - D20 \n7 - Sair')
  print('/-----------------------/')

  x = int(input('escolha um dado: '))
  y = int(input('Quantidade de dados: '))
  
  if x == 1:
    lados = 4
  elif x == 2:
   lados = 6
  elif x == 3:
    lados = 8
  elif x == 4:
    lados = 10
  elif x == 5:
   lados = 12
  elif x == 6:
    lados = 20
  elif x == 7:
    print('Adeus!')
    break
    
  results = roll(lados, y)
  print(f"Resultado: {results} [{sum(results)}]")

  