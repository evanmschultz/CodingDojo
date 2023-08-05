from flask_app import app
from flask import redirect, render_template, request, url_for
from flask_app.models.author import Author
from flask_app.models.book import Book

# Type hinting imports
from typing import Dict, List
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
    Gets all the authors and displays them on the page.

    If there is an id the page only displays that author.
    """
    display_single: bool = False
    books = []

    if not author_id:
        authors: List[Author] = Author.get_authors()
    else:
        authors: List[Author] = Author.get_authors(True, author_id)
        display_single = True

        books: List[Book] = Book.get_books()

    return render_template('authors.html', authors=authors, display_single=display_single, books=books)


@app.route('/create_author', methods=['POST'])
def create_author() -> Response:

    author_data = request.form
    author_id: int = Author.create_author(author_data)

    return redirect(url_for('authors', author_id=author_id))
