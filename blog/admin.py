from django.contrib import admin
from .models import Post, Freebie




# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'slug')
    list_filter = ('title', 'date')
    prepopulated_fields = {'slug': ('title', )}



class FreebieAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'slug')
    list_filter = ('title', 'date')
    prepopulated_fields = {'slug': ('title', )}
    



admin.site.register(Post, PostAdmin)
admin.site.register(Freebie, FreebieAdmin)


