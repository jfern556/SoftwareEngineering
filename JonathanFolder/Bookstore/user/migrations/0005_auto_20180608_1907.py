# Generated by Django 2.0.5 on 2018-06-08 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_book_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='book_rating',
            name='BOOK_RATING_ID',
        ),
        migrations.AddField(
            model_name='book',
            name='Title',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='book_rating',
            name='Book_rating_id',
            field=models.IntegerField(default=600, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='Book_description',
            field=models.CharField(max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='Copies_sold',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='CoverImage',
            field=models.ImageField(default='book_images/noImage.png', upload_to='book_images/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='Price',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='Release_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='UseNickname',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='credit_card',
            name='C_card_number',
            field=models.CharField(max_length=24, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reserved_credit_card',
            name='RCC_ID',
            field=models.CharField(max_length=24, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='Email',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
