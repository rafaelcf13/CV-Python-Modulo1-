aluguel = int(input("Por quantos dias o carro foi alugado? "))
km = float(input('Quantos Quilometros você percorreu com o carro? '))
valor = (aluguel * 60) + (km * 0.15)
print('O valor a pagar é de R$ {}.'.format(valor))