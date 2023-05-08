from LinearAlgebra import *

'''
Matrix Methods
'''
# create matrixA from a list of lists
a = [[1,2,3],[4,5,6], [7,8,9]]
matrixA = Matrix(a)
print("Matrix A is: ")
print(matrixA)

# create matrixB from a list of Vectors
v1, v2, v3 = Vector([0,1,2]), Vector([3,0,3]), Vector([7,6,5])
matrixB = Matrix([v1, v2, v3])
print("Matrix B is: ")
print(matrixB)

# transform matrixA into REF form
matrixA_REF = matrixA.toREF()
print("The REF form of matrixA is: ")
print(matrixA_REF)

# transform matrixB into RREF form
matrixB_RREF = matrixB.toRREF()
print("The RREF form of matrixB is: ")
print(matrixB_RREF)

# addition and multiplication of matrixA and matrixB
sum = matrixA + matrixB
print("matrixA + matrixB = ")
print(sum)

product = matrixA * matrixB
print("matrixA * matrixB = ")
print(product)

scalar_product = 2*matrixA
print("2 * matrixA = ")
print(scalar_product)

# transpose of matrixB
matrixB_T = matrixB.transpose()
print("Transpose of matrixB: ")
print(matrixB_T)

# determinants of matrixA and matrixB:
detA = matrixA.getDeterminants()
detB = matrixB.getDeterminants()
print("Determinants of matrixA: ", detA)
print("Determinants of matrixB: ", detB)

print()
# inverse of matrixA and matrixB:
matrixA_i = matrixA.inverse()
matrixB_i = matrixB.inverse()
print("Inverse of matrixA: ")
print(matrixA_i)
print("Inverse of matrixB: ")
print(matrixB_i)

# check if matrixB_i is inverse of matrixB
print("matrixB_i is inverse of matrixB: ", matrixB_i.isInverse(matrixB))

print()
'''
LinearSystem Methods
'''
# create systemA from a list of lists
a = [[1,2,3,4],[4,5,6,7],[7,8,9,10]]
systemA = LinearSystem(a)
print("System A is: ")
print(systemA)

# create systemB from a list of Vectors
v1, v2, v3, v4 = Vector([0,1,2]), Vector([3,0,3]), Vector([7,6,5]), Vector([4,6,2])
systemB = LinearSystem([v1, v2, v3, v4])
print("System B is: ")
print(systemB)

# solve sytemA and systemB:
resA = systemA.solve()
resB = systemB.solve()
print("Solutions of systemA is: ", resA)
print("Solutions of systemB is: ", resB)

print()
# print REF and RREF forms of systemA and systemB
print("REF form of systemA: ")
print(systemA.toREF())
print("RREF form of systemB: ")
print(systemB.toRREF())

# check if systemA and systemB are consistent
print("sytemA is consistent: ", systemA.isConsistent())
print("sytemB is consistent: ", systemB.isConsistent())

print()
# check if systemA and systemB are homogeneous
print("sytemA is homogeneous: ", systemA.isHomogeneous())
print("sytemB is homogeneous: ", systemB.isHomogeneous())

print()
# check if the columns of systemA and systemB are linearly independent
print("The columns of A is linearly independent: ", systemA.isLinearlyIndependent())
print("The columns of B is linearly independent: ", systemB.isLinearlyIndependent())

print()
'''
Vector Methods
'''
# create vectorA from a list
vectorA = Vector([1,2,3])
print("Vector A is: ")
print(vectorA)

# create matrixB from a list of Vectors
matrixOneColumn = Matrix([[4], [5], [6]])
vectorB = Vector(matrixOneColumn)
print("Vector B is: ")
print(vectorB)

# addition and multiplication of vectorA and vectorB
sum = vectorA + vectorB
print("vectorA + vectorB = ")
print(sum)

product = matrixA * vectorA
print("matrixA * vectorA = ")
print(product)

scalar_product = 2*vectorB
print("2 * vectorB = ")
print(scalar_product)

# compare if vectorA is equal to vectorB
print("vectorA is equal to vectorB: ", vectorA == vectorB)

print()
'''
Linear Combination Methods
'''
# create a linear combination of vectorA and vectorB
combination = LinearCombination([vectorA, vectorB])

# check if vectorC is in the linear combination
vectorC = Vector([7, 8, 9])
print("vectorC is in the linear combination: ", combination == vectorC)

print()
'''
Linear Transformation
'''
# transform a vector in R4 to R3 through a standard matrix A
# matrix A has size 3x4
A = Matrix([[1,0,3,4],[1,5,6,2],[7,0,9,1]])
u = Vector([1,0,2,8])
transformation = LinearTransformation(A)
v = transformation.toT(u)
print("Vector u after transform into R3 is: ")
print(v)

