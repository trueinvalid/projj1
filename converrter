import tkinter as tk

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
