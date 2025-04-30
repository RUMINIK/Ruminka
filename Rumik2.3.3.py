class CalculationLine:
    def __init__(self):
        self.__line = ""

    def set_last_symbol(self, symbol):
        """Добавляет символ в конец строки."""
        self.__line += symbol

    def get_calculation_line(self):
        """Возвращает текущее значение строки."""
        return self.__line

    def get_last_symbol(self):
        """Возвращает последний символ строки."""
        return self.__line[-1] if self.__line else None

    def delete_last_symbol(self):
        """Удаляет последний символ из строки."""
        if self.__line:
            self.__line = self.__line[:-1]

calc_line = CalculationLine()
calc_line.set_last_symbol('5')
calc_line.set_last_symbol('+')
calc_line.set_last_symbol('3')
print(calc_line.get_calculation_line())
print(calc_line.get_last_symbol())
calc_line.delete_last_symbol()
print(calc_line.get_calculation_line())



