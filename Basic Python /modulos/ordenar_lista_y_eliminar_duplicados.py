def opcion_diez():
     while True :
        try :
            






            opcion_submnenu = input("""
                         *** ESTAS EN LA OPCION 10 ORDEN Y ELIMINACION EN LISTAS ***
                        1- CONTINUAR EN ORDEN Y ELIMINACION EN LISTAS
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