import numpy as np

class FileSaveMixin:
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))


class PrettyDisplayMixin:
    def __str__(self):
        return np.array_str(self.data, precision=2, suppress_small=True)


class CoolMatrix(FileSaveMixin, PrettyDisplayMixin):
    def __init__(self, data):
        self._data = np.array(data)
        self._row_count = self._data.shape[0]
        self._col_count = self._data.shape[1] if len(self._data.shape) > 1 else 1


    @property
    def data(self):
        return self._data


    @data.setter
    def data(self, new_data):
        self._data = np.array(new_data)
        self._row_count = self._data.shape[0]
        self._col_count = self._data.shape[1] if len(self._data.shape) > 1 else 1


    @property
    def row_count(self):
        return self._row_count


    @property
    def col_count(self):
        return self._col_count


    def __add__(self, other):
        return CoolMatrix(self._data + other._data)


    def __mul__(self, other):
        return CoolMatrix(self._data * other._data)


    def __matmul__(self, other):
        return CoolMatrix(self._data @ other._data)

def main():
    np.random.seed(0)
    matrix1 = CoolMatrix(np.random.randint(0, 10, (10, 10)).tolist())
    matrix2 = CoolMatrix(np.random.randint(0, 10, (10, 10)).tolist())

    add_result = matrix1 + matrix2
    add_result.save_to_file('artifacts/cool_matrix+.txt')
    mul_result = matrix1 * matrix2
    mul_result.save_to_file('artifacts/cool_matrix*.txt')
    matmul_result = matrix1 @ matrix2
    matmul_result.save_to_file('artifacts/cool_matrix@.txt')

if __name__ == '__main__':
    main()