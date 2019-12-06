# Generated by Django 3.0 on 2019-12-05 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaga',
            name='escolaridade_minima',
            field=models.CharField(choices=[('EF', 'Ensino Fundamental'), ('EM', 'Ensino Fundamental'), ('TC', 'Ensino Fundamental'), ('ES', 'Ensino Fundamental'), ('PM', 'Ensino Fundamental'), ('DR', 'Ensino Fundamental')], default='EF', max_length=2),
        ),
        migrations.AddField(
            model_name='vaga',
            name='faixa_salarial',
            field=models.IntegerField(choices=[(1, 'ate 1.000'), (2, 'de 1.000 a 2.000'), (3, 'de 2.000 a 3.000'), (4, 'acima de 3.000')], default=1),
        ),
        migrations.AddField(
            model_name='vaga',
            name='requisitos',
            field=models.TextField(null=True),
        ),
    ]
