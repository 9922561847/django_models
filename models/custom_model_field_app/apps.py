from django.apps import AppConfig


class CustomModelFieldAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_model_field_app'
