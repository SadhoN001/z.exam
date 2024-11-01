
from django.shortcuts import render
from django.db.models import Q
from .models import Book

def search_books(request):
    query = request.GET.get('q')
    books = Book.objects.filter(Q(title__icontains=query)) if query else []
    return render(request, 'library/index.html', {'books': books, 'query': query})

