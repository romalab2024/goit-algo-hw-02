import queue
import random
from collections import deque

# ЗАВДАННЯ 1: Імітувати систему обробки заявок у сервісному центрі, використовуючи чергу (клас Queue).

# 1. СТВОРЮЄМО ЧЕРГУ ЗАЯВОК
request_queue = queue.Queue()

# 2. ФУНКЦІЯ: ГЕНЕРАЦІЯ НОВИХ ЗАЯВОК
def generate_request():
    """
    Функція зімітує створення нової заявки з унікальним номером і додає її до черги.
    """
    request_id = random.randint(1000, 9999)  # Генеруємо унікальний ID заявки
    request_queue.put(request_id)  # Додаємо заявку до черги
    print(f"Заявка {request_id} успішно додана до черги.")

# 3. ФУНКЦІЯ: ОБРОБКА ЗАЯВОК
def process_request():
    """
    Функція здійснює обробку заявки з черги.
    Знімає заявку з черги та імітує її обробку.
    """
    if not request_queue.empty():
        request_id = request_queue.get()  # Знимаємо заявку з черги
        print(f" Обробляється заявка {request_id}...")
        time.sleep(2)  # Імітуємо обробку
        print(f"✔️ Заявку {request_id} успішно оброблено!")
    else:
        print(" Черга пуста. Немає заявок для обробки.")


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

# ГОЛОВНИЙ ЦИКЛ ВИКОНАННЯ
if __name__ == "__main__":
    while True:
        print("\nОберіть завдання:")
        print("1. Система обробки заявок")
        print("2. Перевірка на паліндром")
        print("3. Перевірка симетричності дужок")
        print("4. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            print("\n--- Система обробки заявок ---")
            generate_request()
            process_request()
        elif choice == "2":
            print("\n--- Перевірка на паліндром ---")
            test_string = input("Введіть рядок: ")
            if is_palindrome(test_string):
                print(f"✔️ Рядок '{test_string}' є паліндромом.")
            else:
                print(f"❌ Рядок '{test_string}' не є паліндромом.")
        elif choice == "3":
            print("\n--- Перевірка симетричності дужок ---")
            test_string = input("Введіть рядок із дужками: ")
            if is_balanced_brackets(test_string):
                print(f"✔️ Рядок '{test_string}' є симетричним.")
            else:
                print(f"❌ Рядок '{test_string}' не є симетричним.")
        elif choice == "4":
            print("🚪 Завершення програми. Гарного дня!")
            break
        else:
            print("❌ Некоректний вибір. Спробуйте ще раз.")
