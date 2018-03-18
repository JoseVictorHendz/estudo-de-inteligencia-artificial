def calculoDeSaida(soma):
    saida = 0
    if (tipoCalculo == 1):
        if (soma < 0):
            saida = 0

        elif (soma >= 0 & soma <= 1):
            saida = soma
        elif (soma > 1):
            saida = 1


    elif (tipoCalculo == 2):
        if (soma <= 0):
            saida = -1
        elif (soma > 0):
            saida = 1

    elif (tipoCalculo == 3):
        if (soma >= 0):
            saida = 1 - 1 / (1 + soma)
        elif (soma < 0):
            saida = -1 + 1 / (1 - soma)
    return saida

peso1 = -2
peso2 = 2

peso3 = 2
peso4 = -1

peso5 = 1
peso6 = 1

saida = 0

continua =1

while continua == 1:

    entrada1 = int(input("Digite a primeira entra: "))
    entrada2 = int(input("Digite a segunda entrada: "))

    tipoCalculo = int(input('Digite qual calculo: 1-fr 2-lr 3-fs '))

    soma1 = (entrada1 * peso1) + (entrada2 * peso2)

    saida1 = calculoDeSaida(soma1)

    soma2 = (entrada1 * peso3) + (entrada2 * peso4)

    saida2 = calculoDeSaida(soma2)

    soma3 = (saida1 * peso5) + (saida2 * peso6)

    print(calculoDeSaida(soma3))
    continua = int(input("Continuar? 0 para sair 1 - para continuar"))
