while True:
    nome = input("Digite seu nome: ")
    if len(nome) < 3:
      print("Por favor, digite um nome com mais de 3 caracteres!")
      continue
    else:
      print("Nome válido")
      break
      print("\n")

while True:
    idade = int(input("Digite sua idade: "))
    if idade <= 150:
      print("Idade Válida")
      break
    else:
      print("Idade inválida, tente outra vez!")
      continue

while True:
      salario = float(input("Digite seu salário: "))
      if salario < 0:
        print("Salário Inválido")
      else:
        print("Salário Válido!")
        break

while True:
    sexo = str(input("Digite seu sexo com apenas 1 caractere [M/F]: ")).upper().strip()
    if sexo not in ['M','F']:
      print("Sexo Inválido, tente novamente!")
    else:
      print("Sexo Válido!")
      break

while True:
    estadoCivil = input("Digite seu estado civil com apenas 1 caractere [S, C, V, D]: ").upper().strip()
    if estadoCivil not in ['S', 'C', 'V', 'D']:
      print("Estado civil inválido, digite apenas o caractere especificado.")
    else:
      print("Estado civil válido!")
      print(f"Dados cadastrados com sucesso, obrigado2 {nome}!")
      break