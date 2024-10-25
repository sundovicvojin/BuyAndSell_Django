from django.apps import AppConfig


class ProdajaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'prodaja'

def ready(self):
    import prodaja.signals
