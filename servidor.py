# SERVIDOR

import socket
import threading

#import time
#Obs.: temp é o valor que passará por conversão
def astronomia_conversor(unid_converter, unid_convertido, temp):
    print(unid_converter, unid_convertido, temp)
    print(type(unid_converter), type(unid_convertido), type(temp))
    if (unid_converter == 2 and unid_convertido == 1):
        valor_convertido = temp*(2.063*(10**5))
    if (unid_converter == 1 and unid_convertido == 2):
        valor_convertido = temp * (4.848*(10**-6))
    if (unid_converter == 1 and unid_convertido == 3):
        valor_convertido = temp*(1.58*(10**-5))
    if (unid_converter == 3 and unid_convertido == 1):
        valor_convertido = temp*6.324*(10**4)
    if (unid_converter == 2 and unid_convertido == 3):
        valor_convertido = temp*3.262
    if (unid_converter == 3 and unid_convertido == 2):
        valor_convertido = temp*0.3066
    return valor_convertido

def astronomia_conversor_km(unid_converter, unid_convertido, temp):
    print(unid_converter, unid_convertido, temp)
    print(type(unid_converter), type(unid_convertido), type(temp))
    if (unid_converter == 2 and unid_convertido == 1):
        valor_convertido = temp*(2.063*(10**5))*(1.496*(10**8))
    if (unid_converter == 1 and unid_convertido == 2):
        valor_convertido = temp * (4.848*(10**-6))*(3.086*(10**13))
    if (unid_converter == 1 and unid_convertido == 3):
        valor_convertido = temp*(1.58*(10**-6))*(9.461*(10**12))
    if (unid_converter == 3 and unid_convertido == 1):
        valor_convertido = temp*(6.324*(10**4))*(1.496*(10**8))
    if (unid_converter == 2 and unid_convertido == 3):
        valor_convertido = temp*3.262*(9.461*(10**12))
    if (unid_converter == 3 and unid_convertido == 2):
        valor_convertido = temp*0.3066*(3.086*(10**13))
    return valor_convertido

def temperatura_conversor(unid_converter, unid_convertido, temp):
    print(unid_converter, unid_convertido, temp)
    print(type(unid_converter), type(unid_convertido), type(temp))
    if (unid_converter == 2 and unid_convertido == 1):
        temperatura_convertida = (temp - 32) * 5/9
    if (unid_converter == 1 and unid_convertido == 2):
        temperatura_convertida = (temp * 9/5) + 32
    if (unid_converter == 1 and unid_convertido == 3):
        temperatura_convertida = temp + 273
    if (unid_converter == 3 and unid_convertido == 1):
        temperatura_convertida = temp - 273
    if (unid_converter == 2 and unid_convertido == 3):
        temperatura_convertida = (5/9)*(temp - 32) + 273
    if (unid_converter == 3 and unid_convertido == 2):
        temperatura_convertida = ((9/5)*(temp - 273) + 32)
    return temperatura_convertida


# Cria um 'objeto socket'
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Obtém o nome da máquina local

# host = socket.gethostname()
host = 'localhost'
port = 9999

# Liga à porta
serversocket.bind((host, port))

# Começa a 'escutar' o requerimento
serversocket.listen(5)

def handle_client(client_socket):
    #Recebendo a opção que o usuário digitou
    opcao = client_socket.recv(1024)
    print('[*] Recebido: %s' %opcao.decode('ascii'))
    
    #Recebendo valores
    un_converter = client_socket.recv(1024)
    print('[*] Recebido: %s' %un_converter.decode('ascii'))
    un_converter = int(un_converter.decode('ascii'))
    print('\n----------------------------------------------\n')
    un_convertida = client_socket.recv(1024)
    print('[*] Recebido: %s' %un_convertida.decode('ascii'))
    un_convertida = int(un_convertida.decode('ascii'))
    print('\n----------------------------------------------\n')
    valor_conversao = client_socket.recv(1024)
    print('[*] Recebido: %s' %valor_conversao.decode('ascii'))
    valor_conversao = float(valor_conversao.decode('ascii'))
    print('\n----------------------------------------------\n')
    
    #Transformando valores
    if int(opcao.decode('ascii')) == 1:
        t = str(temperatura_conversor(un_converter, un_convertida, valor_conversao))
        print(t)
        clientsocket.send(t.encode('ascii'))
    if int(opcao.decode('ascii')) == 2:
        t = str(astronomia_conversor(un_converter, un_convertida, valor_conversao))
        t_km = str(astronomia_conversor_km(un_converter, un_convertida, valor_conversao))
        clientsocket.send(t_km.encode('ascii'))
        print(t_km)
        print(t)
        clientsocket.send(t.encode('ascii'))
 
    #temperatura_transformada = str(temperatura_conversor())
    #clientsocket.send(temperatura_transformada.encode('ascii'))
    #temp_convertida = temperatura_conversor(request)
 
    clientsocket.close()    

while True:
    # Estabelece uma conexão
    clientsocket, addr = serversocket.accept()
    print('Temos uma conexão com %s' % str(addr))
    client_handler = threading.Thread(target = handle_client, args=(clientsocket,))
    client_handler.start()
   # currentTime = time.ctime(time.time()) + "\r\n"
