#Básicamente el concepto de pilas es que el Último elemento ingresado es el primero en salir.

pila = []

def main():
    print('1 Apilar elemento (entero)')
    print('2 Desapilar elemento')
    print('3 Mostrar pila')
    print('4 Salir')
    option = input('Elija una opción: ')

    #Esta opcion permite apilar el numero en la lista
    if str(option) == '1':
        elemento = input('Introduzca el número a apilar: ')
        pila.append(elemento)
        print('Elemento apilado correctamente')
        main()
    
    #Esta opcion saca desapila a partir del ultimo numero ingresado
    elif str(option) == '2':
        if len(pila) == 0:
            print('No hay elementos para despilar')
            main()
        else:
            print('El número: ', pila.pop(), 'fue desapilado')
            main()    
    
    #Esta opción muestra la pila
    elif str(option) == '3':
        for i in reversed(range(len(pila))):
            print('Pila: ', pila[i])
        main()
    
    #Esta opción permite salir de la ejecucion del código
    elif str(option) == '4':
        exit()
    else:
        print('\nOpción no válida\n')
        main()

main()