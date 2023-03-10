from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ("title", "slug", "author","created","update")
    prepopulated_fields = {"slug":("title",)}