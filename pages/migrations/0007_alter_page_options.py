# Generated by Django 4.1 on 2022-09-07 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0006_alter_page_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="page",
            options={"ordering": ["-created"]},
        ),
    ]