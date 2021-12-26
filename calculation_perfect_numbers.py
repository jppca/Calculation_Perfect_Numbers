# @utor:Juan Pablo Parra Cajero.
# Descripción:
# Algoritmo que realiza el cálculo de números perfectos.
# Fecha:28/09/2021

# itertools ayuda a generar una iteración infinita para un for
import itertools
# Función para aplicar test de Lucas Lehmer


def Lucas_Lehmer(iNumber):
    iValidatorS = 4
    iNumberM = 2 ** iNumber - 1
    if(iNumber == 2):
        return True
    for _ in range(iNumber - 2):
        iValidatorS = ((iValidatorS * iValidatorS) - 2) % iNumberM
    return iValidatorS == 0

# Función para verificar si un número es primo


def Is_Prime(iNumber):
    if iNumber % 2 == 0:
        return iNumber == 2
    for nControl_i in range(2, iNumber):
        if iNumber % nControl_i == 0:
            return False
    return True

# Función para calcular números perfectos


def Pefect_Number(iLimit):
    # Variable contador incremental
    nAccountant_i = 0
    # Variable de control para validar que se llego al limite
    nControl_i = 0
    # Ciclo donde se verifica si un número es primo y si cumple con el test de Lucas Lehmer
    for _ in itertools.count(1):
        if Is_Prime(nAccountant_i) and Lucas_Lehmer(nAccountant_i):
            # Se muestra en pantalla el resultado de la aplicación de la formula de EUCLIDES y EULER
            # para determinar números perfectos
            print("Número Perfecto " + str(nControl_i+1) +
                  " *****************************************")
            print((2**nAccountant_i-1)*(2**(nAccountant_i-1)))
            print(
                "-----------------------------------------------------------------------------------")
            nControl_i += 1
            if(iLimit <= nControl_i):
                break
        nAccountant_i += 1


# Ejecución de la función que calcula números perfectos.
# El algoritmo calcula 20 números perfectos sin ningún problema en unos cuantos minutos.
Pefect_Number(20)
