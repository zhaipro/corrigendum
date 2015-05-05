from django.contrib import admin
from .models import Corrigendum, Book, Publisher, Author


# Register your models here.
admin.site.register(Book)
admin.site.register(Corrigendum)
admin.site.register(Publisher)
admin.site.register(Author)
