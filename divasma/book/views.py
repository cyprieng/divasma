from django.http import Http404
from django.shortcuts import render, get_object_or_404
from divasma.book.models import Book, Genre
from divasma.author.models import Author

def book_view(request, id, slug):
    """Show the details of the book

    Keyword arguments:
    id -- id of the book
    slug -- slug of the book. Must be valid!
    """
    book = get_object_or_404(Book, id=id)

    # Check slug
    if book.slug != slug:
        raise Http404

    return render(request, "book/book.html", locals())
