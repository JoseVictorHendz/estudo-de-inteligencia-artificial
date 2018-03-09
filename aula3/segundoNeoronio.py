numEntradas = int(input('Digite quantas entradas e pesos o neuronio tera: '))
entradas = [numEntradas]
pesos = [numEntradas]
soma = 0

for numEntradas in range(0, numEntradas):
    entradas.append(int(input('Digite o valor para a {} entrada: '.format(numEntradas + 1))))
    pesos.append(int(input('Digite o valor para o {} peso: '.format(numEntradas + 1))))
    soma += entradas[numEntradas + 1] * pesos[numEntradas + 1]
    print(soma)

tipoCalculo = (int(input('Digite qual calculo: 1-fr 2-lr 3-fs ')))

if (tipoCalculo == 1):
    if(soma< 0):
        saida = 0
        print('o valor de saida é ', saida)
    elif(soma >= 0 & soma <=1):
        saida = soma
        print('o valor de saida é ', saida)
    elif(soma > 1):
        saida = 1
        print('o valor de saida é ', saida)


elif (tipoCalculo == 2):
    if(soma <= 0):
        saida = -1
        print('o valor de saida é ', saida)
    elif(soma > 0):
        saida = 1
        print('o valor de saida é ', saida)

elif (tipoCalculo == 3):
    if(soma >= 0):
        saida = 1 -1/(1 + soma)
        print('o valor de saida é ', saida)
    elif(soma < 0):
        saida = -1 + 1/(1-soma)
        print('o valor de saida é ', saida)