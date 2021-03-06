from django.db import models
from django.urls import reverse
from django.conf import settings




# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="Наименование")
    content = models.TextField(verbose_name="Контент")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=" Дата публикации")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    photo = models.ImageField(verbose_name="Фото", blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT,  verbose_name="Категория")

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-created_at"]


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Наименование категории")

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["title"]
