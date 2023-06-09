# Generated by Django 3.1.14 on 2023-07-04 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('telefono', models.CharField(max_length=11)),
                ('mail', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Producto_Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('rut', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=40)),
                ('telefono', models.CharField(max_length=11)),
                ('mail', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('rut', models.CharField(max_length=10)),
                ('especialidad', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=11)),
                ('id_proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('1', 'pendiente'), ('2', 'finalizado'), ('3', 'desestimado')], default='1', max_length=3)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.cliente')),
                ('id_prod_serv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.producto_servicio')),
                ('id_proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Protocolo_Mant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion_prot', models.TextField(max_length=300)),
                ('id_tecnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.tecnico')),
            ],
        ),
    ]
