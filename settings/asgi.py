"""
ASGI config for settings project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os


from channels.routing import ProtocolTypeRouter,URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack



from chat import routing

 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')
django_asgi_application = get_asgi_application()
application = ProtocolTypeRouter({
    'http': django_asgi_application,
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                routing.websocket_urlpatterns
            )
        )
    ),
})

# application = get_asgi_application()
