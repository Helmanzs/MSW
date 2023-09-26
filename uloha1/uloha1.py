import numpy as np
import timeit
import math
import random


def timer(python, library, repetitions):
    python_time = timeit.timeit(python, number=repetitions)
    numpy_time = timeit.timeit(library, number=repetitions)

    print(
        f"Python: {python_time}\nNumPy: {numpy_time}\nFaster is {'Python' if python_time < numpy_time else 'NumPy'}\n\n"
    )


# SCALAR
def python_scalar():
    vector1 = [random.random() for _ in range(100000)]
    vector2 = [random.random() for _ in range(100000)]
    python_scalar = sum(x * y for x, y in zip(vector1, vector2))
    return python_scalar


def numpy_scalar():
    vector1 = np.random.rand(100000)
    vector2 = np.random.rand(100000)
    numpy_scalar = np.dot(vector1, vector2)
    return numpy_scalar


# INTEGRATION
def python_integration():
    f = lambda x: x**2
    step = 0.001
    x_values = [x * step for x in range(int(1 / step))]
    python_integration = sum(f(x) * step for x in x_values)
    return python_integration


def numpy_integration():
    f = lambda x: x**2
    x = np.linspace(0, 1, 100)
    y = f(x)

    numpy_integration = np.trapz(y, x)
    return numpy_integration


# MATRIXES ADDITION
def python_matrix():
    python_matrix_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    python_matrix_B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    result = []
    for col in range(len(python_matrix_A)):
        new_col = []
        for row in range(len(python_matrix_A[0])):
            new_col.append(python_matrix_A[col][row] + python_matrix_B[col][row])
        result.append(new_col)

    return result


def numpy_matrix():
    numpy_matrix_A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    numpy_matrix_B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    return np.add(numpy_matrix_A, numpy_matrix_B)


# QUADRATIC
def python_quadratic():
    a = 1
    b = -2
    c = 3
    discriminant = b**2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    if discriminant == 0:
        x = -b / (2 * a)
        return x

    real = -b / (2 * a)
    imaginary = math.sqrt(-discriminant) / (2 * a)
    solution1 = complex(real, imaginary)
    solution2 = complex(real, -imaginary)
    return solution1, solution2


def numpy_quadratic():
    a = 1
    b = -2
    c = 3
    return np.roots([a, b, c])


# SUM OF SQUARES IN ARRAY
def python_squares():
    n = 10**6
    numbers = list(range(1, n + 1))

    sum_of_squares = 0
    for num in numbers:
        sum_of_squares += num**2

    return sum_of_squares


def numpy_squares():
    n = 10**6
    numbers = np.arange(1, n + 1)

    sum_of_squares = np.sum(numbers**2)
    return sum_of_squares


timer(python_scalar, numpy_scalar, 1000)
timer(python_integration, numpy_integration, 1000)
timer(python_matrix, numpy_matrix, 1000)
timer(python_quadratic, numpy_quadratic, 1000)
timer(python_squares, numpy_squares, 1000)
