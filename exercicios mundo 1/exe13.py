produto = float(input("Digite o preço do produto: "))
desconto = produto * 0.12
preco_final = produto - desconto
print(f"O preço final do produto com desconto é: R${preco_final:.2f}")