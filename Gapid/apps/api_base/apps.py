from django.apps import AppConfig


class ApiBaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.api_base'
