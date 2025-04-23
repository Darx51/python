


def opcion_uno():
    while True :
        try :
            n = int(input('\nNUMERO PARA SERIE FIBONACCI \n'))
            a=0
            b=1
            var=a+b              
            print('\n')
            print(b)
            print(var)
            for i in range(a, n):
                a=b
                b=var
                var = a+b
                print(var)        

            opcion_submnenu = input("""
                         *** ESTAS EN LA SERIE DE FIBONACCI ***
                        1- CONTINUAR EN LA SERIE FIBONACCI
                        2- VOLVER AL MENU PRINCIPAL
                        3- SALIR COMPLETAMENTE """)

            if opcion_submnenu == "1":
                continue
            elif opcion_submnenu == "2":
                break
            elif opcion_submnenu == "3":
                print('HASTA PRONTO 🚀')
                exit()
            else:
                print('OPCION NO VALIDA')
            
        except ValueError:
            print('El valor ingresado no es un numero valido')