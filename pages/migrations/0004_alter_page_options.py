# Generated by Django 4.1 on 2022-09-07 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0003_page_author"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="page",
            options={"ordering": ["created"]},
        ),
    ]