# Generated by Django 4.2.7 on 2023-12-02 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=4)),
                ('short', models.CharField(max_length=4)),
            ],
        ),
        migrations.DeleteModel(
            name='FormSubmission',
        ),
    ]