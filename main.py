from exceptions import *

__all__ = ["Matrix"]


class Matrix:
    def __init__(self, rows: int, columns: int, _type: type,
                 values: list | list[list[int | float, ...], ...] | None = None) -> None:
        self.rows = rows
        self.columns = columns
        self._type = _type
        self.values = values
        self.matrix = []
        
        if self._type == int:
            self._default = 0
        elif self._type == float:
            self._default = 0.0
        else:
            raise TypeValuesException(f"Type of {self._type} is not supporting!")
        
        if values is not None and self._validate():
            self.matrix = self.values.copy()
        else:
            self.matrix = []
        
    def _validate(self) -> bool | None:
        if len(self.values) == self.rows and len(self.values[0]) == self.columns:
            for lst in self.values:
                for element in lst:
                    if not isinstance(element, self._type):
                        raise TypeValuesException(f"{element} have type of {type(element)}! ({type(element)} != {self._type})")
            return True
        else:
            raise InitMatrixException(f"Cannot init matrix {self.rows}x{self.columns}, because 'values' have size "
                             f"{len(self.values)}x{len(self.values[0])}")
