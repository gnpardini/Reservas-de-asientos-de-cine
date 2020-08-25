"""Desarrolle un programa que permita realizar reservas en una sala de cine de barrio
de N filas con M butacas por cada fila. Las filas se deberán referenciar con las le-
tras desde la A y las butacas con los números desde el 1. Desarrollar las siguien-
tes funciones y utilizarlas en un mismo programa:
mostrar_butacas: Mostrará por pantalla el estado de cada una de las butacas
del cine por pantalla. Se deberá mostrar antes de que el usuario realice la re-
serva y se volverá a mostrar luego de la misma, con los estados actualizados.
reservar: Deberá recibir una matriz y la butaca seleccionada, y actualizará la
matriz en caso de estar disponible dicha butaca. La función devolverá
True/False si logró o no reservar la butaca.
cargar_sala: recibirá una matriz como parámetro y la cargará con valores
aleatorios para simular una sala con butacas ya reservadas.
butacas_libres: Recibirá como parámetro la matriz y retornará cuántas buta-
cas desocupadas hay en la sala.
butacas_contiguas: Buscará la secuencia más larga de butacas libres conti-
guas en una misma fila y devolverá las coordenadas de inicio de la misma."""

import random

#Funciones

def generarMatriz(filas,columnas):
    matriz = []
    
    for f in range(filas):
        
        fila = []
        
        for c in range (columnas):
        
            
            fila.append(0)
            
        matriz.append(fila)
            
    return matriz
        
        

def numerarAsientos(asientos):
    
    asientosNumero = []
    
    numero = 1
    
    for i in range (asientos):
        
        asientosNumero.append(numero)
        
        numero = numero + 1
        
    return asientosNumero
        

def mostrarButacas(numeracion):
    
    print("NÚMERO DE ASIENTO")
    print(numeracion)
    print("BUTACAS")
    print("0 = Libres, 1 = ocupada")
    
    

                
def validarAsiento(asientosNumeros):
    
   asiento = int(input("Seleccione el asiento que desea"))
   cantidadDeAsientos = len(asientosNumeros)
   
   while ((asiento > cantidadDeAsientos) or (asiento < 1))and (asiento != -1):
       asiento = int(input("El asiento seleccionado no existe. Seleccione nuevamente el asiento que desea"))
       
   return asiento
                
def generarFilasConLetras(matriz,filas,letras):

    letra = -1
    
    largoLetras = len(letras)
    
    contador = 0
    for f in range (filas):
            
        letra = letras[f]
            
        indiceLetra = f
            
        print("Fila",letra, matriz[f])
            
        
        contador = contador + 1
        letra = indiceLetra + 1
        
    return contador,letra

                
def obtenerIndiceDeFila(letras,fila):
    
    indiceFila = -1
    
    for i in range (len(letras)):
        
        if (fila == letras[i]):
            indiceFila = i
            
            
    return indiceFila
                    
                
def obtenerIndiceDeAsiento(columna):
    
    indiceDeAsiento = columna - 1
        
    return indiceDeAsiento
        
        

def reservarAsientos(matriz,indiceFila,indiceColumna):
    
    asiento = matriz[indiceFila][indiceColumna]
    
    if asiento == 0:
        
        matriz[indiceFila][indiceColumna] = 1
        
        return True

    else:
        
        return False
        
    
def cargarSala(matriz,columnas,filas):
    
   
    for i in range (filas):
        
        for c in range (columnas):
            matriz[i][c] = random.randint(0,1)
            
            
def calcularButacasLibres(matriz,filas,columnas):
    
    contador = 0
    
    for i in range (filas):
    
        for c in range (columnas):
            
            if matriz[i][c] == 0:
                contador = contador + 1
    return contador
    
        
def mostrarButacasLibres(contador):
    
    print("La cantidad de butacas libres (0) es de",contador)
    
def generarListaDeButacasDisponiblesPorFila(matriz,filas,columnas):

    
    butacasDisponiblesPorFila = []
    
    for f in range (filas):
        
        contadorDeButacasLibresPorFila = 0
        
        for c in range (columnas):
        
            if matriz[f][c] == 0:
                
                contadorDeButacasLibresPorFila = contadorDeButacasLibresPorFila + 1
                
        butacasDisponiblesPorFila.append(contadorDeButacasLibresPorFila)
   
    return butacasDisponiblesPorFila

def calcularFilaConMasButacasContiguas(indiceDeFila,matriz,filas,columnas):
    
    mayorContinuidad = 0 #TOTALFILA
    
    filaConMayorContinuidad = -1 #Fila especifica
   
    for i in range (filas):
        contador = 0 
        
        continuidad = False #Inicio bandera en False, por default
        
        mayorContinuidadDeFila = 0 #Mayor continuidad de esa fila especifica
        
        for c in range (columnas):
           
           if matriz[i][c] == 0: #Si la columna de esa fila = 0, cambio valor de bandera y sumo 1
               continuidad = True
               contador = contador + 1
            
           else:
               if contador > mayorContinuidadDeFila: #Si la columna de esa fila es 1, me fijo si lo que sumé en el contador es
                                                    #mayor que lo que ya guardé en la mayor continuidadDeFila, si lo es, la mayor continuidad de la fila
                                                    #pasa a valer lo que el contador. E inicio nuevamente el contador en 0
                   mayorContinuidadDeFila = contador
               contador = 0
               
        if mayorContinuidadDeFila > mayorContinuidad: #Si la mayor continuidad de esa fila es mayor a la continuidad ya guardada, la mayor continuidad pasa a valor
                                                     #la mayor continuidad de esa fila y por ultimo guardamos el indice de la fila con mayor COntinuidad para devolver
            mayorContinuidad = mayorContinuidadDeFila
            filaConMayorContinuidad = i
    
    return filaConMayorContinuidad
    
        
def mostrarListaDeButacasDisponiblesPorFila (listaDeButacasDisponiblesPorFila,matriz,filas,letras):

    
    for i in range (filas):
        
    
        print("La fila",letras[i],"posee",listaDeButacasDisponiblesPorFila[i],"asientos disponibles")
        
def mostrarFilaConMasButacasContiguasVacias(butacasContiguas,letras):
    
    print("La fila con más butacas contiguas es la ",letras[butacasContiguas])
            
   
#Main
letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","W","X","Y","Z"]
filas = random.randint(15,20)
asientos = random.randint(15,20)
numeracion = numerarAsientos(asientos)
matriz = generarMatriz(filas,asientos)
mostrarButacas(numeracion)
cantidadDeFilas,letra = generarFilasConLetras(matriz,filas,letras)


asiento = validarAsiento(numeracion)

while asiento != -1:
    indiceAsiento = obtenerIndiceDeAsiento(asiento)
    fila = (input("Ingrese la fila que desea "))
    indiceDeFila = obtenerIndiceDeFila(letras,fila)
    while (indiceDeFila == -1) or (indiceDeFila >= filas):

        fila = (input("ERROR. Fila inexistente.Ingrese la fila que desea "))
        indiceDeFila = obtenerIndiceDeFila(letras,fila)
        
    resultadoDeReserva = reservarAsientos(matriz,indiceDeFila,indiceAsiento)
    if resultadoDeReserva == True:
        print("La reserva se ha generado con éxito")
    else:
        print("El asiento se encuentra reservado. Intentelo nuevamente")
    mostrarButacas(numeracion)
    cantidadDeFilas,letra = generarFilasConLetras(matriz,filas,letras)
    
    asiento = validarAsiento(numeracion)
    
print("Ocupación de sala")   
cargarSala(matriz,asientos,filas)
cantidadDeFilas,letra = generarFilasConLetras(matriz,filas,letras)   
    
butacasLibres = calcularButacasLibres(matriz,filas,asientos)
mostrarButacasLibres(butacasLibres)

listaDeButacasDisponiblesPorFila = generarListaDeButacasDisponiblesPorFila(matriz,filas,asientos)
mostrarListaDeButacasDisponiblesPorFila(listaDeButacasDisponiblesPorFila,matriz,filas,letras)
butacasContiguas = calcularFilaConMasButacasContiguas(indiceDeFila,matriz,filas,asientos)
mostrarFilaConMasButacasContiguasVacias(butacasContiguas,letras)
