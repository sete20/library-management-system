# Generated by Django 4.0.5 on 2022-06-15 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0003_book_active_book_pagescount_book_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='books',
        ),
        migrations.RemoveField(
            model_name='user',
            name='books',
        ),
    ]