# Generated by Django 3.1.4 on 2021-02-02 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='punt_carb',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='punt_prote',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='punt_veg',
        ),
        migrations.AddField(
            model_name='photo',
            name='carbohidratos',
            field=models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='proteinas',
            field=models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='vegetales',
            field=models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0, null=True),
        ),
    ]
