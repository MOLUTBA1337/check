Этот скрипт создан для проверки!

<h1>Инструкция</h1>

<b>Запустите главный файл -> main.py</b>

static_file.py создан для редактирования приветственного текста
note.py отвечает за взаимодействие с базой данных


<h1>Документация</h1>

В файле note.py есть несколько методов

<h3>Создание записи</h3>

<code>
def create_record(self,title : str, description : str) -> None:
</code>

<h3>Метод для просмотра списков записей</h3>

<code>
def turn_notes(self) -> tuple:
</code>

<h3>Найти запись по айди</h3>
<code>
def find_note(self,id : int) -> Union[bool,tuple]:
</code>

<h3>Поиск записей по ключевому слову</h3>
<code>
def search_record(self,word : str) -> Union[tuple,bool]:
</code>

<h3>Удаление заметки</h3>
<code>
def delete_record(self,number : int) -> bool:
</code>