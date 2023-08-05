from flask_app import app
from flask import redirect, render_template, request, url_for
from flask_app.models.author import Author
from flask_app.models.book import Book
from flask_app.models.favorite import Favorite

from pprint import pprint

# Type hinting imports
from typing import Dict, List, Tuple
from werkzeug import Response


# Root Route
@app.route('/')
def index() -> Response:
    return redirect(url_for('authors'))


# Authors Route
@app.route('/authors', methods=['GET'])
@app.route('/authors/<int:author_id>', methods=['GET'])
def authors(author_id: int | None = None) -> str:
    """
    Gets author(s) and displays them on the page.

    If (author_id) is not provided, the page displays all authors.
    If an (author_id) is provided, the page only displays the author with that ID
    with a list of all the books they favorited as well as all the books in the 
    database so the user can have the author favorite any of those as well.

    Returns:
        str: The rendered HTML template for the authors page.
    """
    display_single: bool = False
    books = []
    favorites = ()

    if not author_id:
        authors: List[Author] = Author.get_authors()
    else:
        authors: List[Author] = Author.get_authors(True, author_id)
        books: List[Book] = Book.get_books()
        favorites: Tuple = Favorite.get_favorites('author', author_id)
        display_single = True

    return render_template('authors.html', authors=authors, display_single=display_single, books=books, favorites=favorites)


@app.route('/create_author', methods=['POST'])
def create_author() -> Response:
    """Creates an author in the database and redirects to that author's page."""
    author_data = request.form
    author_id: int = Author.create_author(author_data)

    return redirect(url_for('authors', author_id=author_id))


@app.route(rule='/authors/add_favorite', methods=['POST'])
def add_favorite_book():
    """Adds an book to the authors favorites."""
    favorite_data = request.form
    pprint(favorite_data)
    # author_id: int = int(favorite_data['author_id'])
    Favorite.add_favorite(favorite_data)

    return redirect(url_for('authors', author_id=2))
