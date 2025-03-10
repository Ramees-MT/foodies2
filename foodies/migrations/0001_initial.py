# Generated by Django 5.1.1 on 2024-10-28 05:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=50)),
                ('itemid', models.CharField(max_length=7)),
                ('userid', models.CharField(max_length=50)),
                ('quantity', models.CharField(max_length=50)),
                ('cart_status', models.IntegerField(default=1)),
                ('itemprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('itemimage', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Foodcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(max_length=50)),
                ('categoryimage', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Placeorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=50)),
                ('itemid', models.CharField(max_length=7)),
                ('userid', models.CharField(max_length=50)),
                ('quantity', models.CharField(max_length=50)),
                ('cart_status', models.IntegerField(default=1)),
                ('itemprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('itemimage', models.ImageField(upload_to='')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=50)),
                ('itemid', models.CharField(max_length=7)),
                ('username', models.CharField(max_length=50)),
                ('userid', models.CharField(max_length=50)),
                ('itemdescription', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Special_offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=50)),
                ('itemimage', models.ImageField(upload_to='')),
                ('offerdetails', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=50)),
                ('itemid', models.CharField(max_length=7)),
                ('userid', models.CharField(max_length=50)),
                ('quantity', models.CharField(max_length=50)),
                ('wishliststatus', models.CharField(max_length=50)),
                ('itemprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('itemimage', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Fooditems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=100)),
                ('itemprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('itemdescription', models.TextField()),
                ('itemimage', models.URLField()),
                ('itemcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodies.foodcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('userid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='foodies.login')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=30)),
                ('login_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='foodies.login')),
            ],
        ),
    ]
