# Generated by Django 3.0.5 on 2020-06-09 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destinations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=100)),
                ('imgs', models.ImageField(upload_to='pics')),
                ('descs', models.TextField()),
                ('prices', models.IntegerField()),
                ('offers', models.BooleanField(default=False)),
            ],
        ),
    ]
