# Generated by Django 4.0.3 on 2022-03-03 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_comments_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile'),
        ),
    ]
