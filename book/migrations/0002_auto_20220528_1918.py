# Generated by Django 3.2 on 2022-05-29 00:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('author', '0001_initial'),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rack',
            name='number',
        ),
        migrations.RemoveField(
            model_name='rack',
            name='status',
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='sujeto',
            field=models.CharField(max_length=180, null=True),
        ),
        migrations.AddField(
            model_name='rack',
            name='is_rent',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='rack',
            name='is_reserve',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rack',
            name='rack',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='rack',
            name='recerve',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recerve', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rack',
            name='rent',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='author.author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='rack',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('89a6fd7a-538b-40d5-82d1-c4f82dcd3351')),
        ),
    ]