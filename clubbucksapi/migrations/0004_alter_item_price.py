# Generated by Django 4.2.2 on 2023-06-15 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubbucksapi', '0003_remove_student_teacher_delete_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(),
        ),
    ]
