import json

FILE_NAME = "zapiski.json"


def load_zapiski():
    try:
        with open(FILE_NAME, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_zapiski(zapiski):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(zapiski, f, ensure_ascii=False, indent=2)


def add_note(zapiski):
    text = input("Текст заметки: ")
    zapiski.append({"text": text, "done": False})
    save_zapiski(zapiski)
    print("Заметка добавлена!")


def show_notes(zapiski):
    if not zapiski:
        print("Заметок пока нет.")
        return
    for i, note in enumerate(zapiski, start=1):
        marker = "[x]" if note["done"] else "[ ]"
        print(f"{i}. {marker} {note['text']}")


def mark_done(zapiski):
    """Отмечает заметку по номеру как выполненную."""
    show_notes(zapiski)
    if not zapiski:
        return
    try:
        num = int(input("Номер заметки: "))
        note = zapiski[num - 1]
    except (ValueError, IndexError):
        print("Нет такой заметки.")
        return
    note["done"] = True
    save_zapiski(zapiski)
    print("Отмечено выполненной!")


def main():
    zapiski = load_zapiski()

    while True:
        print("\n=== Менеджер заметок ===")
        print("1. Добавить заметку")
        print("2. Показать все заметки")
        print("3. Отметить выполненной")
        print("4. Выйти")

        choice = input("Выбери действие: ")

        if choice == "1":
            add_note(zapiski)
        elif choice == "2":
            show_notes(zapiski)
        elif choice == "3":
            mark_done(zapiski)
        elif choice == "4":
            print("Пока!")
            break
        else:
            print("Не понял команду. Попробуй ещё раз.")


if __name__ == "__main__":
    main()