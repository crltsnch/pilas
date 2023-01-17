#Este ejercicio convierte un número decimal en su representación binaria. 
# Utiliza una pila para almacenar los residuos de la división por 2 y luego construye el número binario pop de la pila. Al final, devuelve el número binario generado.

def convert_to_binary(decimal):
    stack = []
    while decimal > 0:
        remainder = decimal % 2
        stack.append(remainder)
        decimal = decimal // 2
    binary = ""
    while stack:
        binary += str(stack.pop())
    return binary

print(convert_to_binary(10)) # 1010
print(convert_to_binary(23)) # 10111
