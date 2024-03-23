dias = int(input('Quantos dias foi alugado o carro?'))
km = float(input('Quantos quilometros rodados?'))
total = (60*dias) + (0.15*km)
print('O total do valor a ser pago do aluguel do carro é de R$ {:.2f}'.format(total))