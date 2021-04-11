# Generated by Django 3.1.7 on 2021-04-06 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoAnalysis',
            fields=[
                ('photo_id', models.AutoField(primary_key=True, serialize=False)),
                ('line_id', models.CharField(max_length=120)),
                ('date', models.DateTimeField()),
                ('pic', models.ImageField(upload_to='images')),
            ],
        ),
    ]