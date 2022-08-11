# Generated by Django 3.2.15 on 2022-08-11 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('e_category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('price', models.BigIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_category.category')),
                ('created_by', models.ForeignKey(db_column='created_by', editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_create_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(db_column='updated_by', editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_update_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'e_products',
                'ordering': ['-id'],
                'abstract': False,
            },
        ),
    ]
