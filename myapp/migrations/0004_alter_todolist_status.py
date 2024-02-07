# Généré par Django 4.1.3

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ListeDeTaches',
            name='statut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='myapp.statut'),
        ),
    ]
