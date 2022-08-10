# Generated by Django 4.1 on 2022-08-09 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_order_product_alter_customer_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('out of delivery', 'out of delivery'), ('delivered', 'delivered')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='tag',
            field=models.ManyToManyField(to='accounts.tag'),
        ),
    ]