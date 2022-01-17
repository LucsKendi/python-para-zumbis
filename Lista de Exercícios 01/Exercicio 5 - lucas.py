merc = float(input('Qual valor da mercadoria?'))
desc = float(input('Qual porcentagem do desconto?'))

descontado = merc * desc / 100
final = merc - descontado
print('O preço da mercadoria com o desconto é', final)
