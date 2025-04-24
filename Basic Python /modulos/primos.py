def opcion_dos():
    while True :
        try :

            #Metodo a llamar            
            def es_primo(numero): 
                if numero<1:
                    return False
                for i in range(2, int(numero ** 0.5)+1): #
                    if numero % i == 0:
                        return False
                return True

            #Metodo a llamar            
            def es_primo(numero): 
                if numero<1:
                    return False
                for i in range(2, int(numero ** 0.5)+1):
                    if numero % i == 0:
                        return False
                return True

            numeros_primos= []            
            #Inicio de programa
            cantidad_numeros = int(input('\n Cuantos numeros quieres introducir'))

            for _ in range(n):
                num = int(input('Introduce numero'))
                if es_primo(num):
                    print('Es PRIMO')
                    numeros_primos.append(num)
                else:
                    print(f"{num} No ES Primo")
            print(f"  NUMEROS PRIMOS \n{numeros_primos}")
            





            opcion_submnenu = input("""
                         *** ESTAS EN LA OPCION 2 NUMEROS PRIMOS ***
                        1- CONTINUAR EN NUMEROS PRIMOS
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
