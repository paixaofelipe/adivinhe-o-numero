import random

print("Digite o maior número possível")
num_max = input("Depois você vai ter que adivinhar qual é: ")

if num_max.isdigit():
    num_max = int(num_max)

    if num_max <= 0:
        print("Tente um número acima de zero...")
        quit()
else:
    print("Tente digitar um número...")
    quit()

num_aleatorio = random.randint(0, num_max)
print("Número aleatório decidido!")
#não mostrar número aleatório print(num_aleatorio)

num_tentativa = 0

while True:
    tentativa = input("Adivinhe qual foi o número aleatório gerado: ")
    num_tentativa += 1
    
    if tentativa.isdigit():
        tentativa = int(tentativa)

    else:
        print("Tente digitar um número...")
        continue
    
    if tentativa == num_aleatorio:
        print("É isso aí! Você acertou!")
        break
    else:
        print("Não foi esse número :(")

print("Você conseguiu acertar depois de apenas", num_tentativa, "tentativas!")