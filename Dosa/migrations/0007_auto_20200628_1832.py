# Generated by Django 2.2.11 on 2020-06-28 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dosa', '0006_auto_20200628_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='youtube_link',
            field=models.TextField(null=True),
        ),
    ]