# Conversão de KM/h e m/s

while True:
    print('Escolha uma das áreas:')
    print('''
    1 - Cinemática
    2 - Calorimetria
    3 - Matemáticas
    ''')
    area_selecionada = int(input(" "))
    if area_selecionada == 1:
        print('Cinemática: ')
        print('''
        1 - De KM/h para m/s
        2 - De m/s para KM/h
        ''')
        opcao_selecionada = int(input(" "))
        if opcao_selecionada == 1:
            valor = float(input('Digite a grandeza em KM/h: '))
            convertido = valor / 3.6
            print(f'{valor: .2f} KM/h equivalem a {round(convertido)} m/s')
        elif opcao_selecionada == 2:
            valor = float(input('Digite a grandeza em m/s: '))
            convertido = valor * 3.6
            print(f'{valor: .2f} m/s equivalem a {convertido} KM/h')
        elif opcao_selecionada == 0:
            pass
    if area_selecionada == 2:
        print('Calorimetria: ')
        print('''
        Celsius:
        1 - Conversão de Cº para Fº
        2 - Conversão de Cº para Kº

        Fahrenheit:
        3 - Conversão de Fº para Cº
        4 - Conversão de Fº para K

        Kelvin:
        5 - Conversão de K para Cº
        6 - Conversão de K para Fº 
        ''')
        opcao_selecionada = int(input(' '))
        if opcao_selecionada == 1:
            valor = float(input('Digite a grandeza em Cº: '))
            convertido = valor*1.8 + 32
            print(f'{valor} Cº equivalem a {convertido} Fº: ')
        elif opcao_selecionada == 2:
            valor = float(input('Digite a grandeza em Cº: '))
            convertido = valor + 273
            print(f'{valor} Cº equivalem a {convertido}K: ')
        elif opcao_selecionada == 3:
            valor = float(input('Digite a grandeza em Fº'))
            convertido = (valor - 32)/1.8
            print(f'{valor} Fº equivalem a {convertido} Cº')
        elif opcao_selecionada == 5:
            valor = float(input('Digite a grandeza em Kelvin: '))
            convertido = valor - 273
            print(f'{valor}K equivalem a {convertido} Cº: ')