from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_on')
    list_filter = ('status')
    search_fields = ['title', 'content']



# Register your models here.
admin.site.register(Post)
