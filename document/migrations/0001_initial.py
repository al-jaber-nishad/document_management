# Generated by Django 4.2.4 on 2023-08-08 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('format', models.CharField(choices=[('pdf', 'PDF'), ('docx', 'DOCX'), ('txt', 'TXT')], max_length=10)),
                ('file', models.FileField(upload_to='documents/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_documents', to='authentication.customuser')),
                ('shared_with', models.ManyToManyField(blank=True, related_name='shared_documents', to='authentication.customuser')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
