a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
menor = a
if b<a and b<c:
    menor = b
if c < a and c < b:
    menor = c

print('O menor valor é o {}' .format(menor))

