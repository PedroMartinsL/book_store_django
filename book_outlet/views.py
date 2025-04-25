from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.db.models import Avg

# Create your views here.
from.models import Book

def index(request):
    books = Book.objects.all().order_by("-title")
    num_books = books.count()
    avg_rating = books.aggregate(Avg('rating'))['rating__avg']
    return render(request, 'book_outlet/index.html',
                  {'books': books,
                   'total_number_of_books': num_books,
                   'avarage_rating': avg_rating,
                   })

def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(id=book_id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_outlet/book_detail.html',
                  {'book': book})#can use pk too