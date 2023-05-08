# Linear Algebra Library

## Matrix

`matrix = Matrix(a, row=True)`

Creates a new Matrix object with the specified array `a`. 
- `a` can be a list of lists. If `row=True` (default), the inner lists represent rows. Set `row=False` to make the inner lists represent columns instead.
- `a` can be a list of Vectors (see the Vector class below). In this case, the `row` argument is not required.

`matrix.getMatrix() -> list`

Returns the two-dimensional array that represents the matrix.

`matrix.toREF() -> Matrix`

Returns the Matrix object in row echelon form.

`matrix.toRREF() -> Matrix`

Returns the Matrix object in reduced row echelon form.

`matrixA + matrixB -> Matrix` 

Adds two matrices together using the `+` operator and returns a new Matrix object representing the sum. Raises a ValueError if the two matrices do not have the same dimensions.

`matrixA * matrixB -> Matrix` 

Multiplies two matrices together and returns a new Matrix object representing the product. Raises a ValueError if the matrices cannot be multiplied or if the argument is not a Matrix object.

`matrixA * vectorB -> Vector` 

Multiplies a matrix by a Vector and returns a new Vector object representing the product. Raises a ValueError if they cannot be multiplied or if the argument is not a Vector object.

`c * matrix -> Matrix` 

Multiplies a matrix by a scalar and returns a new Matrix object representing the result. Raises a TypeError if the argument is not an int or float.

`matrix.transpose() -> Matrix` 

Returns a new Matrix object that is the transpose of the original matrix.

`matrix.getDeterminants() -> float` 

Calculates the determinant of the matrix and returns the result.

`matrix.inverse() -> Matrix` 

Calculates the inverse of the matrix and returns a new Matrix object representing the inverse. Returns None if the matrix is not invertible.

`matrixA.isInverse(matrixB) -> Boolean` 

Checks if the given matrix is the inverse of the current matrix.

## Linear System 

`system = LinearSystem(a: lists, row=True) `

Creates a new LinearSystem object with the specified array a, which should be a list of lists or Vector objects. `a` should include the `y` values of the system. The row parameter is a boolean value that specifies whether the lists or vectors are arranged in rows or columns.

`system.solve() -> None/inf/list ` 

Solves the linear system.
- Returns a list of numbers representing the solution if there's one solution
- Returns None there's no solution 
- Returns inf if there are infinitely many solutions.

`system.getMatrix() -> Matrix`

Returns a new Matrix object representing the coefficients of the equations in the linear system.

`system.toREF() -> Matrix` 

Returns the Matrix object of the system of linear equations in row echelon form.

`system.toRREF() -> Matrix`

Returns the Matrix object of the system of linear equations in reduced row echelon form.

`system.isConsistent -> Boolean`

Returns a boolean value indicating whether the system of linear equations has a solution.

`system.isHomogeneous() -> Boolean`

Returns a boolean value indicating whether the system of linear equations is homogeneous.

`system.isLinearlyIndependent() -> Boolean`

Returns a boolean value indicating whether the system of linear equations is linearly independent.

## Vector

`vector = Vector(a)` 

Create a new Vector object with `a`.
- `a` can be an array of floats
- `a` can be a Matrix object with one column

`vector.getVector()` 

Returns the two-dimensional array that represents the vector.

`vectorA + vectorB -> Vector` 

Adds two vectors together using the `+` operator and returns a new Vector object representing the sum. Raises a ValueError if the two vectors do not have the same dimensions.

`c * vector -> Vector` 

Multiplies a vector by a scalar and returns a new Vector object representing the result. Raises a TypeError if the argument is not an int or float.

`vectorA == vectorB -> Boolean`


## Linear Combination

`combination = LinearCombination(vectors)`

Create a new LinearCombination object with a list of Vector objects vectors.

`combination == vector -> Boolean`

Returns True if the vector is a linear combination of the vectors in vectors, otherwise returns False.

## Linear Transformation

`transformation = LinearTransformation(A)`

Create a new LinearTransformation object with a Matrix `A` that represents the standard matrix.

`transformation.toT(u) -> Vector`

Returns the result Vector after applying the linear transformation from the Vector `u` to `T(u)` through the standard matrix `A`. If an error occurs during the operation, prints a message and returns None.



