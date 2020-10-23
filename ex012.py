p = float(input('Qual preço do produto: R$ '))
d = float(input('Qual valor do desconto: % '))
d = p*d/100
p = p-d
print('O desconto é de {:.2f} reais e valor do produto com desconto é de R$ {:.2f}'.format(d, p))