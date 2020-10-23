vel=int(input('Qual a velocidade do carro? '))
if vel <= 80:
    print('Parabéns, você é um bom motorista!')
else:
    multa = (vel - 80) * 7
    print('MULTADO! Você excedeu o limite de velocidade de 80km/h')
    print('E terá que pagar uma multa de R$ {:.2f},00!'.format(multa))

print('Tenha um bom dia! Dirija com segurança!')