# ЗАВДАННЯ 3: Перевірка симетричності символів-розділювачів за допомогою стеку

def is_balanced_brackets(input_string):
    """
    Функція перевіряє, чи є символи-розділювачі у рядку симетричними.
    - Використовує стек для перевірки парності дужок.
    """
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}

    for char in input_string:
        if char in brackets.values():
            stack.append(char)  # Додаємо відкриваючі дужки до стеку
        elif char in brackets.keys():
            if stack and stack[-1] == brackets[char]:
                stack.pop()  # Видаляємо пару зі стеку
            else:
                return False

    return len(stack) == 0  # Симетрично, якщо стек порожній
