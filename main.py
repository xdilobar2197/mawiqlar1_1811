mawiqlar1_1811

# 1 - masala
def salomlaw():
    soat = int(input('Soatni kiriting: '))

    if 6 <= soat < 12:
        print('xayrli tong')
    elif 12 <= soat < 18:
        print('xayrli kun')
    else:
        print('xayrli kech')


# 2- masala
def hisob():
    sonlar = [10, 20, 30]
    yigindi = sum(sonlar)

    kopaytma = 1
    for i in sonlar:
        kopaytma *= i

    print(f'Yigindi: {yigindi}, Kopaytma: {kopaytma}')

hisob()

#3 - masala
def teskari_son():
    for i in range(10, 1, -1):
        print(i)

teskari_son()



#4 - masala
def persnl_salom(ism, til):
    if til == 'uz':
        print(f'Salom, {ism}')
    elif til == 'en':
        print(f'Hello, {ism}')
    elif til == 'ru':
        print(f'privet, {ism}')
    else:
        print('unday til qolat quvatlanmauydi')

print(persnl_salom('ali', 'privet'))


def kvadra_ryht(roy):
    for son in roy:
        print(f'{son} ning kvadrati = {son ** 2}')
