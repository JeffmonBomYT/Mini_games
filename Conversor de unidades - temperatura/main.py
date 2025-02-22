#Conversor de Unidades + temp.
c = 0
k = 0
f = 0

def converter(x, y):
  if x == 1:
    return y - 273
  elif x == 2:
    return (y - 273) * 1.8 + 32
  elif x == 3:
    return y + 273
  elif x == 4:
    return y * 1.8 + 32 
  elif x == 5:
    return (y - 32) / 1.8  
  elif x == 6:
    return (y - 32) * 5/9 + 273
  elif x == 0:
    print('Até mais')

while True:


  print("/-------------------------------------/")
  print("[ Conversor de unidades - temperatura ]")
  print("/-------------------------------------/")
  print("      |        De → Par       |    ")
  print("      |-----------------------|    ")
  print("      | Kelvin → Celsius      | - 1")
  print("      | Kelvin → Fahrenheit   | - 2")
  print("      | Celsius → Kelvin      | - 3")
  print("      | Celsius → Fahrenheit  | - 4")
  print("      | Fahrenheit → Celsius  | - 5")
  print("      | Fahrenheit → Kelvin   | - 6")
  print("      | Sair                  | - 0")
  print("      |_______________________|    ")
  x = int(input('  > '))
  y = float(input('valor: '))

  resultado = converter(x, y)

  if resultado is not None:
    print(f'Resultado: {resultado}')










""" 
Conversão de Escalas Termométricas

| De → Para             | Fórmula                   |
|-----------------------|---------------------------|
| Kelvin → Celsius      | C = K - 273               |
| Kelvin → Fahrenheit   | (K - 273) × 1,8 + 32      |
| Celsius → Kelvin      | K = C + 273               |
| Celsius → Fahrenheit  | F = C × 1,8 + 32          |
| Fahrenheit → Celsius  | C = (F - 32) / 1,8        |
| Fahrenheit → Kelvin   | K = (F - 32) × 5/9 + 273  | 
"""

# test 1:
"""   c = 0
  k = 0
  f = 0

  c = k - 273 # kelvin -> celcius
  f = (k - 273) * 1,8 + 32 #kelvin -> fahrenheit
  k = c + 273 # celcius -> kelvin
  f =  """