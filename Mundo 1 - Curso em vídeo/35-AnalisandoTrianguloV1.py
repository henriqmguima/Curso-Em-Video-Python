print('-='*20)
print('Analisador de Triângulos')
print('-='*20)

s1 = float(input('1º Segmento: '))
s2 = float(input('2º Segmento: '))
s3 = float(input('3º Segmento: '))
if s1 < s2+s3 and s2 < s1+s3 and s3 < s1+s2:
    resp = 'PODEM'
else:
    resp = 'NÃO PODEM'
print('Os segmentos acima {} FORMAR triângulo!'.format(resp))
