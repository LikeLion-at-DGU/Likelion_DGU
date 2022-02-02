# Generated by Django 3.2 on 2022-02-02 13:57

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
            name='Homework',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('contents', models.TextField()),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('contents', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('edit_date', models.DateTimeField(auto_now=True)),
                ('hw_id', models.ForeignKey(db_column='hw_id', on_delete=django.db.models.deletion.CASCADE, to='homework.homework')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]