# Generated by Django 5.0.2 on 2024-02-23 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fresh_tohome', '0003_add_farmers'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_products',
            name='product_image',
            field=models.ImageField(null=True, upload_to='product_images/'),
        ),
    ]
