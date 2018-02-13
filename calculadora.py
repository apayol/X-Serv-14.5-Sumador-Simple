#!/usr/bin/python3
# ADRIÁN PAYOL MONTERO

import sys

def suma(op1, op2):
    return op1 + op2

def resta(op1, op2):
    return op1 - op2

def multiplicacion(op1, op2):
    return op1 * op2

def division(op1, op2):
    try:
        return op1 / op2
    except ZeroDivisionError:
        return("Indefinido, división entre 0!")

def exponencial(op1, op2):
    return op1**op2

funciones = {
    "sumar": suma,
    "restar": resta,
    "multiplicar": multiplicacion,
    "dividir": division,
    "exp": exponencial
}

if __name__ == "__main__":    #para importarlo a otro programa

    if len(sys.argv) != 4:    # han de ser 4 argumentos
        sys.exit("uso: python3 calculadora.py función operando1 operando2")
    
    _, funcion, op1, op2 = sys.argv    # guardo los argumentos

    try:
        op1 = float(op1)
        op2 = float(op2)
        resultado = funciones[funcion](op1, op2)
    except ValueError:
        sys.exit("Los operandos han de ser números")
    except KeyError:
        sys.exit("Funciones aceptadas: sumar, restar, multiplicar, dividir o exp")

    print("La operación resulta: " + str(resultado))


