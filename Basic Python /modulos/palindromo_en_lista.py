"""
pedir al usuario una frase o palabra y verificar si es palindromo y despues meterlo en una lista
"""


def opcion_ocho():
     while True :
        try :
            






            opcion_submnenu = input("""
                         *** ESTAS EN LA OPCION 8 PALINDROMO Y LISTA ***
                        1- CONTINUAR EN PALINDROMO Y LISTA
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