from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from .models import Author

class BookNameFilter(SimpleListFilter):
    title = 'book name'
    parameter_name = 'book_name'

    def lookups(self, request, model_admin):
        books = set()
        for author in Author.objects.all():
            books.update([(book.name, book.name) for book in author.books.all()])
        return sorted(books)

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(books__name=self.value())

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Changable information', {
            'fields': ('name', 'surname', 'patronymic', 'bio')
        }),
        ('Static information', {
            'fields': ('birth_date', 'created_at', 'updated_at')
        }),
    )

    readonly_fields = ('created_at', 'updated_at')
    list_display = ('name', 'surname', 'patronymic', 'get_books')
    list_filter = ('name', 'surname', 'patronymic', BookNameFilter)

    def get_books(self, obj):
        return ", ".join([book.name for book in obj.books.all()])
    get_books.short_description = 'Books'

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('bio',)
        return self.readonly_fields