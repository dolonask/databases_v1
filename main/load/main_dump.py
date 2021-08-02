def load_mains(apps, schema_editor):
    Role = apps.get_model("main", "Role")
    role = Role(id=1, name='Admin')
    role.save()
    role = Role(id=2, name='Country Admin')
    role.save()
    role = Role(id=3, name='Monitor')
    role.save()

