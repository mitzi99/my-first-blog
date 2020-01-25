# Generated by Django 2.2.9 on 2020-01-25 04:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marcador', '0002_auto_20200125_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookmarks', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
    ]
