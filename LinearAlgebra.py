import copy

class Matrix:
    def __init__(self, a, row=True):
        self.matrix = []
        if isinstance(a[0], Vector):
            for i in range(len(a)):
                a[i] = a[i].getVector()
                a[i] = [a[i][j][0] for j in range(len(a[i]))]
            row = False
        if row:
            self.matrix = a
        else:
            if isinstance(a[0], (int, float)):
                self.matrix = [[a[i]] for i in range(len(a))]
            else:
                self.matrix = [[a[i][j] for i in range(len(a))] for j in range(len(a[0]))]
                
        self.det = None    
    def getMatrix(self):
        return self.matrix
    def __str__(self):
        res = ''
        for i in self.matrix:
            for j in i:
                if j == -0:
                    j = 0
                if j - int(j) == 0:
                    j = int(j)
                res += (str(round(j,2)) + ' ')
            res += '\n'
        return res
    def toREF(self):
        matrix = copy.deepcopy(self.matrix)
        rows, cols = len(matrix), len(matrix[0])
        pivot_row, pivot_col = 0, 0
        self.det = 1
        while pivot_row < rows and pivot_col < cols:
            nonzero_pivot_row = None
            for i in range(pivot_row, rows):
                if matrix[i][pivot_col] != 0:
                    nonzero_pivot_row = i
                    break
            if nonzero_pivot_row is not None:
                # Swap current row with nonzero pivot row
                matrix[pivot_row], matrix[nonzero_pivot_row] = matrix[nonzero_pivot_row], matrix[pivot_row]
                self.det *= (-1)
                # Scale current row to make pivot element 1
                pivot = matrix[pivot_row][pivot_col]
                if pivot != 0:
                    matrix[pivot_row] = [val / pivot for val in matrix[pivot_row]]
                    self.det *= (pivot)
                # Subtract current row from all rows below it to eliminate elements in the current column
                for i in range(pivot_row+1, rows):
                    factor = matrix[i][pivot_col]
                    matrix[i] = [val - factor*matrix[pivot_row][j] for j, val in enumerate(matrix[i])]
                pivot_row += 1
            pivot_col += 1
        return Matrix(matrix)
    def toRREF(self):
        matrix = self.toREF().getMatrix()
        rows, cols = len(matrix), len(matrix[0])
        for row in range(rows-1, -1, -1):
            pivot_col = next((col for col in range(cols) if matrix[row][col] != 0), None)
            if pivot_col:
                matrix[row] = [val/matrix[row][pivot_col] for val in matrix[row]]
                for i in range(row-1, -1, -1):
                    factor = matrix[i][pivot_col]
                    matrix[i] = [val - factor*matrix[row][j] for j, val in enumerate(matrix[i])]
        return Matrix(matrix)        
    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Matrices must be of the same dimensions.")
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))])
    def __mul__(self, other):
        if isinstance(other, (Matrix, Vector)):
            if isinstance(other, Vector):
                other = other.vector
            if len(self.matrix[0]) != len(other.matrix):
                raise ValueError("Matrices cannot be multiplied.")
            product = [[0 for j in range(len(other.matrix[0]))] for i in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(other.matrix[0])):
                    for k in range(len(other.matrix)):
                        product[i][j] += self.matrix[i][k] * other.matrix[k][j]
            if len(product[0]) == 1:
                return Vector((Matrix(product)).transpose().getMatrix()[0])
            return Matrix(product)
        else:
            raise TypeError("Multiplication not supported for the given types.")    
    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[self.matrix[i][j]*other for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))])
        else:
            raise TypeError("Multiplication not supported for the given types.") 
    def transpose(self):
        return Matrix([[self.matrix[i][j] for i in range(len(self.matrix))] for j in range(len(self.matrix[0]))])
    def getDeterminants(self):
        if len(self.matrix) == len(self.matrix[0]):
            upper_triangle = self.toREF().getMatrix()
            for i in range(len(self.matrix)):
                self.det *= upper_triangle[i][i]
        if self.det == 0:
            self.det = 0
        if self.det - int(self.det) == 0:
            self.det = int(self.det)
        return round(self.det, 2)
    def inverse(self):
        if self.det == None:
            self.getDeterminants()
        if self.det != 0:
            matrix = copy.deepcopy(self.matrix)
            n = len(matrix)
            identity = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
            for i in range(n):
                for j in range(n):
                    matrix[i].append(identity[i][j])
            matrix = Matrix(matrix).toRREF().getMatrix()
            matrix = [[matrix[i][j] for j in range(n, 2*n)] for i in range(n)]
            return Matrix(matrix)
        return None
    def isInverse(self, matrix):
        inverse = self.inverse().getMatrix()
        matrix = matrix.getMatrix()
        try:
            for i in range(len(inverse)):
                for j in range(len(inverse[i])):
                    if abs(inverse[i][j] - matrix[i][j]) > 0.001:
                        return False
            return True
        except:
            return False   
    
class LinearSystem:
    def __init__(self, a, row = True):
        '''
        a: an array of lists/Vectors, including the y
        '''
        self.matrix = None
        self.solution = None
        
        # You haven't done the part if a is a list of Vectors
        if isinstance(a[0], Vector):
            for i in range(len(a)):
                a[i] = a[i].getVector()
                a[i] = [a[i][j][0] for j in range(len(a[i]))]
            row = False
        if row:
            self.matrix = Matrix(a)
        else:
            self.matrix = Matrix(a, row=False) 
    def __str__(self):
        matrix = self.matrix.getMatrix()
        res = ''
        for i in matrix:
            count = 0
            for j in i:
                if j == -0:
                    j = 0
                if j - int(j) == 0:
                    j = int(j)
                if count == len(matrix[0]) - 1:
                    res += ('| ' + str(round(j,2)))
                else:
                    res += (str(round(j,2)) + ' ')
                count += 1
            res += '\n'
        return res
    def solve(self):
        rref = self.matrix.toRREF().getMatrix()
        rows, cols = len(rref), len(rref[0])
        for i in range(rows):
            all_zeros = all(val == 0 for val in rref[i][:-1])
            if all_zeros and rref[i][-1] != 0:
                self.solution = 0
                return None
        if all_zeros or cols-1 > rows:
            self.solution = float('inf')
            return float('inf')
        solution = [0] * rows
        for i in range(rows-1, -1, -1):
            pivot_col = next((j for j in range(cols) if rref[i][j] != 0), None)
            if pivot_col:
                solution[i] = round(rref[i][-1], 2)
        self.solution = solution
        return solution
    def isConsistent(self):
        if self.solution == None:
            self.solve()
        return self.solution != 0
    def toREF(self):
        return self.matrix.toREF()
    def toRREF(self):
        return self.matrix.toRREF()
    def isHomogeneous(self):
        matrix = self.matrix.getMatrix()
        if self.solution == None:
            self.solve()
        return isinstance(self.solution, list) and all(matrix[i][-1] == 0 for i in range(len(matrix)))
    def isLinearlyIndependent(self):
        return isinstance(self.solution, list)  
        
class Vector:
    def __init__(self, a):
        '''
        a: an array of floats
        '''
        if isinstance(a, list):
            self.vector = Matrix(a, row=False)
        elif isinstance(a, Matrix):
            self.vector = a
    def getVector(self):
        return self.vector.getMatrix()
    def __str__(self):
        res = ''
        for i in self.vector.getMatrix():
            for j in i:
                if j - int(j) == 0:
                    j = int(j)
                res += (str(round(j,2)) + ' ')
            res += '\n'
        return res
    def __add__(self, other):
        return Vector(self.vector + other.vector)
    def __rmul__(self, other):
        return Vector((other * self.vector).transpose().getMatrix()[0])
    def __eq__(self, other):
        return isinstance(self, Vector) and isinstance(other, Vector) and self.getVector() == other.getVector()
    
class LinearCombination:
    def __init__(self, vectors):
        self.vectors = vectors
    def __eq__(self, vector):
        matrix = []
        for v in self.vectors:
            matrix.append(v)
        matrix.append(vector)
        return LinearSystem(matrix).isConsistent()

class LinearTransformation:
    def __init__(self, A):
        self.A = A
        pass
    def toT(self, u):
        try:
            return self.A*u
        except:
            return "Can't find T(u)"