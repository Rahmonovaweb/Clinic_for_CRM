# Generated by Django 5.0.2 on 2024-03-03 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.IntegerField(choices=[(1, 'comment'), (2, 'complain'), (3, 'suggest')], default=1),
        ),
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.IntegerField(choices=[(1, 'doctor'), (2, 'manager'), (3, 'admin'), (4, 'nurse'), (5, 'director'), (6, 'cooker')]),
        ),
    ]
