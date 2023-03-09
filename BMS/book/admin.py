from django.contrib import admin

# Register your models here.
from django.contrib import admin

from book.models import BookInfo, HeroInfo
# Register your models here.
# 注册书籍模型类
admin.site.register(BookInfo)
# 注册人物模型类
admin.site.register(HeroInfo)
