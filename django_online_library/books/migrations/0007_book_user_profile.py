# Generated by Django 4.0.2 on 2022-02-21 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_remove_book_prof_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.profile'),
        ),
    ]
