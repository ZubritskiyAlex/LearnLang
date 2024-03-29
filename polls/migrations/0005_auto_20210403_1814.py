# Generated by Django 3.1.7 on 2021-04-03 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20210403_1811'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='theme',
            new_name='question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='description',
        ),
        migrations.AddField(
            model_name='test',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='test',
            name='theme',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
