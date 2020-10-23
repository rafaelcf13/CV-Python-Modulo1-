sal = float(input('Digite o Salario do funcionario: '))
if sal <= 1250:
    print('Seu salario era R$ {:.2f} e agora é R$ {:.2f}'.format(sal, sal * 1.15))
else:
    print('Seu salario era R$ {:.2f} e agora é R$ {:.2f}'.format(sal, sal * 1.10))


