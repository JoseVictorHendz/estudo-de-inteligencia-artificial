
entrada1 = (int(input('Digite a primeira entrada ')))
entrada2 = (int(input('Digite a segunda entrada ')))

peso1 = -1
peso2 = 1

saida = 0

tipoCalculo = (int(input('Digite qual calculo: 1-fr 2-lr 3-fs ')))

soma = (entrada1*peso1) + (entrada2*peso2)

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
