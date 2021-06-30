from django.apps import AppConfig


class MigrantConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'migrant'
    verbose_name = 'Приложение мигрант'
    verbose_name_plural = 'Приложения мигранты'
