from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from .models import Book

class AuthorFilter(SimpleListFilter):
    title = 'Author'
    parameter_name = 'author'

    def lookups(self, request, model_admin):
        authors = set()
        for book in Book.objects.all():
            authors.update([author.name for author in book.author.all()])
        return [(author, author) for author in authors]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(author__name=self.value())

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Static information', {
            'fields': ('name', 'get_authors', 'publication_year',)
        }),
        ('Changeable information', {
            'fields': ('created_at', 'updated_at', 'issue_date')
        }),
        ('Additional information', {
            'fields': ('description', 'count',)
        }),
    )

    readonly_fields = ('name', 'description', 'created_at', 'updated_at', 'get_authors')
    list_display = ('id', 'name', 'description', 'count', 'get_authors', 'created_at', 'updated_at')
    list_filter = ('id', 'name', AuthorFilter, 'count', 'publication_year')

    def get_authors(self, obj):
        return ", ".join([author.name for author in obj.author.all()])
    get_authors.short_description = 'Author'

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('publication_year',)
        return self.readonly_fields