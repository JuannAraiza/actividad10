
def opAritmetica(a, b, clave): 
    if clave == 's':
        return a + b
    elif clave == 'r':
        return a - b 
    elif clave == 'm':
        return a * b
    elif clave == 'd':
        return a / b 

    else:
        return 'clave invalida'

def main():
    n1 = int(input('Dame el valor del primer número: '))
    n2 = int(input('Dame el valor del segundo número: '))
    clave = input('Dame la clave (s=suma/r=resta/m=multiplicacion/d=divisio): ')

    resultado = opAritmetica(n1, n2, clave)

    print(resultado) 
   




if __name__=='__main__':
    main()
