#!/usr/bin/python3
# ADRIÁN PAYOL MONTERO

import socket
import calculadora

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        http_recibido = str(recvSocket.recv(2048), 'utf-8')
        relativa = http_recibido.split()[1]    # /op1/función/op2
        print(relativa)
        _, op1, funcion, op2 = relativa.split('/')    #guardo cada término

        try:
            op1 = float(op1)
            op2 = float(op2)
            resultado = calculadora.funciones[funcion](op1, op2)
        except KeyError:
            resultado = "FAIL! Funciones aceptadas: sumar, restar, multiplicar, dividir o exp"
        except ValueError:
            resultado = "FAIL! Los operandos han de ser numeros"
        
        # Respuesta:
        print('Answering back...\n')
        html_respuesta = "<html><body><h2>Calculadora &uarr; </h2>"
        html_respuesta += "<p><h4>El resultado es: "
        html_respuesta += str(resultado)
        html_respuesta += "</h4></p></body></html>"

        recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" + html_respuesta + "\r\n", 'utf-8'))
        recvSocket.close()

except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
