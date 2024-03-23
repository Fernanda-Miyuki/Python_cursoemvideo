real =float(input('Quantos reais você tem em sua carteira?: R$'))
dolar = real/4.99
euro = real/5.42
iene = real/0.033
peso = real/0.0059
print('Com R${} você pode comprar: \n US${:.2f} \n €{:.2f} \n ¥{:.2f} \n ${:.2f}'.format(real,dolar,euro,iene,peso))
