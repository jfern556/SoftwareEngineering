# Generated by Django 2.0.5 on 2018-07-01 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saved_for_later_content',
            name='Saved_ContentID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
