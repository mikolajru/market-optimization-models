import numpy as np

def calculate_determinant(matrix: np.ndarray) -> float:
    """
    Calculate determinant of the matrix.
    :param matrix: (np.ndarray): matrix.

    Returns:
        Determinant of the matrix

    Raises:
        None
    """

    result = np.linalg.det(matrix)
    result = round(result, 2)
    return result

if __name__ == '__main__':
    matrix_a = np.array([[1, -1, 2], [0, 1, 1], [-1, 3, -2]])
    calculated_determinant = calculate_determinant(matrix_a)
    print (f"The determinant of the matrix is: {calculated_determinant}")