# Generated by Django 4.2.6 on 2023-11-02 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmakesapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='people',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
    ]
