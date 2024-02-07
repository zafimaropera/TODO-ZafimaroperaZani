# Généré par Django 4.1.3

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0002_delete_myprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ListeDeTaches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('statut', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='status', to='myapp.statut')),
            ],
        ),
    ]
