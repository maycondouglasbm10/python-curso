from random import randint
from time import sleep
computador = randint(0, 5)
print("=-=" * 25)
print("Irei pensar em um número, entre 0 e 5. Tente adivinhar...")
print("=-=" * 25)
print("PROCESSANDO...")
sleep(3)
print("PROCESSANDO...")
sleep(3)
print("Pronto! Já pensei em um número entre 1 e 5. Tente adivinhar!")
numero = int(input("O número que eu pensei foi...?"))
if numero == computador:
    print("Parabéns! Você acertou!")
else:
    print(f"Você errou! Eu pensei no número {computador}.")
    print("Tente novamente!")