# Generated by Django 3.1 on 2021-02-25 12:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_auto_20210225_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='post_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
