ish= int(input('Введите исходное число: '))
ss = int(input('Введите целевую систему счисления 2/8: '))
chislo = ''
while ish > 0:
    chislo = chislo + str(ish%ss)
    ish = ish //ss
print( chislo ) 
