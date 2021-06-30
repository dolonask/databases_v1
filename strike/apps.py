from django.apps import AppConfig


class StrikeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'strike'
    verbose_name = 'Приложение забастовка'
    verbose_name_plural = 'Приложения забастовки'
