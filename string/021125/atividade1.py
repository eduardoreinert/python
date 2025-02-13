

string = input("Digite um texto: ")
inversa = ""

stringlower = string.lower()

pontuacao = [".",",",":",";","!","?"]

# remove os sinais de pontuação
for p in pontuacao:
    stringlower = stringlower.replace(p,"")

for x in stringlower:
    inversa = x + inversa
print(inversa)

if stringlower == inversa:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")