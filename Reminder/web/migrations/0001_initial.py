# Generated by Django 3.2.15 on 2022-09-16 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, max_length=100, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('logo', models.URLField(verbose_name='Logo')),
                ('treshold', models.PositiveIntegerField(blank=True, verbose_name='Treshold')),
                ('Repeat_all_Day', models.BooleanField(default=False)),
                ('disabled', models.BooleanField(default=False)),
                ('Repeat', models.PositiveIntegerField(blank=True, default=0, verbose_name="Repaet('Day')")),
                ('Upcoming_DateTime', models.DateTimeField(verbose_name='Upcoming_DateTime')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created_Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
            ],
        ),
    ]