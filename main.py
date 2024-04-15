import os
import json
# import uuid
from datetime import datetime
import random

def generate_id():
    return str(random.randint(10000, 99999))
def create_note(note_title, note_content):
    # note_id = str(uuid.uuid4())
    note_id = generate_id()
    note = {
        "id": note_id,
        "title": note_title,
        "content": note_content,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "last_modified": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    filename = "notes.json"
    notes = []

    if os.path.exists(filename):
        with open(filename, "r") as file:
            notes = json.load(file)

    notes.append(note)

    with open(filename, "w") as file:
        json.dump(notes, file, indent=4)

    print("Заметка создана.")

def view_notes():
    filename = "notes.json"

    if not os.path.exists(filename):
        print("Список заметок пуст.")
        return

    with open(filename, "r") as file:
        notes = json.load(file)

    print("Список заметок:")
    for note in notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата создания: {note['created_at']}, Последнее изменение: {note['last_modified']}")

def view_notes(filter_date=None):
    filename = "notes.json"

    if os.path.exists(filename):
        with open(filename, "r") as file:
            notes = json.load(file)
            if filter_date:
                filtered_notes = [note for note in notes if datetime.strptime(note["created_at"], "%Y-%m-%d %H:%M:%S").date() == datetime.strptime(filter_date, "%Y-%m-%d").date()]
                if filtered_notes:
                    for note in filtered_notes:
                        print(f"ID: {note['id']}")
                        print(f"Заголовок: {note['title']}")
                        print(f"Содержание: {note['content']}")
                        print(f"Дата создания: {note['created_at']}")
                        print(f"Последнее изменение: {note['last_modified']}")
                        print("----------------------------")
                else:
                    print("Заметок за указанную дату нет.")
            else:
                for note in notes:
                    print(f"ID: {note['id']}")
                    print(f"Заголовок: {note['title']}")
                    print(f"Содержание: {note['content']}")
                    print(f"Дата создания: {note['created_at']}")
                    print(f"Последнее изменение: {note['last_modified']}")
                    print("----------------------------")
    else:
        print("Список заметок пуст.")
def read_note(note_id):
    filename = "notes.json"

    if not os.path.exists(filename):
        print("Заметки отсутствуют.")
        return

    with open(filename, "r") as file:
        notes = json.load(file)

    for note in notes:
        if note['id'] == note_id:
            print(f"Заголовок: {note['title']}")
            print(f"Дата создания: {note['created_at']}")
            print(f"Последнее изменение: {note['last_modified']}")
            print(f"Содержимое: {note['content']}")
            break
    else:
        print("Заметка не найдена.")

def edit_note(note_id, new_content):
    filename = "notes.json"
    found = False

    if not os.path.exists(filename):
        print("Заметки отсутствуют.")
        return

    with open(filename, "r") as file:
        notes = json.load(file)

    for note in notes:
        if note['id'] == note_id:
            note['content'] = new_content
            note['last_modified'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            found = True
            break

    if found:
        with open(filename, "w") as file:
            json.dump(notes, file, indent=4)
        print("Заметка отредактирована.")
    else:
        print("Заметка не найдена.")

def delete_note(note_id):
    filename = "notes.json"
    found = False

    if not os.path.exists(filename):
        print("Заметки отсутствуют.")
        return

    with open(filename, "r") as file:
        notes = json.load(file)

    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            found = True
            break

    if found:
        with open(filename, "w") as file:
            json.dump(notes, file, indent=4)
        print("Заметка удалена.")
    else:
        print("Заметка не найдена.")

while True:
    print("Меню:")
    print("1. Создать заметку")
    print("2. Просмотреть список заметок")
    print("3. Просмотреть заметки по дате")
    print("4. Прочитать заметку")
    print("5. Редактировать заметку")
    print("6. Удалить заметку")
    print("7. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        note_title = input("Введите заголовок заметки: ")
        note_content = input("Введите содержимое заметки: ")
        create_note(note_title, note_content)
    elif choice == "2":
        view_notes()
    elif choice == "3":
        filter_date = input("Введите дату в формате ГГГГ-ММ-ДД: ")
        view_notes(filter_date)
    elif choice == "4":
        note_id = input("Введите идентификатор заметки: ")
        read_note(note_id)
    elif choice == "5":
        note_id = input("Введите идентификатор заметки, которую хотите отредактировать: ")
        new_content = input("Введите новое содержимое заметки: ")
        edit_note(note_id, new_content)
    elif choice == "6":
        note_id = input("Введите идентификатор заметки, которую хотите удалить: ")
        delete_note(note_id)
    elif choice == "7":
        break
    else:
        print("Некорректный выбор. Попробуйте еще раз.")


