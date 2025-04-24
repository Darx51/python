<<<<<<< HEAD
# 1- SERIE FIBONACCI
=======
from modulos import fibonacci, primos, bisiesto_par_impar, calculadora, n_letras_en_frace, n_mayor_menor,adivina_numero, palindromo_en_lista, suma_listas, ordenar_lista_y_eliminar_duplicados
>>>>>>> f0091693afa6e3149e360a97fdd5681e33c0fc93

<<<<<<< HEAD
n = int('dame un numero')

a=0
b=1
var=a+b
while var<n :
    print(var)
    
=======
    


def opcion_salir():
    print('HASTA PRONTO 🚀')
    exit()

def menu_principal():
     while True:
        opcion = input("""   ELIJE UN NUMERO DE EJERCICIO
        1- SERIE FIBONACCI  
        2- NUMEROS PRIMOS  
        3- PAR O IMPAR 
        4- CALCULADORA 
        5- CANTIDAD DE LETRAS EN FRASE
        6- NUMERO MAYOR Y MENOR
        7- ADIVINA NUMERO
        8- PALINDROMO EN LISTA
        9- SUMA Y MULTIPLICACION DE LISTAS DE DIFERENTES TAMANOS
        10- ORDENAR Y ELIMINAR EN LISTAS
        X Press X para SALIR 
                           """).strip().lower()             
        try:
            opcion
            match opcion:
                case "1":
                    fibonacci.opcion_uno()
                case "2":
                    primos.opcion_dos()
                case "3":
                    bisiesto_par_impar.opcion_tres()
                case "4":
                    calculadora.opcion_cuatro()
                case "5":
                    n_letras_en_frace.opcion_cinco() 
                case "6":
                    n_mayor_menor.opcion_seis() 
                case "7":
                    adivina_numero.opcion_siete() 
                case "8":
                    palindromo_en_lista.opcion_ocho() 
                case "9":
                    suma_listas.opcion_nueve() 
                case "10":
                    ordenar_lista_y_eliminar_duplicados.opcion_diez() 
                case "x":
                    opcion_salir() 
                    
        except ValueError:
            print('El valor ingresado no es un numero valido')    

menu_principal()
>>>>>>> f0091693afa6e3149e360a97fdd5681e33c0fc93

