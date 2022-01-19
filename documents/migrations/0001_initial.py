# Generated by Django 3.2 on 2021-05-16 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=150)),
                ('docs', models.FileField(upload_to='media/documents/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('expiry_date', models.DateTimeField(blank=True)),
                ('is_lock', models.BooleanField(blank=True, default=False, null=True)),
                ('is_private', models.BooleanField(blank=True, default=False, null=True)),
                ('uploader_name', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
