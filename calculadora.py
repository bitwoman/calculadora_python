def somar(v1, v2):
    return v1 + v2

def subtrair(v1, v2):
    return v1 - v2

def multiplicar(v1, v2):
    return v1 * v2

def dividir(v1, v2):
    return v1 / v2
        

def calculadora():
    print('*' * 10, 'Calculadora Python', '*' * 10)
    print('Selecione o número da operação desejada: \n')
    print('1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão')
    
    operacao = int(input('Digite sua opção(1-2-3-4): '))
    
    if operacao == 1:
        numero1 = int(input('Digite primeiro número: '))
        numero2 = int(input('Digite primeiro número: '))
        
        soma = somar(numero1, numero2)
        
        print('\n%d + %d = %d' %(numero1, numero2, soma))
    elif operacao == 2:
        numero1 = int(input('Digite primeiro número: '))
        numero2 = int(input('Digite primeiro número: '))
        
        subtracao = subtrair(numero1, numero2)
        
        print('\n%d - %d = %d' %(numero1, numero2, subtracao))
    elif operacao == 3:
        numero1 = int(input('Digite primeiro número: '))
        numero2 = int(input('Digite primeiro número: '))
        
        multiplicacao = multiplicar(numero1, numero2)
        
        print('\n%d * %d = %d' %(numero1, numero2, multiplicacao))
    elif operacao == 4:
        numero1 = int(input('Digite primeiro número: '))
        numero2 = int(input('Digite primeiro número: '))
        
        divisao = dividir(numero1, numero2)
        
        print('\n%d / %d = %d' %(numero1, numero2, divisao))
    else:
        print('Operação inválida!')

calculadora()
