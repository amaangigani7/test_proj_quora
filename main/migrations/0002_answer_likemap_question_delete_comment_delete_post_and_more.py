# Generated by Django 4.2.4 on 2023-08-05 06:47

from django.db import migrations, models, transaction
import django.db.models.deletion
from django.contrib.auth.models import User



def add_users(apps, schema_editor):
    super_user = User.objects.create(username="super_user", is_staff=True, is_superuser=True)
    super_user.set_password('super_pass1')
    super_user.save()
    user2 = User.objects.create(username="test_user2")
    user2.set_password('password2')
    user2.save()
    user3 = User.objects.create(username="test_user3", password="password3")
    user3.set_password('password3')
    user3.save()

def add_posts(apps, schema_editor):
    Question = apps.get_model("main", "Question")
    Answer = apps.get_model("main", "Answer")
    Question.objects.create(user='test_user2', title="This is the first Question", content="This is the content of the first question")
    Question.objects.create(user='test_user3', title="This is the second Question", content="This is the content of the second question")



class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(null=True, unique=True)),
                ('user', models.CharField(default='test', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LikeMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True, unique=True)),
                ('content', models.TextField(null=True, unique=True)),
                ('user', models.CharField(default='test', max_length=100)),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='likemap',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.question'),
        ),
        migrations.RunPython(add_users),
        migrations.RunPython(add_posts),
    ]
