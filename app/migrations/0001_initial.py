# Generated by Django 4.2.14 on 2024-07-25 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('due_date', models.DateField()),
                ('difficulty', models.PositiveSmallIntegerField()),
                ('priority', models.IntegerField(default=0, editable=False)),
                ('finished', models.PositiveSmallIntegerField(default=False)),
            ],
        ),
    ]
