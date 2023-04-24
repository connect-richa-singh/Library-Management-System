from django.contrib import admin
from .models import Book
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display=['title','quantity','image','status']

admin.site.register(Book,BookAdmin)