from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'book_name', 'created_at', 'planed_end_at', 'end_at')
    list_filter = ('user__first_name', 'book__name', 'created_at', 'planed_end_at', 'end_at')

    def user_name(self, obj):
        return obj.user.first_name
    user_name.short_description = 'User Name'

    def book_name(self, obj):
        return obj.book.name
    book_name.short_description = 'Book Name'
