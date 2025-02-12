n = int(input("Uma quantidade de números para ser analisado: "))
print("Informe o número: ")
anterior = int(input())

i = 1 # leu um numero
ordenado = 0 # ordenado é a variavel contadora

while (i < n) and (ordenado == 0):
    print("Informe o número: ")
    atual = int(input())
    i = i + 1 # leu mais um número
    if (atual <= anterior):
        ordenado = ordenado + 1
    anterior = atual

if (ordenado == 0):
    print("Sequência está ordenada.")
else:
    print("Sequência não está ordenada.")