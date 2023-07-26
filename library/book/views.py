from . import models
from order.models import Order
from author.models import Author
from django.shortcuts import render, redirect
from django.http import HttpResponse

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from .models import Book
from rest_framework import viewsets
from .serializers import *

@permission_classes([IsAdminUser])
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def index_book(request):
    if not request.user.is_authenticated:
        return HttpResponse("<h1>You need to login first</h1>")
    books = list(models.Book.objects.all())
    book_authors = [book.author.all() for book in books]
    author_names = []
    for query_author in book_authors:
        author_arr = [f"{author.name} {author.surname[0]}. {author.patronymic[0]}." for author in query_author]
        author_names.append(", ".join(author_arr))
    zipped_data = list(zip(books, author_names))
        
    context = {"action": "All books:", 
               "books": zipped_data, 
               "role": request.user.role, 
               "books_active": "active"}
    return render(request, "index_book.html", context = context)
    
def book_by_id(request, book_id):
    if not request.user.is_authenticated:
        return HttpResponse("<h1>You need to login first</h1>")
    book = models.Book.objects.get(id=book_id)
    authors = Author.objects.filter(books=book_id)
    author_names = [f"{author.name} {author.surname} {author.patronymic} " for author in authors]
    author_string = ", ".join(author_names)
    context = {"book_id": book_id,
               "book": book, 
               "author": author_string, 
               "page_name": "Book by id", 
               "role": request.user.role, 
               "books_active": "active"}
    return render(request, "book_by_id.html", context=context)
    
def filter_by(request):
    if not request.user.is_authenticated:
        return HttpResponse("<h1>You need to login first</h1>")
    raw_filter = request.GET.get('filter')
    all_filters = raw_filter.split(" ")
    filters_dict={filter.split(":")[0]:filter.split(":")[1] for filter in all_filters}
    books = models.Book.objects.filter(**filters_dict)
    book_authors = [book.author.all() for book in books]
    author_names = []
    for query_author in book_authors:
        author_arr = [f"{author.name} {author.surname[0]}. {author.patronymic[0]}." for author in query_author]
        author_names.append(", ".join(author_arr))
    zipped_data = list(zip(books, author_names))
    context = {"action": f"Filter by {raw_filter}", 
               "books": zipped_data,  
               "role": request.user.role,
               "books_active": "active"}
    return render(request, "index_book.html", context=context)

def provided_to(request):
    if not request.user.is_authenticated:
        return HttpResponse("<h1>You need to login first</h1>")
    if request.user.role != 1:
        return HttpResponse("<h1>Only admins allowed</h1>")
    user_id = request.GET.get('user_id')
    orders_with_user_id = Order.objects.filter(user_id = user_id)
    book_ids = [order.book.id for order in orders_with_user_id]
    books = [models.Book.objects.filter(id=id).first() for id in book_ids]
    context = {"action": f"Info about books provided to user with id: {user_id}", 
               "books": books, 
               "books_active": "active"}
    return render(request, "provided_to_user.html", context=context)

def create_book(request):
    if not request.user.is_authenticated:
        return HttpResponse("<h1>You need to login first</h1>")
    if request.user.role != 1:
        return HttpResponse("<h1>Only admins allowed</h1>")
    context = {"authors": Author.objects.all(), 
               "books_active": "active"}
    return render(request, 'create_book.html', context=context)

def create_book_in_db(request):
    if not request.user.is_authenticated:
        return HttpResponse("<h1>You need to login first</h1>")
    if request.user.role != 1:
        return HttpResponse("<h1>Only admins allowed</h1>")
    book_name = request.POST['book_name']
    book_description = request.POST['book_description']
    book_count = request.POST['book_count']
    author_id = request.POST['author']
    author = Author.objects.filter(id=author_id)
    models.Book.create(book_name, book_description, book_count, author=author)
    return redirect("index_books")

def delete_book(request, book_id):
    if not request.user.is_authenticated:
        return HttpResponse("<h1>You need to login first</h1>")
    if request.user.role != 1:
        return HttpResponse("<h1>Only admins allowed</h1>")
    models.Book.delete_by_id(book_id)
    return redirect("index_books")