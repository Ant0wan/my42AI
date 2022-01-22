"""
Vectors
"""


class Vector:
    """Vector Class"""

    def __init__(self, values):
        self.__values = self._define_vector(values)
        self.__shape = self.define_shape(self.__values)

    def __str__(self):
        return str(self.__values)

    def __add__(self, vector):
        """Add two vectors together"""
        if isinstance(vector, Vector) and self.__shape == vector.shape:
            sum_values = vector.values
            if all(isinstance(val, list) for val in self.__values):
                for column_index in range(0, self.__shape[0]):
                    for row_index in range(0, self.__shape[1]):
                        sum_values[column_index][row_index] += self.__values[column_index][row_index]
            else:
                for row_index in range(0, self.__shape[1]):
                    sum_values[row_index] += self.__values[row_index]
            sum_vector = Vector(sum_values)
            return sum_vector
        raise ValueError("Can only add Vector types with same dimensions")

    @staticmethod
    def _vector_from_size(size):
        """Create vector made of size column with values from 0 to size"""
        vector = []
        for column in range(0, size):
            vector.append([float(column)])
        return vector

    @staticmethod
    def _vector_from_tuple(pair):
        """Create vector from tuple from [0] to [1]"""
        values = []
        if pair[0] == pair[1]:
            raise ValueError("Vector cannot be empty")
        elif pair[1] > pair[0]:
            for column in range(pair[0], pair[1]):
                values.append([float(column)])
        else:
            for column in range(pair[0], pair[1], -1):
                values.append([float(column - 1)])
        return values

    @staticmethod
    def _define_vector(vec):
        """Check only 1 and 2 dimensions vectors"""
        if not vec:
            raise ValueError("Vector cannot be empty")
        elif isinstance(vec, int):
            return Vector._vector_from_size(vec)
        elif isinstance(vec, tuple) and all(isinstance(val, int) for val in vec) and len(vec) == 2:
            return Vector._vector_from_tuple(vec)
        elif isinstance(vec, list):
            if all(isinstance(val, float) for val in vec):
                return vec
            elif all(isinstance(column, list) for column in vec):
                column_len = len(vec[0])
                for column in vec:
                    if not column:
                        raise ValueError("Vector cannot be empty")
                    if column_len != len(column):
                        raise ValueError("Value is not a correct vector")
                    if not all(isinstance(val, float) for val in column):
                        raise ValueError("Vector must be list of floats")
                return vec
        raise ValueError("Vector must be list of floats or list of lists of floats")

    @staticmethod
    def define_shape(vec):
        """Store dimension of the vector (row, column)"""
        #### ERROR in this function ###
        if isinstance(vec, list):
            if all(isinstance(val, float) for val in vec):
                return (1, len(vec))
            elif all(isinstance(column, list) for column in vec):
                return (len(vec), len(vec[0]))

    @property
    def values(self):
        return self.__values

    @property
    def shape(self):
        return self.__shape
