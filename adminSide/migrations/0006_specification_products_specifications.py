# Generated by Django 4.2.1 on 2023-08-10 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminSide', '0005_alter_products_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='specifications',
            field=models.ManyToManyField(to='adminSide.specification'),
        ),
    ]
