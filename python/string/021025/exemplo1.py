a = "eu blebleble\n"
print(a)

b = "20 de Abril tem prova\n"
print(b[0])

c = "\nFizeram os exercícios?\n"
print(c)

d = a + b
print(d)

print(3 * a)

string = input("Digite um texto: ")
inversa = " "

for x in string:
    inversa = x + inversa
print(inversa)

print(b[6:11])
print(b[6:11:2])
print(b[::-1])

print(c)

print(c.strip(), "oi")

resultado = "exercicios" in "Fizeram os exercicios?"
print(resultado)
True

print(c.find("Fizeram"))
print(c.find("eu"))

numeros = "1; 2 ; 3"
h= numeros.split(";")
print(h)

i = c.replace("exercícios","estudos dirigidos")
print(i)

listanumeros = list(numeros)
print(listanumeros)

l = list("Atividade")
print("-".join(l))

str = "Atividade"
str1 = str.upper()
str2 = str.lower()
print(str)
print(str1)
print(str2)