# Generated by Django 4.0.6 on 2022-07-07 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Help',
            fields=[
                ('help_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('help_question', models.TextField()),
                ('help_answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('status_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('status_title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tesk',
            fields=[
                ('tsk_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tsk_title', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='TypeCom',
            fields=[
                ('typecom_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('typecom_title', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='TypePro',
            fields=[
                ('typepro_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('type_title', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='TypeSer',
            fields=[
                ('typeser_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('typeser_title', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='TypeUser',
            fields=[
                ('typeuser_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('typeuser_title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WstUser',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=30)),
                ('user_pass', models.CharField(max_length=30)),
                ('validate', models.CharField(max_length=30)),
                ('typeuser_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.typeuser')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('serv_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('serv_name', models.CharField(max_length=70)),
                ('serv_details', models.TextField()),
                ('serv_price', models.IntegerField()),
                ('serv_created_date', models.DateField(auto_now_add=True)),
                ('serv_status', models.BooleanField()),
                ('typeser_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.typeser')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.wstuser')),
            ],
        ),
        migrations.CreateModel(
            name='Proces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_created_date', models.DateField(auto_now_add=True)),
                ('pro_amount', models.IntegerField()),
                ('bal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.typepro')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('not_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('not_title', models.CharField(max_length=70)),
                ('not_content', models.TextField()),
                ('not_created_date', models.DateField(auto_now_add=True)),
                ('tsk_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.tesk')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('img_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('img_link', models.TextField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.wstuser')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('eval_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('eval_star_number', models.IntegerField()),
                ('eval_comment', models.TextField()),
                ('eval_created_date', models.DateField(auto_now_add=True)),
                ('serv_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.service')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.wstuser')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('con_created_date', models.DateField(auto_created=True)),
                ('con_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('con_title', models.CharField(max_length=70)),
                ('con_details', models.TextField()),
                ('con_price', models.IntegerField()),
                ('con_attachements', models.TextField()),
                ('serv_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.service')),
                ('status_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.status')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.wstuser')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('com_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('com_title', models.CharField(max_length=70)),
                ('com_details', models.TextField()),
                ('com_image', models.TextField()),
                ('com_created_date', models.DateField(auto_now_add=True)),
                ('typecom_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.typecom')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.wstuser')),
            ],
        ),
        migrations.CreateModel(
            name='BankAcount',
            fields=[
                ('bank_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('bank_name', models.CharField(max_length=100)),
                ('bank_acount_number', models.IntegerField()),
                ('acount_iban', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.wstuser')),
            ],
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('bal_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('bal_amount', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_app.wstuser')),
            ],
        ),
    ]