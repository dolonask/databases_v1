from django.contrib.auth.models import User
def load_mains(apps, schema_editor):
    Role = apps.get_model("main", "Role")
    role = Role(id=1, name='Admin')
    role.save()
    role = Role(id=2, name='Country Admin')
    role.save()
    role = Role(id=3, name='Monitor')
    role.save()
    User.objects.create_superuser('admin', 'x@x.com', 'admin')
    Position = apps.get_model("main", 'Position')
    position = Position(user_id=1, role_id=1)
    position.save()