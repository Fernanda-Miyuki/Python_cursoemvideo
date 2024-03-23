alt = float(input('Digite a medida da altura da parede:'))
lar = float(input('Digite a medida da largura da parede:'))
area = alt*lar
tinta = area/2
print('A área de sua parede é de {:.2f} metros quadrados. \n Para pintar esta parede será necessário {:.2f} litros de tinta!'.format(area,tinta))