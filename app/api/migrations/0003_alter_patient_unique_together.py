# Generated by Django 4.0.3 on 2022-04-01 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_patient_email_alter_patient_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='patient',
            unique_together={('email', 'name')},
        ),
    ]
