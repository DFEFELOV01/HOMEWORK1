"""
Домашнее задание №1
Функции и структуры данных
"""
# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def power_numbers(*args):
    return [x**2 for x in args]

def filter_numbers(numbers, filter_type):
    if filter_type == EVEN:
        return list(filter(lambda x: x % 2 == 0, numbers))
    elif filter_type == ODD:
        return list(filter(lambda x: x % 2 != 0, numbers))
    elif filter_type == PRIME:
        def is_prime(n):
            if n <= 1:
                return False
            elif n <= 3:
                return True
            elif n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
        return list(filter(is_prime, numbers))

# Пример использования функций:
#if__name__ == "__main__":
print("Квадраты чисел:", power_numbers(1,2,3,4,5))  # Вывод: [1, 4, 25, 49]
print("Нечетные числа:", filter_numbers([1, 2, 3], 'odd'))  # Вывод: [1, 3]
print("Четные числа:", filter_numbers([2, 1, 3, 5, 4], "even"))  # Вывод: [2, 4]
print("Простые числа:", filter_numbers([1,2,3,4,5,6,7,8,9],"prime"))
