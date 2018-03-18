def calculoDeRampa(soma):
    if (soma < 0):
        saida = 0
        print('o valor de saida é ', saida)
    elif (soma >= 0 & soma <= 1):
        saida = soma
        print('o valor de saida é ', saida)
    elif (soma > 1):
        saida = 1
        print('o valor de saida é ', saida)
    return int(saida)

def cauculoDePeso(w1, w2, x11, x12):
    soma = 0
    soma = x11 * w1 + x12 * w2
    return soma

def recauculandoPeso(w, y1,x11, saida):
    w1 = (w + 1 * (y1 - saida) * x11)
    return w1

x11 = 0 #int(input("adicione x11 "))
x12 = 0 #int(input("adicione x12 "))
x21 = 1 #int(input("adicione x21 "))
x22 = 1 #int(input("adicione x22 "))

w1 = -1 #int(input("adicione w1 "))
w2 = -1 #int(input("adicione w2 "))

y1 = 0
y2 = 1

correto1 = 0
correto2 = 0
saida1 = 0
saida2 = 0

soma1 = 0
soma2 = 0



while correto1 == 0 or correto2 == 0:
    correto1 = 0
    correto2 = 0
    soma1 = cauculoDePeso(w1, w2, x11, x12)
    print(("--------------------------------", soma1))
    soma2 = cauculoDePeso(w1, w2, x21, x22)
    print(("--------------------------------", soma2))

    if correto1 == 0:
        saida1 = calculoDeRampa(soma1)

    if(correto2 == 0):
        saida2 = calculoDeRampa(soma2)


    if saida1 == y1 and correto1 !=1:
        print("---------saida1 é ", saida1)
        correto1 = 1
    elif correto1 !=1:
        w1 = recauculandoPeso(w1, y1, x11, saida1)
        w2 = recauculandoPeso(w1, y1, x12, saida1)
        print("correção1 do w1 w2 saida1", w1, w2)

    if saida2 == y2:
        print("---------saida2 é ", saida2)
        correto2 = 1
    else:
        w1 = recauculandoPeso(w1, y2, x21, saida2)
        w2 = recauculandoPeso(w2, y2, x22, saida2)
        print("correção2 do w1 e w2 saida2", w1, w2)

print('fim')