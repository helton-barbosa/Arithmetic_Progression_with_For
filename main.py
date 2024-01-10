termo_ini = int(input('Termo inicial: '))
dif_comum = int(input('Diferença em comum: '))
termos = int(input('Quantidade de termos: '))

for pa in range(termo_ini, termo_ini + termos * dif_comum, dif_comum):
    print(f'{pa}')
