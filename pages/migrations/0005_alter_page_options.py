# Generated by Django 4.1 on 2022-09-07 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0004_alter_page_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="page",
            options={"ordering": ["-created"]},
        ),
    ]
