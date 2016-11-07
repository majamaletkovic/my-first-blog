from django.contrib import admin
# Register your models here.

from .models import Post


class PostAdmin(admin.ModelAdmin):
     list_display = ['author', 'title', 'subtitle', 'text', 'test_field', 'created_date', 'published_date']
admin.site.register(Post, PostAdmin)

