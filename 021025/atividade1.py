def adjacente_iguais(numero):
    numero_str = str(numero)
    for i in range(len(numero_str) - 1):
        if numero_str[i] == numero_str[i + 1]:
            return True
    return False

numero = int(input("Digite um número inteiro: "))

if adjacente_iguais(numero):
    print("Sim")
else:
    print("Não")