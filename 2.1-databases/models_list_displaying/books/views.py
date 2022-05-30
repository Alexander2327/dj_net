from django.shortcuts import render, redirect

from books.models import Book
from django.core.paginator import Paginator


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, template, context)


def book_view(request, date):
    template = 'books/books_list.html'
    books = Book.objects.filter(pub_date=date).all()

    paginator = Paginator(books, 10)
    page_date = request.GET.get('date')
    page = paginator.get_page(page_date)

    context = {
        'books': books,
        'page': page,
    }
    return render(request, template, context)
