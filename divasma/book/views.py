from django.shortcuts import render

def book_view(request, id, slug):
    book_name = 'Dune'

    return render(request, 'book/book.html', locals())
