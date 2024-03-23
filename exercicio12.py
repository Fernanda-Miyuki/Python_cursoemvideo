preco = float(input('Qual é o valor do produto? R$'))
des = preco - (preco*0.05) 
print('O valor do produto é de R$ {:.2f} e com desconto de 5% é R$ {:.2f}! APROVEITE A PROMOÇÃO! :)'.format(preco,des))