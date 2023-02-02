import connexion
import six

from swagger_server.models.book import Book  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server import util

books = []

def create_book(body):  # noqa: E501
    """Метод добавления новой книги в каталог

    Метод предназначен для сохранения в БД данных по новой книге. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Book
    """
    if connexion.request.is_json:
        body = Book.from_dict(connexion.request.get_json())  # noqa: E501

    if not body.book_id:
        i = str(len(books)+1)
        while [b for b in books if b.book_id==body.book_id]:
            i += 1
        body.book_id = i
    elif [b for b in books if b.book_id==body.book_id]:
        return {'error': 'Информация о книге с введеным id уже существует'}
    books.append(body)
    return body

def delete_book_by_id(id_):  # noqa: E501
    """Метод удаления книги по идентификатору

     # noqa: E501

    :param id: Идентификатор книги
    :type id: str

    :rtype: None
    """
    for i, book in enumerate(books):
        if book.book_id==id_:
            books.pop(i)
            return {'result': 'Информация о книге удалена'}
    return {'error': 'Книги с введным id не существует'}


def get_book_by_id(id_):  # noqa: E501
    """Метод получения книги по идентификатору

     # noqa: E501

    :param id: Идентификатор книги
    :type id: str

    :rtype: Book
    """
    book = [b for b in books if b.book_id==id_]
    if book:
        return book[0]
    else:
        return {'error': 'Книги с введным id существует'}


def get_books():  # noqa: E501
    """Метод получения книг

    Метод предназначен для получения списка всех книг, сохраненных в БД. # noqa: E501


    :rtype: List[Book]
    """
    return books


def update_book(body, id_):  # noqa: E501
    """Метод обновления книги в каталоге

    Метод предназначен для обновления в БД данных по имеющейся книге. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id: Идентификатор книги
    :type id: str

    :rtype: Book
    """
    if connexion.request.is_json:
        body = Book.from_dict(connexion.request.get_json())  # noqa: E501

    if body.book_id!=id_ and [b for b in books if b.book_id == body.book_id]:
        return {'error': 'Книга с таким id уже существует. Измените id'}

    book = [b for b in books if b.book_id==id_]
    if not book:
        return {'error': 'Книги с введным id не существует'}

    book = book[0]
    book.book_id = body.book_id
    book.author = body.author
    book.genre = body.genre
    book.title = body.title
    book.year = body.year

    return book
