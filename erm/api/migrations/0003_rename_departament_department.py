# Generated by Django 3.2.12 on 2022-03-29 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_employee_birth_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Departament',
            new_name='Department',
        ),
    ]
