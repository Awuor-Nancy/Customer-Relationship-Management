# Generated by Django 4.1 on 2022-08-09 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_product_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(blank=b'I00\n', to='accounts.tag'),
        ),
    ]
