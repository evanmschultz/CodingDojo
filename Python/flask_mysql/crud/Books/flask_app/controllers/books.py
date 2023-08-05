from flask_app import app
from flask_app.models.book import Book
from flask_app.models.author import Author
from flask_app.models.favorite import Favorite
from flask import redirect, render_template, request, url_for

# Type hinting imports
from werkzeug import Response
from typing import List, Tuple

from pprint import pprint


# Books Route
@app.route('/books', methods=['GET'])
@app.route('/books/<int:book_id>', methods=['GET'])
def books(book_id: int | None = None) -> str:
    """
    Gets book(s) and displays them on the page.

    If (book_id) is not provided, the page displays all books.
    If an (book_id) is provided, the page only displays the book with that ID
    with a list of all the authors who favorited the book as well as all the authors 
    in the database so the user can have the author favorite the displayed book.

    Returns:
        str: The rendered HTML template for the books page.
    """
    display_single: bool = False
    authors = []
    favorites = ()

    if not book_id:
        books: List[Book] = Book.get_books()
    else:
        books: List[Book] = Book.get_books(True, book_id)
        favorites: Tuple = Favorite.get_favorites('book', book_id)
        authors: List[Author] = Author.get_authors()
        display_single = True

    return render_template('books.html', books=books, display_single=display_single, authors=authors, favorites=favorites)


@app.route('/create_book', methods=['POST'])
def create_book() -> Response:
    """Creates a book in the database and redirects to that book's page."""
    book_data = request.form
    book_id: int = Book.create_book(book_data)

    return redirect(url_for('books', book_id=book_id))


@app.route('/books/add_favorite', methods=['POST'])
def add_favorite_author():
    """Adds an author that favorited the book."""
    favorite_data = request.form
    book_id: int = int(favorite_data['book_id'])
    Favorite.add_favorite(favorite_data)

    return redirect(url_for('books', book_id=book_id))
