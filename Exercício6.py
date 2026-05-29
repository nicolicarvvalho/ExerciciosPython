numero = int(input("Digite um número: "))
nPrimo = True
for i in range (2, numero):
  if numero % i == 0:
   print("Esse número não é primo!")
   break
else:
    print("Esse número é primo!")