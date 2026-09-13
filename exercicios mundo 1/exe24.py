num = float(input("Digite um número: "))
print(f"Analisando o número {num}...")
print(f"Unidade: {int(num) % 10}")
print(f"Dezena: {int(num) // 10 % 10}")
print(f"Centena: {int(num) // 100 % 10}")
print(f"Milhar: {int(num) // 1000 % 10}")

