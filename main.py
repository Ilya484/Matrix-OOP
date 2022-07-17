from exceptions import *

__all__ = ["Matrix"]


class Matrix:
    def __init__(self, rows: int, columns: int, _type: type,
                 values: list | list[list[int | float, ...], ...] | None = None) -> None:
        self.__rows = rows
        self.__columns = columns
        self.__type = _type
        self.__values = values
        self.__matrix = []

        if self.__type == int:
            self.__default = 0
        elif self.__type == float:
            self.__default = 0.0
        else:
            raise TypeValuesException(f"Type of {self.__type} is not supporting!")

        self.__matrix = []
        if values is not None and self.__validate():
            self.__matrix = self.__values.copy()
        else:
            self.__matrix = [[self.__default] * self.__columns for _ in range(self.__rows)]

        del self.__values
        del self.__default

    def print(self):
        for string in self.__matrix:
            print(*string, sep="\t")

    def __validate(self) -> bool | None:
        if len(self.__values) == self.__rows and len(self.__values[0]) == self.__columns:
            for lst in self.__values:
                for element in lst:
                    if not isinstance(element, self.__type):
                        raise TypeValuesException(
                            f"{element} have type of {type(element)}! ({type(element)} != {self.__type})")
            return True
        else:
            raise InitMatrixException(f"Cannot init matrix {self.__rows}x{self.__columns}, because 'values' have size "
                                      f"{len(self.__values)}x{len(self.__values[0])}")

    def __check_type(self,  obj):
        return isinstance(obj, (float, int, Matrix)), type(obj)

    def __getitem__(self, key):
        x, y = key
        return self.__matrix[x - 1][y - 1]

    def __setitem__(self, key, value):
        if not isinstance(value, self.__type):
            raise TypeValuesException(
                            f"{value} have type of {type(value)}! ({type(value)} != {self.__type})")
        x, y = key
        self.__matrix[x - 1][y - 1] = value

    def __mul__(self, other):
        if not (t := self.__check_type(other))[0]:
            raise TypeError(f"can't use * for {type(other)} and Matrix")

        if t[1] in (int, float):
            new = [[0] * self.__columns for _ in range(self.__rows)]
            if t[1] == int:
                type_ = self.__type
            else:
                type_ = float

            for i in range(self.__rows):
                for j in range(self.__columns):
                    new[i][j] = other * self.__matrix[i][j]
            return Matrix(self.__rows, self.__columns, type_, new)
        else:
            type_ = float

    def __repr__(self):
        return f"Matrix: type of {self.get_type()}; size of {self.get_size()}"


    def __rmul__(self, other):
        return self * other

    def get_size(self):
        return f"{self.__rows}x{self.__columns}"

    def get_type(self):
        return str(self.__type).split()[-1][1:-2]
