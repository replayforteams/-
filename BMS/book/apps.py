from django.apps import AppConfig


# class BookConfig(AppConfig):
#     default_auto_field = "django.db.models.BigAutoField"
#     name = "book"
class BookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book'
    verbose_name = '图书管理'
