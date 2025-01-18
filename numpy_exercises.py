import numpy as np

def array_creation_basics():
    print("\n=== Array Creation and Basics ===")
    
    # Create 1D array from 10 to 50
    arr1 = np.arange(10, 51)
    print("1D array from 10 to 50:", arr1)
    
    # Create 3x3 random array
    arr2 = np.random.random((3, 3))
    print("\n3x3 random array:\n", arr2)
    
    # Create arrays of zeros and ones
    zeros_arr = np.zeros(10)
    ones_arr = np.ones(10)
    print("\nArray of zeros:", zeros_arr)
    print("Array of ones:", ones_arr)
    
    # Create 5x5 identity matrix
    identity_matrix = np.eye(5)
    print("\n5x5 Identity matrix:\n", identity_matrix)
    
    # Create 4x4 matrix with values 1-16
    arr3 = np.arange(1, 17).reshape(4, 4)
    print("\n4x4 matrix with values 1-16:\n", arr3)

def indexing_and_slicing():
    print("\n=== Indexing and Slicing ===")
    
    # Create a sample 4x4 matrix
    matrix = np.arange(1, 17).reshape(4, 4)
    print("Original matrix:\n", matrix)
    
    # Access 3rd row, 2nd column
    element = matrix[2, 1]  # Remember 0-based indexing
    print("\nElement at 3rd row, 2nd column:", element)
    
    # Extract first three rows
    first_three_rows = matrix[:3, :]
    print("\nFirst three rows:\n", first_three_rows)
    
    # Replace even numbers with -1
    even_replaced = matrix.copy()
    even_replaced[even_replaced % 2 == 0] = -1
    print("\nEven numbers replaced with -1:\n", even_replaced)
    
    # Reverse rows and columns
    reversed_matrix = np.flip(np.flip(matrix, 0), 1)
    print("\nReversed matrix:\n", reversed_matrix)

def mathematical_operations():
    print("\n=== Mathematical Operations ===")
    
    # Create two 2x2 matrices
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    
    print("Matrix 1:\n", matrix1)
    print("\nMatrix 2:\n", matrix2)
    
    # Element-wise operations
    print("\nAddition:\n", matrix1 + matrix2)
    print("\nSubtraction:\n", matrix1 - matrix2)
    print("\nMultiplication:\n", matrix1 * matrix2)
    print("\nDivision:\n", matrix1 / matrix2)
    
    # Dot product
    mat1 = np.array([[1, 2, 3], [4, 5, 6]])  # 2x3
    mat2 = np.array([[7, 8], [9, 10], [11, 12]])  # 3x2
    dot_product = np.dot(mat1, mat2)
    print("\nDot product:\n", dot_product)
    
    # Statistical operations
    arr = np.array([1, 2, 3, 4, 5])
    print("\nArray:", arr)
    print("Sum:", np.sum(arr))
    print("Mean:", np.mean(arr))
    print("Median:", np.median(arr))
    print("Variance:", np.var(arr))
    print("Standard deviation:", np.std(arr))

def reshaping_and_flattening():
    print("\n=== Reshaping and Flattening ===")
    
    # Create and reshape 1D array to 4x4
    arr = np.arange(16)
    reshaped = arr.reshape(4, 4)
    print("Reshaped 4x4 matrix:\n", reshaped)
    
    # Flatten 2D array
    flattened = reshaped.flatten()
    print("\nFlattened array:", flattened)
    
    # Stack arrays
    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])
    vertical_stack = np.vstack((arr1, arr2))
    horizontal_stack = np.hstack((arr1, arr2))
    print("\nVertical stack:\n", vertical_stack)
    print("\nHorizontal stack:\n", horizontal_stack)

def boolean_indexing():
    print("\n=== Boolean Indexing and Filtering ===")
    
    # Create sample array with negative values
    arr = np.array([-3, -2, -1, 0, 1, 2, 3])
    negative_count = np.sum(arr < 0)
    print("Number of negative values:", negative_count)
    
    # Replace values > 50
    arr = np.array([30, 45, 60, 75, 90])
    arr[arr > 50] = 50
    print("\nArray with values capped at 50:", arr)
    
    # Filter odd numbers
    arr = np.arange(10)
    even_mask = arr % 2 == 0
    even_numbers = arr[even_mask]
    print("\nEven numbers:", even_numbers)

def special_functions():
    print("\n=== Special Functions and Operations ===")
    
    # Create linearly spaced points
    linear_space = np.linspace(-1, 1, 100)
    print("First 5 points of linear space:", linear_space[:5])
    
    # Generate and sort random integers
    random_ints = np.random.randint(5, 16, 10)
    sorted_ints = np.sort(random_ints)
    print("\nSorted random integers:", sorted_ints)
    
    # Matrix operations
    matrix = np.array([[1, 2], [3, 4]])
    determinant = np.linalg.det(matrix)
    inverse = np.linalg.inv(matrix)
    eigenvals, eigenvects = np.linalg.eig(matrix)
    
    print("\n2x2 Matrix:\n", matrix)
    print("Determinant:", determinant)
    print("Inverse:\n", inverse)
    print("Eigenvalues:", eigenvals)
    print("Eigenvectors:\n", eigenvects)

if __name__ == "__main__":
    array_creation_basics()
    indexing_and_slicing()
    mathematical_operations()
    reshaping_and_flattening()
    boolean_indexing()
    special_functions()
