import fire

class MathUtils:
    def print_numbers(self, n, current=1):
        """Выводит  все числа рекурсивно до заданного начиная с 1"""
        if current <= n:
            print(current, end=' ')
            self.print_numbers(n, current + 1)
    
    def max_two(self, number1: float, number2: float):
        """Возвращает самое  больше из  двух  чисел"""
        return number1 if number1 >= number2 else number2

if __name__ == '__main__':
    fire.Fire(MathUtils)