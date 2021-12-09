from django.contrib import admin
from blog.models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author",  "category", "photo", "created_at", "updated_at")
    list_display_links = ("id", "title")
    search_fields = ("title", "content")
    list_filter = ("category",)
    fields = ("author", "title", "category", "content", "photo", "created_at", "updated_at")
    readonly_fields = ( "created_at", "updated_at")





class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    search_fields = ("title",)

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
