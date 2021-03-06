# Generated by Django 3.0.3 on 2020-02-17 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(blank=True, max_length=100, null=True, verbose_name='product name')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='price')),
                ('stocks', models.IntegerField(blank=True, null=True, verbose_name='quantity')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='product image')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
            ],
        ),
    ]
