import numpy as np

def find_shape(matrix):
    return matrix.shape

def find_number_of_dimensions(matrix):
    return matrix.ndim

def find_number_of_elements(matrix):
    return matrix.size

def find_data_type(matrix):
    return matrix.dtype

def find_determinant(matrix):
    
    return np.linalg.det(matrix)

def find_inverse(matrix):
    return np.linalg.inv(matrix)

def find_rank(matrix):
    return np.linalg.matrix_rank(matrix)

def find_eigen_values(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues

def find_eigen_vectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvectors

def find_transpose(matrix):

    return matrix.T

def addition(matrix1, matrix2):
    return matrix1 + matrix2

def subtraction(matrix1, matrix2):
    return matrix1 - matrix2

def scalar_multiplication(scalar, matrix):
    return scalar * matrix

def matrix_multiplication(matrix1, matrix2):
    return matrix1 @ matrix2
