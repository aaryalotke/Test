# Generated by Django 4.1.4 on 2022-12-10 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.TextField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phnno', models.TextField()),
                ('loanamount', models.BigIntegerField()),
                ('university', models.TextField()),
                ('course', models.TextField()),
                ('workexp', models.TextField()),
            ],
        ),
    ]
