# Generated by Django 4.1.1 on 2022-09-06 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('admin', 'Администратор'), ('moderator', 'Модератор'), ('member', 'Пользователь')], default='member', max_length=9)),
                ('age', models.PositiveSmallIntegerField()),
                ('locations', models.ManyToManyField(related_name='user', to='ads.location')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['username'],
            },
        ),
    ]
