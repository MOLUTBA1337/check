import sqlite3
from typing import Union

class Note:
    #Подключение к базе данных
    __connection = sqlite3.connect("database/notebook.db")
    cursor = __connection.cursor()

    #создание записи
    def create_record(self,title : str, description : str) -> None:
        self.cursor.execute("INSERT INTO note(title,description) VALUES(?,?)",(title.lower(),description,))
        self.__connection.commit()
    
    #список записей
    def turn_notes(self) -> tuple:
        return self.cursor.execute("SELECT * FROM note").fetchall()
    
    #найти запись по айди
    def find_note(self,id : int) -> Union[bool,tuple]:
        check = self.cursor.execute("SELECT title,description FROM note WHERE id = ?",(id,)).fetchone()

        if not check:
            return False
        return check

    #поиск записей по ключевому слову
    def search_record(self,word : str) -> Union[tuple,bool]:
        result = self.cursor.execute("SELECT id,title FROM note WHERE title LIKE ?",("%"+word.lower()+"%",)).fetchall()
        if result:
            return result
        return False
    
    #удалить запись
    def delete_record(self,number : int) -> bool:
        check = self.cursor.execute("SELECT * FROM note WHERE id = ?",(number,)).fetchone()

        if check:
            self.cursor.execute("DELETE FROM note WHERE id = ?",(number,))
            self.__connection.commit()
            return True
        return False


