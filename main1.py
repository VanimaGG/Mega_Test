import random

chars = "+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

length = int(input("Digite o tamanho da senha: "))

password = ""

for i in range(length):
    password += random.choice(chars)

print("Senha gerada:", password)
