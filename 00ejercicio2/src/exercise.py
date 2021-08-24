
#calcular el area de un rectangulo 
def areaRect(largo, ancho): 
    area = largo * ancho 
    return area

#calcula el perimetro de un rectangulo 
def perimetroRect(largo, ancho): 
    perimeto = 2 * (largo + ancho) 
    return pertimetro 

def main():
   largo = float(input('Dame el largo: '))
   ancho = float(input('Dame el ancho: '))

   respuesta = input('¿Qué desea calcular (a)Area (p)Perimetro?')

    if respuesta == 'a' or respuesta == 'A':
        print('El área del rectangulo es: '+str(areaRect(largo,ancho)))
    elif respuesta == 'p' or respuesta == 'P': 
        print('El perimetro del rectangulo es: '+str(perimetroRect(largo,ancho)))
    else:
        print('Respuesta incorrecta')




if __name__=='__main__':
    main()
