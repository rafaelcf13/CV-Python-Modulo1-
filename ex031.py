dist = float(input('Qual a distância dessa viagem? '))
if dist <= 200:
    valor = dist * 0.5
    print('O valor da viagem será de R$ {:.2f} '.format(valor))
else:
    valor = dist * 0.45
    print('O valor da viagem será de R$ {:.2f} '.format(valor))
