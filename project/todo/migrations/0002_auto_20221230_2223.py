from django.db import migrations, transaction


def add_users(apps, schema_editor):
    User = apps.get_model('todo', 'User')
    user_admin = User(username='admin', password='admin', is_superuser=True, is_staff=True)
    user_bobby = User(username='bobby', password='tables', is_superuser=False)
    user_chuck = User(username='chuck', password='norris', is_superuser=False)

    users = [user_admin, user_bobby, user_chuck]

    for user in users:
        with transaction.atomic():
            user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_users)
    ]