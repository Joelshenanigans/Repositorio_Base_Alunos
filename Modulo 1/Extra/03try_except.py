# crie uma função chamada calculadora que receba tres parametros
# dois numeros e uma operação( +, -, *, /)
# a função deve retornar o resultado da operação, mas precisa tratar as exceções:
# divisão por zero (ZeroDivisionError)
# tipo de dado invalido (valueError)

def calculadora():
    try:
        n = input('digite um numero (ou x para sair do sistema: ')     
        if n.lower() == 'x':
            print('ate breve')
            return
        n1=input('digite um numero ou x para sair do sistema: ')
        if n1.lower() == 'x':
            print('ate breve')
        operador = input('informe um operador matematico (+, -, *, /) ou x para sair do sistema: ')
        if operador.lower() == 'x':
            print('ate breve')
            return
        # converter as entradas (inputs) em float
        n = float(n)
        n1 = float(n1)

        if operador == '+':
            resultado = n + n1
        elif operador == '-':
            resultado = n - n1
        elif operador == '*':
            resultado = n * n1
        elif operador == '/':
            resultado = n / n1
            if n1 == 0:
                raise ZeroDivisionError('não é possivel dividir por zero')
            resultado = n / n1
        else:
            print('você não escolheu um operador ou escolheu um comando valido')
            return
        print(f"operação: {n}{operador}{n1} = {resultado}")
    except ValueError:
        print('voce digitou um caracter invalido, digite somente numeros')
    except ZeroDivisionError as zero:
        print(zero)
calculadora()



