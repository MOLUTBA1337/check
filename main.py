from texts import static_texts
from notebook.note import Note
from sys import exit

def main():
    #Приветственный текст
    print(static_texts.first_greetings)

    first_action = input(">>")

    #вызов функции
    call_func_dict = {
        1 : add_note,
        2 : find_note,
        3 : view_note,
        4 : delete_note,
        5 : exit
    }

    if first_action.isdigit():
        first_action = int(first_action)

        call_func = call_func_dict.get(first_action)

        if call_func != None:
            call_func()
        else:
            print("[-] Такой команды нету!")
        
        next_action = input("Хотите продолжить?\nДа - 1\nНет - 2\n\n>>")

        if next_action.isdigit():
            
            next_action = int(next_action)  
            if next_action == 1:
                main()
            
            elif next_action == 2:
                return
            
            else:
                print("[-]Набранного вами номера не существует!")
        
        else:
            print("[-] Такой команды нету!")
    
    else:
        print("[-] Такой команды нету!")

#функция добавления заметки
def add_note():
    note = Note()
    title = input("Введите название заголовка\n\n>>")
    description = input("Введите описание\n\n>>")
    note.create_record(title,description)
    print("\n[+] Заметка сохранена!")

#функция просмотра список всех заметок
def find_note():
    note = Note()
    notebook = note.turn_notes()
    if not notebook:
        print("\n[-] Заметок нет!\n")
        main()
    for notes in notebook:
        print(f"{notes[1]} - {notes[0]}\n")
    
    second_action = input("Хотите посмотреть заметку более подробно?\nДа - 1\nНет - 2\n\n>>")
    if second_action.isdigit():
        second_action = int(second_action)
        if second_action == 1:
            number_note = input("Введите номер заметки\n>>")
            if number_note.isdigit():
                need_note = note.find_note(int(number_note))
                if need_note:
                    print("\n\n".join(need_note))
                else:
                    print("[-] Такой заметки не существует!")
            else:
                print("[-] Такой команды нету!")
        else:
            main()
    else:
        print("[-] Такой команды нету!")

#функция поиска заметок по ключевому слову
def view_note():
    note = Note()
    word = input("Введите ключевое слово\n\n>>")
    notes = note.search_record(word)
    if notes:

        print("Название - номер")
        for note in notes:
            print(f"[+]{note[1].capitalize()} - {note[0]}")
            print()
    else:
        print("[-] Заметок с таким ключевым словом не существует!\n")


#функция удаления записи
def delete_note():
    class_note = Note()

    notes = class_note.turn_notes()
    if notes:

        print("Название - номер")
        for note in notes:
            print(f"[+]{note[1].capitalize()} - {note[0]}")
            print()
    else:
        print("[-] Заметок вовсе нет!\n")
        return

    num = input("Введите номер заметки\n")


    if num.isdigit():
        result = class_note.delete_record(int(num))
        if result:
            print("[+] Заметка успешна удалена!\n")
        else:
            print("[-] Заметка не найдена!\n")
    else:
        print("[-] Такой команды нету!")

if __name__ == "__main__":
    main()
