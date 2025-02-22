from random import randint


def roll(lados, quant):
    results = []
    for x in range(quant):
        results.append(randint(1, lados))
    return results

while True:
    print("/------------/")
    print("Escolha")
    x = int(input("1 - d6\nsua escolha: "))
    y = int(input("Quantidade: "))
    print("/------------/")



    if x == 1:
        lados = 6
    elif x != 1:
        print('Escolha inválida, tente outra vez ou saia')
    else:
        print('Adeus')
        break
    results = roll(lados, y)
    print(f'Reusltado: {results}')



    
 

        
       

