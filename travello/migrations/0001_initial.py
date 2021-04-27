# Generated by Django 2.1.15 on 2021-04-27 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='auction_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auction_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('username', models.CharField(max_length=30)),
                ('auction_value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='auctiondetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('product_specifications', models.TextField()),
                ('current_bid', models.IntegerField()),
                ('closing_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='productdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_no', models.IntegerField()),
                ('email', models.CharField(max_length=30)),
            ],
        ),
    ]
