# Generated by Django 4.2.3 on 2023-07-24 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_statistic_total_client_alter_statistic_won_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='total_client',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='won',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='year',
            field=models.PositiveIntegerField(default=0),
        ),
    ]