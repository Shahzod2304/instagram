# Generated by Django 4.1.3 on 2022-11-10 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.PositiveIntegerField(max_length=12)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
