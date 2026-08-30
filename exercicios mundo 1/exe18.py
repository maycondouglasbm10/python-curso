import math 
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = math.hypot(co, ca)
print(f"O comprimento da hipotenusa é: {hi:.2f}")