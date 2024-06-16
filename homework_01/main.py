# Домашнее задание №1
# Функции и структуры данных

# filter types
ODD = "ODD"
EVEN = "even"
PRIME = "prime"

def power_numbers(*args):
    # Возвращает список квадратов переданных чисел
    return [x**2 for x in args]

def is_prime(x):
    # Функция, которая проверяет, является ли число x простым
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def filter_numbers(numbers, filter_type):
    # Фильтрует список чисел в зависимости от типа фильтрации(нечетные, четные и простые)
    if filter_type == EVEN:
        return list(filter(lambda x: x % 2 == 0, numbers))
    elif filter_type == ODD:
        return list(filter(lambda x: x % 2 != 0, numbers))
    elif filter_type == PRIME:
        return list(filter(is_prime, numbers))

# Пример использования функций:
if __name__ == "__main__":
    print("Квадраты чисел:", power_numbers(1, 2, 3, 4, 5))  # Вывод: [1, 4, 9, 16, 25]
    print("Нечетные числа:", filter_numbers([1, 2, 3], ODD))  # Вывод: [1, 3]
    print("Четные числа:", filter_numbers([2, 1, 3, 5, 4], EVEN))  # Вывод: [2, 4]
    print("Простые числа:", filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], PRIME))  # Вывод: [2, 3, 5, 7]
