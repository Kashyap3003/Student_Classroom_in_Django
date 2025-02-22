# Generated by Django 4.1.5 on 2023-03-14 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assignment', '0002_alter_assignment_deadline'),
        ('classes', '0002_persons'),
        ('users', '0004_alter_users_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('submission_id', models.AutoField(primary_key=True, serialize=False)),
                ('submission_date', models.DateField()),
                ('work', models.FileField(upload_to='submissions/')),
                ('marks_obtained', models.IntegerField(null=True)),
                ('assignment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.assignment')),
                ('classroom_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.classrooms')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
            options={
                'db_table': 'submissions',
            },
        ),
    ]
