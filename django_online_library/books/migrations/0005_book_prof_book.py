# Generated by Django 4.0.2 on 2022-02-21 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='prof_book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='books.profile'),
            preserve_default=False,
        ),
    ]