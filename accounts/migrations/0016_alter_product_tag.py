# Generated by Django 4.1 on 2022-08-10 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_alter_product_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(null=True, to='accounts.tag'),
        ),
    ]
