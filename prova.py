import random
numeroALeatorio = random.randint(1, 10)
tentativas = 0

while tentativas < 3:
    tentativa = int(input("Advinhe um número entre 1 e 10: "))

    if tentativa == numeroALeatorio:
        print("Parabéns! Você acertou!")
        break
    else: 
        print("Tente novamente!")
    tentativas += 1

else:
    print("Suas tentativas acabaram. O número era:", numeroALeatorio)


    