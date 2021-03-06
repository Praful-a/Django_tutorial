# Generated by Django 3.0.5 on 2020-05-11 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0003_auto_20200509_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['headline'],
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.RemoveField(
            model_name='book',
            name='Publisher',
        ),
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='store',
            name='books',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
        migrations.DeleteModel(
            name='Store',
        ),
        migrations.AddField(
            model_name='article',
            name='Publication',
            field=models.ManyToManyField(to='docs.Publication'),
        ),
    ]
