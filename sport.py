from colorama import Fore, Style, init #pip install colorama
# Инициализация библиотеки (необязательно для Windows, но рекомендуется)
#ascii https://patorjk.com/
init(autoreset=True)

def dayMenu():
    day = input(Fore.GREEN +"Введите день недели: ").capitalize()  # Делаем ввод с большой буквы для удобства
    if day == "Понедельник":
        print("Утро: \tКаша и молоко\nОбед: \tКурица с рисом\nУжин: \tОвощной салат")
    elif day == "Вторник":
        print("Утро: \tЯйца и тосты\nОбед: \tСуп с лапшой\nУжин: \tЗапеченная рыба")
    elif day == "Среда":
        print("Утро: \tПанкейки с мёдом\nОбед: \tТушёное мясо\nУжин: \tКотлеты с пюре")
    elif day == "Четверг":
        print("Утро: \tОвсянка с фруктами\nОбед: \tБорщ\nУжин: \tЗапеканка")
    elif day == "Пятница":
        print("Утро: \tЙогурт и гранола\nОбед: \tГречка с котлетой\nУжин: \tПицца")
    elif day == "Суббота":
        print("Утро: \tОмлет с сыром\nОбед: \tШашлык\nУжин: \tОвощное рагу")
    elif day == "Воскресенье":
        print("Утро: \tСырники\nОбед: \tПлов\nУжин: \tСалат Цезарь")
    else:
        print("Такого дня недели нет, попробуйте снова!")


def daily_calorie_intake():
    print("Чтобы узнать, сколько калорий вы сжигаете, заполните следующие поля.")

    # Получаем пол пользователя. Используем метод `.strip()` для удаления лишних пробелов, а `.lower()` — для приведения к нижнему регистру.
    input_sex = input("1. Напишите пол (\"м\" - для мужчин или \"ж\" - для женщин): ").strip().lower()

    if input_sex == "м":
        print("Ваш выбор - мужчина")
    elif input_sex == "ж":
        print("Ваш выбор - женщина")
    else:
        print("Некорректный ввод пола!")
        return

    try:
        weight = float(input("2. Ваш вес (кг): ").strip())  # Преобразуем строку в число для расчетов.
        height = float(input("3. Ваш рост (см): ").strip())
        age = float(input("4. Ваш возраст: ").strip())
    except ValueError:
        print("Ошибка ввода! Введите числа для веса, роста и возраста.")
        return

    # Рассчитываем базовый обмен веществ (BMR) на основе пола. Формулы взяты из Mifflin-St Jeor Equation.
    if input_sex == "м":
        bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
    elif input_sex == "ж":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.33 * age)

    print("\nВаш образ жизни:")
    print("1. Сидячий")
    print("2. Тренировки 1-3 раза в неделю")
    print("3. Занятия 3-5 дней в неделю")
    print("4. Интенсивные тренировки 6-7 раз в неделю")
    print("5. Спортсмены, выполняющие упражнения чаще, чем раз в день")

    activity_choice = input("Введите один номер из вышеперечисленных: ").strip()

    # Используем словарь для хранения коэффициентов активности.
    # Это упрощает код и делает его более читаемым.
    activity_factors = {
        "1": 1.2,
        "2": 1.375,
        "3": 1.55,
        "4": 1.725,
        "5": 1.9
    }

    # Проверяем, есть ли введенный пользователем выбор в словаре.
    if activity_choice in activity_factors:
        # Рассчитываем суточную норму калорий, умножая BMR на коэффициент активности.
        daily_calories = bmr * activity_factors[activity_choice]
        print(f"{daily_calories:.2f} - это количество калорий, необходимых для правильного функционирования организма")
    else:
        print("Некорректный выбор уровня активности!")
        return

    # Рассчитываем суточную норму белков, жиров и углеводов.
    # Для белков используется коэффициент 1.5 г на 1 кг веса.
    protein = weight * 1.5
    # Для жиров — 0.8 г на 1 кг веса.
    fat = weight * 0.8
    # Для углеводов — 2 г на 1 кг веса.
    carbohydrates = weight * 2

    print("Ваша суточная норма:")
    print(f"Белки: {protein:.2f} г")
    print(f"Жиры: {fat:.2f} г")
    print(f"Углеводы: {carbohydrates:.2f} г")
    print("Совет: Следите за сбалансированным питанием для здоровья и хорошего самочувствия.")

def shop():
    try:
        # Чтение всех продуктов из файла
        print("Название    -  Белки  -     Жиры  -   Углеводы  - Общее количество калорий")
        with open("Product.txt", "r", encoding="utf-8") as file:
            all_products = file.readlines()
            for product in all_products:
                print(product.strip())  # Выводим каждый продукт

        # Запрос на поиск продукта
        print("\nВведите название продукта, который Вы хотите купить: ")
        product_search = input().lower()  # Преобразуем введенное в нижний регистр для поиска

        # Поиск продукта в списке
        found_product = next((product for product in all_products if product.lower().find(product_search) != -1), None)

        if found_product:
            # Добавляем продукт в корзину
            with open("Korzina.txt", "a", encoding="utf-8") as file:
                file.write(product_search + "\n")
            print(f"Ваш товар '{product_search}' успешно добавлен в корзину!")
        else:
            print("Такого товара нет в списке.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


def on_show_all():
    try:
        # Очистка экрана
        print("Корзина\n ")

        # Чтение всех товаров в корзине
        with open("Korzina.txt", "r", encoding="utf-8") as file:
            all_products = file.readlines()
            for product in all_products:
                print(product.strip())  # Выводим каждый товар в корзине

        # Запрос на подтверждение покупки
        print("\nВы хотите купить содержимое корзины? (да / нет)\n")
        user_input = input().lower()

        if user_input == "да":
            # Очистка корзины
            with open("Korzina.txt", "w", encoding="utf-8") as file:
                file.truncate(0)  # Очищаем файл
            print("\033c", end="")
            print("Вы только что купили содержимое Вашей корзины\nСпасибо за покупку\n")
        elif user_input == "нет":
            # Очистка корзины
            with open("Korzina.txt", "w", encoding="utf-8") as file:
                file.truncate(0)  # Очищаем файл
            print("\033c", end="")
            print("Вы не купили ни один продукт\n")
        else:
            print("Неверный ответ, корзина не была очищена.")

    except FileNotFoundError:
        print("Ваша корзина пока пуста\n")



while True:
    print("1. Меню на неделю")
    print("2. Калькулятор подсчета калорий")
    print("3. Магазин с продуктами")
    print("4. Список выбранных продуктов")
    print("5. Выход")

    choice = input("Выберите действие (1-5)")
    if choice == "1":
        print("Ваше меню на один день")
        dayMenu()
    elif choice == "2":
        print("Норма калорий")
        daily_calorie_intake()
    elif choice == "3":
        print("Наше меню")
        shop()
    elif choice == "4":
        print("Cписок выбранных продуктов")
        on_show_all()
    elif choice == "5":
        print("Конец")
        print(r"""
  /$$$$$$                  /$$       /$$
 /$$__  $$                | $$      | $$
| $$  \__/  /$$$$$$   /$$$$$$$  /$$$$$$$ /$$   /$$
| $$       /$$__  $$ /$$__  $$ /$$__  $$| $$  | $$
| $$      | $$  \ $$| $$  | $$| $$  | $$| $$  | $$
| $$    $$| $$  | $$| $$  | $$| $$  | $$| $$  | $$
|  $$$$$$/|  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$$
 \______/  \______/  \_______/ \_______/ \____  $$
                                         /$$  | $$
                                        |  $$$$$$/
                                         \______/
""")
        break
    else:
        print("Неверный ввод, попробуйте снова")
