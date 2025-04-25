from django.http import Http404
from django.shortcuts import get_object_or_404, render

# Create your views here.
from.models import Book

def index(request):
    books = Book.objects.all()
    return render(request, 'book_outlet/index.html',
                  {'books': books})

def book_detail(request, book_id):
    # try:
    #     book = Book.objects.get(id=book_id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_outlet/book_detail.html',
                  {'book': book})#can use pk too