numero = int(input("Digite um número de 1 a 10: "))
if numero > 10 or numero < 1:
  print("Por favor, digite um número entre 1 e 10!")
else:
  for i in range(1, 11):
    print(numero * i)