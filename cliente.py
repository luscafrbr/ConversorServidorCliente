# CLIENTE

import socket


#Unidades de temperatura
def unidade_converter():
    print('CONVERSOR DE TEMPERATURA\n')
    print('-------------------------------------\n')
    print('1 Celsius\n2 Fahrenheit\n3 Kelvin\n')
    print('-------------------------------------\n')
    unid_converter = int(input('Pressione 1, 2 ou 3 para selecionar a unidade da qual você deseja converter e dê enter.\nExemplo: tenho um valor em Celsius e quero em Kelvin. Então você digita 1, referente à unidade Celsius, neste caso.\n'))
    return unid_converter
def unidade_converter_eng():
    print('TEMPERATURE CONVERTER\n')
    print('-------------------------------------\n')
    print('1 Celsius\n2 Fahrenheit\n3 Kelvin\n')
    print('-------------------------------------\n')
    unid_converter = int(input('Press 1, 2 ou 3 to select which unit you want to convert from and enter.\nExample: I have a value in Celsius and I want it in Kelvin. Then you type 1, referring to the Celsius unit, in this case.\n'))
    return unid_converter
def unidade_convertida():
    unid_convertido = int(input('Pressione 1, 2 ou 3 para selecionar a unidade para qual da qual você deseja converter e dê enter.\nExemplo: tenho um valor em Celsius e quero em Kelvin. Então você digita 3, referente à unidade Kelvin, neste caso.\n'))
    return unid_convertido
def unidade_convertida_eng():
    unid_convertido = int(input('Press 1, 2 or 3 to select the unit to which you want to convert and hit enter.\nExample: I have a value in Celsius and I want it in Kelvin. Then you type 3, for the Kelvin unit, in this case.\n'))
    return unid_convertido
def temperatura_conv():
    temp = float(input('Digite o valor de temperatura para ser convertido e pressione enter\n'))  
    return temp
def temperatura_conv_eng():
    temp = float(input('Enter the temperature value to be converted and press enter\n'))  
    return temp

#Unidades da astronomia
def unit_astroconverter():
    print('CONVERSOR DE UNIDADES DA ASTRONOMIA\n')
    print('-------------------------------------\n')
    print('1 Unidade Astronômica\n2 Parsec\n3 Ano-luz\n')
    print('-------------------------------------\n')
    unid_astroconverter = int(input('Pressione 1, 2 ou 3 para selecionar a unidade da qual você deseja converter e dê enter.\nExemplo: tenho um valor em Unidades Astronômicas e quero em Anos-Luz. Então você digita 1, referente à Unidade Astronômica, neste caso.\n'))
    return unid_astroconverter
def unit_astroconvertida():
    unid_astroconvertido = int(input('Pressione 1, 2 ou 3 para selecionar a unidade para qual da qual você deseja converter e dê enter.\nExemplo: tenho um valor em Unidades Astronômicas e quero em Anos-Luz. Então você digita 3, referente à unidade Anos-Luz, neste caso.\n'))
    return unid_astroconvertido
def astrocomprimento_conv():
    astrocomprimento = float(input('Digite o valor de comprimento para ser convertido e pressione enter\n'))  
    return astrocomprimento

def unit_astroconverter_eng():
    print('ASTRONOMY UNIT CONVERTER\n')
    print('-------------------------------------\n')
    print('1 Astronomical Unit\n2 Parsec\n3 Light-Year\n')
    print('-------------------------------------\n')
    unid_astroconverter = int(input('Press 1, 2 or 3 to select the unit you want to convert from and press enter.\nExample: I have a value in Astronomical Units and I want it in Light Years. Then you type 1, referring to the Astronomical Unit, in this case.\n'))
    return unid_astroconverter
def unit_astroconvertida_eng():
    unid_astroconvertido = int(input('Press 1, 2 or 3 to select the unit to which you want to convert and press enter.\nExample: I have a value in Astronomical Units and I want it in Light Years. Then you type 3, referring to the Light Years unit, in this case.\n'))
    return unid_astroconvertido
def astrocomprimento_conv_eng():
    astrocomprimento = float(input('Type the length value to be converted and press enter\n'))  
    return astrocomprimento

# Obtém o nome da máquina local
#host = socket.gethostname()
host = 'localhost'
port = 9999

k = 0
while k == 0:
    print('SELECIONE A LÍNGUA\n')
    print('SELECT THE LANGUAGE\n')
    print('1 PORTUGUÊS-BR\n')
    print('1 PORTUGUESE-BR\n')
    print('2 INGLÊS\n')
    print('2 ENGLISH\n')
    lingua = int(input())
    if lingua == 1:
        f = 1
        while f == 1:
            # Cria um 'objeto socket'
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #Menu de escolha
            op = 0
            while op != 1 and op != 2:
                print('Selecione que tipo de conversão você deseja realizar:\n')
                print('1 Conversão de unidades de temperatura (Celsius, Fahrenheit e Kelvin)\n')
                print('2 Conversão de unidades da astronomia (Unidade Astronômica, Parsec e Ano-luz)\n')
                op = int(input('Digite 1 ou 2 para selecionar e pressione enter\n'))
                if op != 1 and op != 2:
                    print('Por favor, selecione uma opção válida (1 ou 2)')
                
            # Conexão ao host através da porta
            s.connect((host, port))
            opcao = str(op)
            s.send(opcao.encode('ascii'))
            if op == 1:
                unitconverter = str(unidade_converter())
                s.send(unitconverter.encode('ascii'))
                unitconvertida = str(unidade_convertida())
                s.send(unitconvertida.encode('ascii'))
                temperature = str(temperatura_conv())
                s.send(temperature.encode('ascii'))
            
            if op == 2:
                unitconverter = str(unit_astroconverter())
                s.send(unitconverter.encode('ascii'))
                unitconvertida = str(unit_astroconvertida())
                s.send(unitconvertida.encode('ascii'))
                comprimento = str(astrocomprimento_conv())
                s.send(comprimento.encode('ascii'))
                tm_km = s.recv(1024)
                print('Curiosidade: o valor convertido em quilômetros é %s\n' % tm_km.decode('ascii'))
        
            # Receba não mais do que 1024 bytes
            tm = s.recv(1024)    
            s.close()
            print('O valor, após a conversão desejada, é %s\n' % tm.decode('ascii'))


            # Perguntando ao usuário se ele deseja realizar outra conversão
            f = 0
            while f != 1 and f != 2:
                print('Você deseja fazer outra conversão?\n')
                print('1 Sim\n')
                print('2 Não\n')
                f = int(input('Digite 1 ou 2 para selecionar a opção desejada e pressione enter\n'))
                if f != 1 and f != 2:
                    print('Por favor, selecione uma opção válida (1 ou 2)')
        k = 2
    if lingua == 2:
        #roda programa em inglês
        f = 1
        while f == 1:
            # Cria um 'objeto socket'
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #Menu de escolha
            op = 0
            while op != 1 and op != 2:
                print('Select what type of conversion you want to perform:\n')
                print('1 Conversion of temperature units (Celsius, Fahrenheit and Kelvin)\n')
                print('2 Conversion of astronomy units (Astronomical Unit, Parsec and Light Year)\n')
                op = int(input('Type 1 or 2 to select and press enter\n'))
                if op != 1 and op != 2:
                    print('Please, select a valid option (1 or 2)')
            # Conexão ao host através da porta
            s.connect((host, port))
            opcao = str(op)
            s.send(opcao.encode('ascii'))
            if op == 1:
                unitconverter = str(unidade_converter_eng())
                s.send(unitconverter.encode('ascii'))
                unitconvertida = str(unidade_convertida_eng())
                s.send(unitconvertida.encode('ascii'))
                temperature = str(temperatura_conv_eng())
                s.send(temperature.encode('ascii'))
            
            if op == 2:
                unitconverter = str(unit_astroconverter_eng())
                s.send(unitconverter.encode('ascii'))
                unitconvertida = str(unit_astroconvertida_eng())
                s.send(unitconvertida.encode('ascii'))
                comprimento = str(astrocomprimento_conv_eng())
                s.send(comprimento.encode('ascii'))
                tm_km = s.recv(1024)
                print('Curiosity: the value converted into kilometers is %s\n' % tm_km.decode('ascii'))
        
            # Receba não mais do que 1024 bytes
            tm = s.recv(1024)    
            s.close()
            print('The value, after the desired conversion, is %s\n' % tm.decode('ascii'))

            # Perguntando ao usuário se ele deseja realizar outra conversão
            f = 0
            while f != 1 and f != 2:
                print('Would you like to do another conversion?\n')
                print('1 Yes\n')
                print('2 No\n')
                f = int(input('Type 1 or 2 to select the desired option and press enter\n'))
                if f != 1 and f != 2:
                    print('Please, select a valid option (1 or 2)')
        k = 2
    else:
        print('Selecione uma opção válida (1 ou 2)\n Select a valid option\n')
        k = 0


