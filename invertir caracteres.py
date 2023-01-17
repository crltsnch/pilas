#Este ejercicio invierte el orden de los caracteres en una cadena dada. 
#Utiliza una pila para almacenar los caracteres de la cadena y luego los pop de la pila para construir la cadena invertida. Al final, devuelve la cadena invertida.

def reverse_string(string):
    stack = list(string)
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    return reversed_string

print(reverse_string("hello")) # olleh
print(reverse_string("world")) # dlrow