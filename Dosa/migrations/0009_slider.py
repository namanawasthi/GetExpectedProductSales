# Generated by Django 2.2.11 on 2020-06-28 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dosa', '0008_auto_20200628_1833'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='slider/')),
            ],
        ),
    ]