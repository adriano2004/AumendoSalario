s = float(input('Qual o seu salário atual? '))
a = 15.0 # 15% de aumento
valor = s + (s*a) / 100

print('Seu salário aumentou de {} para {}'.format(s,valor))