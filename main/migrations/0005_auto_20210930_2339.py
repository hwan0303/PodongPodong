# Generated by Django 2.2.20 on 2021-09-30 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_comment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]