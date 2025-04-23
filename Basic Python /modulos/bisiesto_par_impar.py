
"""
Verificar si un año es bisiesto
Un año es bisiesto si: divisible por 4, pero no por 100, excepto si también es divisible por 400 
y decir si es par o impar.
"""


def opcion_tres():
     while True :
        try :
            






            opcion_submnenu = input("""
                         *** ESTAS EN LA OPCION 3 PAR O IMPAR ***
                        1- CONTINUAR EN NUMEROS PAR O IMPAR
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
