import numpy as np
from functools import lru_cache

class HashMixin:
    '''Хэш вычисляется как сумма всех элементов матрицы, умноженная на её размерность'''
    def __hash__(self):
        return int(sum(sum(row) for row in self.data) * (self.row_count + self.col_count))


class Matrix(HashMixin):
    def __init__(self, data):
        if not all(len(row) == len(data[0]) for row in data):
            raise ValueError('All rows must have the same length')
        self.data = data
        self.row_count = len(data)
        self.col_count = len(data[0]) if self.row_count > 0 else 0


    def __add__(self, other):
        if self.row_count != other.row_count or self.col_count != other.col_count:
            raise ValueError('Matrices must have the same dimensions for addition')
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.col_count)]
            for i in range(self.row_count)
        ]
        return Matrix(result)


    def __mul__(self, other):
        if self.row_count != other.row_count or self.col_count != other.col_count:
            raise ValueError('Matrices must have the same dimensions for component-wise multiplication')
        result = [
            [self.data[i][j] * other.data[i][j] for j in range(self.col_count)]
            for i in range(self.row_count)
        ]
        return Matrix(result)

    @lru_cache(maxsize=None)
    def __matmul__(self, other):
        if self.col_count != other.row_count:
            raise ValueError('Number of columns in the first matrix must match number of rows in the second matrix for matrix multiplication')
        result = [
            [
                sum(self.data[i][k] * other.data[k][j] for k in range(self.col_count))
                for j in range(other.col_count)
            ]
            for i in range(self.row_count)
        ]
        return Matrix(result)


    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])


def main():
    np.random.seed(0)
    matrix1 = Matrix(np.random.randint(0, 10, (10, 10)).tolist())
    matrix2 = Matrix(np.random.randint(0, 10, (10, 10)).tolist())

    add_result = matrix1 + matrix2
    with open('artifacts/matrix+.txt', 'w') as f:
        f.write(str(add_result))

    mul_result = matrix1 * matrix2
    with open('artifacts/matrix*.txt', 'w') as f:
        f.write(str(mul_result))

    matmul_result = matrix1 @ matrix2
    with open('artifacts/matrix@.txt', 'w') as f:
        f.write(str(matmul_result))

    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[1, 0], [0, 1]])  
    C = Matrix([[4, 3], [2, 1]])  
    D = B

    assert hash(A) == hash(C)
    assert A != C
    assert B == D
    assert (A @ B).data != (C @ D).data

    with open('artifacts/A.txt', 'w') as f:
        f.write(str(A))
    with open('artifacts/B.txt', 'w') as f:
        f.write(str(B))
    with open('artifacts/C.txt', 'w') as f:
        f.write(str(C))
    with open('artifacts/D.txt', 'w') as f:
        f.write(str(D))
    with open('artifacts/AB.txt', 'w') as f:
        f.write(str(A @ B))
    with open('artifacts/CD.txt', 'w') as f:
        f.write(str(C @ D))
    with open('artifacts/hash.txt', 'w') as f:
        f.write(f'hash AB: {hash(A @ B)}\nhash CD: {hash(C @ D)}')

if __name__ == '__main__':
    main()