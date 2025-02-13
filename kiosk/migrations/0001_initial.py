# Generated by Django 5.1.6 on 2025-02-13 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_datetime', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.IntegerField()),
                ('earned_points', models.IntegerField()),
                ('store', models.CharField(choices=[('A', 'Store A'), ('B', 'Store B')], max_length=50)),
            ],
        ),
    ]
