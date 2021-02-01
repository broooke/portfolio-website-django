# Generated by Django 3.1.5 on 2021-02-01 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=300, null=True)),
                ('sub_headline', models.CharField(max_length=500, null=True)),
                ('picture', models.ImageField(default='default.png', null=True, upload_to='images')),
                ('tags', models.ManyToManyField(blank=True, null=True, to='base.Tag')),
            ],
        ),
    ]
