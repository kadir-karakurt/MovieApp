from django.contrib import admin
from .models import Category,Movie

class MovieAdmin(admin.ModelAdmin): # movie modeli için yönetici admin sınıfı
    list_display = ("film_name", "description", "boolean",) #sütun bilgisini görmemizi sağlar. 
    list_display_links = ("film_name","description",) #sütunların tıklanabilir olmasını sağlar.
    search_fields = ("film_name",) # arama kutusu ile arama yapmamızı sağlar.


admin.site.register(Category)
admin.site.register(Movie, MovieAdmin)




