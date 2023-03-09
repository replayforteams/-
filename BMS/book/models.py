from django.db import models


# Create your models here.
class BookInfo(models.Model):
    bname = models.CharField(max_length=128, unique=True, verbose_name='书名')
    bpubdate = models.DateTimeField(null=True, verbose_name='发布日期')

    def __str__(self):
        return self.bname


class HeroInfo(models.Model):
    hname = models.CharField(max_length=128, verbose_name='人物名字')
    hgender = models.BooleanField(verbose_name='性别')
    # 外键约束
    book = models.ForeignKey(to=BookInfo, on_delete=models.CASCADE, verbose_name='所属书籍')

    def __str__(self):
        return self.hname
