# Generated by Django 3.2 on 2021-04-28 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='date_added',
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
