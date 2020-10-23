sal = float(input('Qual é o salário? R$ '))
aum = float(input('De quantos % foi o aumento: '))
nsal = (sal * aum / 100) + sal
print('O seu salário era R$ {} e com {}% de aumento, foi para R$ {:.2f}'.format(sal, aum, nsal))