# Generated by Django 4.2.2 on 2023-06-16 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubbucksapi', '0004_alter_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='total_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='transactionitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
