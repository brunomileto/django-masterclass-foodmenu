from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'foodmenu.users'

    def ready(self):
        import foodmenu.users.signals
