from rest_framework import viewsets
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .serializers import *
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser

@permission_classes([IsAdminUser])
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

def author_list(request):
    authors = list(Author.objects.all())
    author_books = [author.books.all() for author in authors]
    book_names = []
    for queryset in author_books:
        book_sting = ""
        for book in queryset:
            book_sting += book.name + "  "
        book_names.append(book_sting)
    zipped_data = list(zip(authors, book_names))
    return render(request, 'author_list.html', {'authors': zipped_data, "authors_active":"active"})


def author_create(request):
    if request.method == 'POST':
        form = CreateAuthorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            patronymic = form.cleaned_data['patronymic']
            author = Author(name=name, surname=surname, patronymic=patronymic)
            author.save()
            return redirect('author_list')
    else:
        form = CreateAuthorForm()

    return render(request, 'author_create.html', {'form': form})


def author_delete(request, author_id):
    author = Author.objects.get(id=author_id)
    if not author.books.exists():
        author.delete()
    return redirect('author_list')
