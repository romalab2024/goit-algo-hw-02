# ЗАВДАННЯ 2: Перевірка, чи є рядок паліндромом, використовуючи двосторонню чергу (deque).

def is_palindrome(input_string):
    """
    Функція перевіряє, чи є заданий рядок паліндромом.
    - Ігнорує пробіли та регістр символів.
    """
    # Нормалізуємо рядок: видаляємо пробіли, переводимо в нижній регістр
    normalized_string = ''.join(char.lower() for char in input_string if char.isalnum())

    # Створюємо двосторонню чергу (deque) з символів рядка
    char_deque = deque(normalized_string)

    # Порівнюємо символи з обох кінців deque
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True