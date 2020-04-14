from django.shortcuts import render
from .models import Book

def home(request):
  context = {
    'books': Book.objects.all()
  }
  return render(request, 'home.html', context)

def detail(request, book_id):
  books = {
    'books': Book.objects.get(id=book_id)
  }
  return render(request, 'detail.html', books)

