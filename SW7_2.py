def add_expense():
    category = input("Введите категорию расхода: ")
    amount = input("Введите сумму: ")
    description = input("Введите описание: ")

    with open("expenses.txt", "a", encoding="utf-8") as f:
        f.write(f"{category};{amount};{description}\n")

def show_expenses():
    print("\nТекущие расходы:")
    try:
        with open("expenses.txt", "r", encoding="utf-8") as f:
            for line in f:
                category, amount, description = line.strip().split(";")
                print(f"{category}: {amount} руб — {description}")
    except FileNotFoundError:
        print("Файл расходов пока не создан.")

while True:
    print("\nМеню:")
    print("1 — Добавить расход")
    print("2 — Показать все расходы")
    print("3 — Выход")
    choice = input("Выберите пункт меню: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        break
    else:
        print("Неверный выбор. Повторите ввод.")
