from flask_app import app
from flask_app.models.book import Book
from flask_app.models.author import Author
from flask_app.models.favorite import Favorite
from flask import redirect, render_template, request, url_for

# Type hinting imports
from werkzeug import Response
from typing import List


# Books Route
@app.route('/books', methods=['GET'])
@app.route('/books/<int:book_id>', methods=['GET'])
def books(book_id: int | None = None) -> str:
    """
    Gets all the books and displays them on the page with a menu to add a book.

    If there is an id the page only displays that book with a an option menu to
    have any of the authors favorite that book.
    """
    display_single: bool = False
    authors = []
    favorites = []

    if not book_id:
        books: List[Book] = Book.get_books()
    else:
        books: List[Book] = Book.get_books(True, book_id)
        favorites: List[Favorite] = Favorite.get_favorites('book', book_id)
        display_single = True

        authors: List[Author] = Author.get_authors()

    return render_template('books.html', books=books, display_single=display_single, authors=authors, favorites=favorites)


@app.route('/create_book', methods=['POST'])
def create_book() -> Response:

    book_data = request.form
    book_id: int = Book.create_book(book_data)

    return redirect(url_for('books', book_id=book_id))


@app.route('/books/add_favorite', methods=['POST'])
def add_favorite():
    favorite_data = request.form
    Favorite.add_favorite(favorite_data)
    book_id: int = int(favorite_data['book_id'])
    return redirect(url_for('books', book_id=book_id))
