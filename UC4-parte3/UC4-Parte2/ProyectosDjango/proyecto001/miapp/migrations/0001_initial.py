# Generated by Django 4.2.7 on 2023-12-11 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('idcourse', models.BigAutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=30)),
                ('hour', models.PositiveSmallIntegerField()),
                ('credits', models.PositiveSmallIntegerField()),
                ('state', models.CharField(max_length=1)),
            ],
        ),
    ]
