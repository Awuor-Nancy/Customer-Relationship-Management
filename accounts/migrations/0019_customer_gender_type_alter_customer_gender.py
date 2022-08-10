# Generated by Django 4.1 on 2022-08-10 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_customer_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='gender_type',
            field=models.CharField(choices=[('female', 'female'), ('male', 'male')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
