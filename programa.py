#Dimensión matriz
#El valor que ingrese el usuario en la variable "f" representará el numero de filas en dicha matriz
f=int(input("Ingresa el numero de filas:"))
#El valor que ingrese el usuario en la variable "c" representará el numero de columnas en dicha matriz
c=int(input("Ingresa el numero de columnas:"))
#matriz traspuesta
#Dicha matriz será representada como una lista
#Por medio de los datos ingresados anteriormente,se creara una matriz nula.
matriz=[]
for i in range(f):
    matriz.append([0]*c)
#El usuario ingresará los valores de la matriz
for j in range(f):
    for k in range(c):
        matriz[k][j]= int(input("Elemento %d,%d :" % (j,k)))
#Se imprimirá la matriz resultante
print(matriz)
