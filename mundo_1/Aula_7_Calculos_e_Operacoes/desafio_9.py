# Faça um programa que leia um número inteiro qualquer
# e mostre na tela a sua tabuada

n = int(input("Digite um número: \n"))
print("Tabuada do {}:".format(n))

print("{} x {} = {}".format(n, 1, (n * 1)))

# Sem loop o código é repetitivo
# Para tabuada completa do 1 ao 10
n = int(input('Digite um numero: '))
print(f'Tabuada do {n}:')

for i in range(1, 11):
     print(f'{n} x {i} = {n * i}')
