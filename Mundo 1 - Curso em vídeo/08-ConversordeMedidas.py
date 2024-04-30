m = float(input('Digite uma distância em metros: '))

print('A medida de {}m corresponde a:\n{}Km\n{}Hm\n{}Dam\n{}Dm\n{}Cm\n{}mm'.format(
    m, m/1000, m/100, m/10, m*10, m*100, m*1000))
