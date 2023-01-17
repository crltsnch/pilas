#Este ejercicio verifica si los paréntesis en una expresión dada están balanceados. 
# Utiliza una pila para almacenar los paréntesis que se abren y luego verifica si los paréntesis que se cierran corresponden a los que se abrieron.
# Si todos los paréntesis están balanceados, la función devuelve True, de lo contrario, devuelve False.

def balance_parenthesis(expr):
    stack = []
    for char in expr:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                return False
            if char == ")" and stack[-1] != "(":
                return False
            if char == "]" and stack[-1] != "[":
                return False
            if char == "}" and stack[-1] != "{":
                return False
            stack.pop()
    if not stack:
        return True
    return False

print(balance_parenthesis("({[]})")) # True
print(balance_parenthesis("({[})")) # False