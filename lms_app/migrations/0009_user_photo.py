# Generated by Django 4.0.5 on 2022-06-16 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0008_book_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(default=1, upload_to='photos/%y/%m/%d'),
            preserve_default=False,
        ),
    ]
