# Generated by Django 4.0.1 on 2022-03-12 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Flower_name', models.CharField(max_length=50)),
                ('Introduction', models.TextField()),
                ('Etymology', models.TextField()),
                ('Evolution', models.TextField()),
                ('Species', models.TextField()),
                ('Tax_domain', models.CharField(max_length=50)),
                ('Tax_kingdom', models.CharField(max_length=50)),
                ('Tax_phylum', models.CharField(max_length=50)),
                ('Tax_order', models.CharField(max_length=50)),
                ('Tax_family', models.CharField(max_length=50)),
                ('Tax_genus', models.CharField(max_length=50)),
                ('Ornamental_plants', models.TextField()),
                ('Cut_flowers', models.TextField()),
                ('Medicinal_uses', models.TextField()),
                ('Health_benefit', models.TextField()),
                ('Perfumes_food', models.TextField()),
                ('Symbolizes', models.TextField()),
                ('Season_to_grow', models.TextField()),
                ('Img', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='predict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Flower_name', models.CharField(max_length=50)),
                ('Img_pre', models.ImageField(blank=True, null=True, upload_to='pre/')),
            ],
        ),
    ]
