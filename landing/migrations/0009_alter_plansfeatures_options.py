# Generated by Django 5.0.4 on 2024-04-17 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0008_delete_plans_alter_plansfeatures_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plansfeatures',
            options={'managed': True},
        ),
    ]