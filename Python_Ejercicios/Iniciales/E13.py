"""Ejercicio 13: Implementa la clase “Matriz” con los atributos int rows, int columns e int[rows][columns] matrix,
que contenga los siguientes métodos: 
    - getNumberRows(): devuelve el número de filas de la matriz.
    - getNumberColumns(): devuelve el número de columnas de la matriz.
    - setElement(int x, int j, int element): cambia el valor de la matriz en [x][j] por el valor de [element].
    - addMatrix(int[][] matrix): suma todos los elementos de la matriz actual a los elementos de [matrix],
    y el resultado se almacena en la matriz inicial. Si [matrix] no tiene el mismo número de filas y columnas 
    que la matriz inicial, la operación no se puede realizar (notificalo).
    - multMatrix(int[][] matrix]: multiplica todos los elementos de la matriz actual a los elementos de [matrix],
    y el resultado se almacena en la matriz inicial. Si [matrix] no tiene el mismo número de filas y columnas que
    la matriz inicial, la operación no se puede realizar (notificalo)."""


class Matriz:
    def __init__(self, rows, columns, matrix):
        self.rows = rows
        self.columns = columns
        self.matrix = matrix
        
    def getNumberRows(self):
        return self.rows
    
    def getNumberColumns(self):
        return self.columns
    
    def setElement(self, x, j, element):
        self.matrix[x][j] = element
        
    def addMatrix(self, matrix):
        if len(matrix) == self.rows and len(matrix[0]) == self.columns:
            for i in range(self.rows):
                for j in range(self.columns):
                    self.matrix[i][j] += matrix[i][j]
        else:
            print("La matriz no tiene el mismo número de filas y columnas que la matriz inicial")
            
    def multMatrix(self, matrix):
        if len(matrix) == self.rows and len(matrix[0]) == self.columns:
            for i in range(self.rows):
                for j in range(self.columns):
                    self.matrix[i][j] *= matrix[i][j]
        else:
            print("La matriz no tiene el mismo número de filas y columnas que la matriz inicial")
            
    def toString(self):
        for i in range(self.rows):
            for j in range(self.columns):
                print(self.matrix[i][j], end=" ")
            print()
            

matriz = Matriz(2, 2, [[1, 2], [3, 4]])
print("Número de filas:", matriz.getNumberRows())
print("Número de columnas:", matriz.getNumberColumns())
print("Matriz inicial:")
matriz.toString()

matriz.addMatrix([[1, 2], [3, 4]])
print("Matriz después de sumar:")
matriz.toString()

matriz.multMatrix([[1, 2], [3, 4]])
print("Matriz después de multiplicar:")
matriz.toString()