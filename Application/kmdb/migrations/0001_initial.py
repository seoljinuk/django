# Generated by Django 5.1 on 2024-08-08 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('moviecd', models.BigIntegerField(primary_key=True, serialize=False)),
                ('movienm', models.CharField(blank=True, max_length=255, null=True)),
                ('movienmen', models.CharField(blank=True, max_length=255, null=True)),
                ('prdtyear', models.IntegerField(blank=True, null=True)),
                ('opendt', models.BigIntegerField(blank=True, null=True)),
                ('typenm', models.CharField(blank=True, max_length=255, null=True)),
                ('prdtstatnm', models.CharField(blank=True, max_length=255, null=True)),
                ('nationalt', models.CharField(blank=True, max_length=255, null=True)),
                ('genrealt', models.CharField(blank=True, max_length=255, null=True)),
                ('repnationnm', models.CharField(blank=True, max_length=255, null=True)),
                ('repgenrenm', models.CharField(blank=True, max_length=255, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('year_momth', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movies',
            },
        ),
    ]
