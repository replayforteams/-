# Generated by Django 4.1.7 on 2023-03-06 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BookInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "bname",
                    models.CharField(max_length=128, unique=True, verbose_name="书名"),
                ),
                ("bpubdate", models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="HeroInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("hname", models.CharField(max_length=128, verbose_name="人物名字")),
                ("hgender", models.BooleanField(verbose_name="性别")),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="book.bookinfo"
                    ),
                ),
            ],
        ),
    ]
