from database.dao.common import GenericDAO
from database.models.book import Book

class BookDAO(GenericDAO):
    model = Book
    fields_to_json = ['id','title','description','created_on','updated_on']

bookdao = BookDAO()

