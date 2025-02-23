[09:43, 23.02.2025] +996 999 103 406: import tkinter as tk

# Раскладки клавиатуры
eng_layout = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"
rus_layout = "йцукенгшщзхъфывапролджэячсмитьбю."


# Функция перевода текста
def convert_layout():
    text = entry.get()
    choice = var.get()

    if choice == 1:
        result = translate(text, eng_layout, rus_layout)
    else:
        result = translate(text, rus_layout, eng_layout)

    result_label.config(text="Результат: " + result)


# Функция перевода
def translate(text, from_layout, to_layout):
    converted = []
    for ch in text:
        index = from_layout.find(ch)
        converted.append(to_layout[index] if index != -1 else ch)
    return "".join(converted)


# Создаем окно
window = tk.Tk()
window.title("Переключатель раскладки")
window.geometry("4…
[09:49, 23.02.2025] +996 999 103 406: # Начальные данные: список покупок (изменяемый) и популярные товары (кортеж - неизменяемый)
shopping_list = []
popular_items = ("хлеб", "молоко", "яйца")  # Товары, которые всегда можно купить, неизменяемый список


# Функция для отображения списка покупок
def show_list():
    print("\nВаш список покупок:")
    if shopping_list:
        for item in shopping_list:
            print("-", item)
    else:
        print("Список пока пуст.")
    print("Часто покупаемые товары:", popular_items)


# Функция для добавления товара в список
def add_item(item):
    if item not in shopping_list:
        shopping_list.append(item)
        print(f"'{item}' добавлен в список покупок.")
    else:
        print(f"'{item}' уже в списке покупок.")


# Функция для удаления товара из списка
def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' удален из списка покупок.")
    else:
        print(f"'{item}' не найден в списке покупок.")


# Функция для проверки наличия товара в списке
def check_item(item):
    if item in shopping_list or item in popular_items:
        print(f"'{item}' есть в списке покупок или среди часто покупаемых товаров.")
    else:
        print(f"'{item}' нет в списке покупок.")

def sort_list():
    shopping_list.sort()
    print("Список покупок отсортирован по алфавиту.")

def count_items():
    print(f"В вашем списке покупок {len(shopping_list)} товаров.")


# Основной цикл программы
while True:
    print("\nМеню:")
    print("1. Показать список покупок")
    print("2. Добавить товар")
    print("3. Удалить товар")
    print("4. Проверить наличие товара")
    print("5. Выйти")
    print("6. Сортировать список покупок")
    print("7. Количество товаров")

    choice = input("Выберите действие (1-5): ")

    if choice == "1":
        show_list()
    elif choice == "2":
        item = input("Введите название товара, который хотите добавить: ")
        add_item(item)
    elif choice == "3":
        item = input("Введите название товара, который хотите удалить: ")
        remove_item(item)
    elif choice == "4":
        item = input("Введите название товара для проверки: ")
        check_item(item)
    elif choice == "5":
        print("Выход из программы. Хорошего дня!")
        break
    elif choice == "6":
        sort_list()
    elif choice == "7":
        count_items()

    else:
        print("Неверный ввод, попробуйте снова.")
