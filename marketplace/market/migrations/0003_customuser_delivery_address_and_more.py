# Generated by Django 5.0.4 on 2024-04-29 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_alter_customuser_options_customuser_contact_info_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='delivery_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='company_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
