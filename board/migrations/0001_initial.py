# Generated by Django 2.2.1 on 2019-05-15 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
                ('company', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=1000)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
