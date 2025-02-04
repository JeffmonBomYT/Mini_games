tipo = (int(input('Escolha o tipo de cálculo: \n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n/-----------------/\n')))

x = int(input('1º valor: '))
y = int(input('2ª valor: '))
somas = x + y
subs = x - y
multis = x * y
divis = x / y

while True:
  def soma():
    if tipo == 1:
      print(f"/-----------------/\n {x} + {y} =", somas)
  soma()

  def sub():
    if tipo == 2:
      print(f"/-----------------/\n {x} - {y} =", subs)
  sub()

  def multi():
    if tipo == 3:
      print(f"/-----------------/\n {x} * {y} =", multis)
  multi()

  def divi(): 
    if tipo == 4:
      print(f"/-----------------/\n {x} / {y} =", divis)
  divi()

  if tipo == 0:
    break






