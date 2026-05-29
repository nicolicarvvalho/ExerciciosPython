lista = [5, 7, 2, 9, 4, 1, 3]
print("O tamanho da lista é ", len(lista))
print("O maior valor da lista é ", max(lista))
print("O menor valor da lista é ", min(lista))
print("A soma dos elementos da lista é igual a ", sum(lista))
lista.sort()
print("A ordem crescente é ", lista)
lista.sort(reverse=True)
print("A ordem decrescente é :", lista)