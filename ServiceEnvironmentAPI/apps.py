import sys
from django.apps import AppConfig


class ServiceenvironmentapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ServiceEnvironmentAPI'

    def ready(self, *args, **kwargs):
        is_manage_py = any(arg.casefold().endswith("manage.py") for arg in sys.argv)
        is_runserver = any(arg.casefold() == "scrap" for arg in sys.argv)
        if (is_manage_py and is_runserver) or (not is_manage_py):
            from ServiceEnvironmentAPI.scrapping import get_data_scrapped
            get_data_scrapped()
