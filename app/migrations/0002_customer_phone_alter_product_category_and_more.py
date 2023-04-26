# Generated by Django 4.1.7 on 2023-03-28 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(default='', max_length=13),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('breads', 'Bread'), ('cakes', 'Cake'), ('cupcakes', 'Cupcake'), ('cookies', 'Cookies'), ('dessert', 'Dessert'), ('doughnuts', 'Doughnut'), ('pastries', 'Pastries'), ('todayspecial', 'Featured'), ('specialoffer1', 'Specialoffer1'), ('specialoffer2', 'Specialoffer2'), ('specialoffer3', 'Specialoffer3')], max_length=15),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='productsimg'),
        ),
    ]
