# Generated by Django 4.1.1 on 2022-10-26 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_models', '0002_categoriaproducto_alter_contact_sexo_infoproducto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriaproducto',
            name='categoria',
            field=models.CharField(max_length=40),
        ),
    ]
