import queue
import time
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

# 4. ГОЛОВНИЙ ЦИКЛ ПРОГРАМИ
def main_queue_system():
    print("\n ВІТАЄМО У СИСТЕМІ ОБРОБКИ ЗАЯВОК!")
    while True:
        print("\n1. Створити нову заявку")
        print("2. Обробити заявку")
        print("3. Вийти")
        choice = input("\nВаш вибір: ")
        
        if choice == "1":
            generate_request()
        elif choice == "2":
            process_request()
        elif choice == "3":
            print("🚪 Вихід із системи. Гарного дня!")
            break
        else:
            print(f"❌ Рядок '{user_input}' не є паліндромом.")
            print(" Некоректний вибір. Спробуйте ще раз.")
