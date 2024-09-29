# Generated by Django 4.2.15 on 2024-08-14 09:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app01", "0002_departments"),
    ]

    operations = [
        migrations.RenameField(
            model_name="userinfo",
            old_name="name",
            new_name="username",
        ),
        migrations.RemoveField(
            model_name="userinfo",
            name="age",
        ),
        migrations.AddField(
            model_name="userinfo",
            name="mobile",
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
    ]
