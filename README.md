# websocketJP Real chat app
 
1. env 
2. Django
3. settings
4. app
5. channels

a.1. application account - Set up user register, user model

b.1. Create chat application
    2. create consumer,
    3. routing 
    4. models -  user messages.

c. application asgi
    1.ASGI_APPLICATION = 'settings.asgi.application'
    2. asgi inside:
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
            to check asgi or wsgi
            pip install daphne
            daphne -b 0.0.0.0 -p 8000 settings.wsgi:application


d) 1. adding javascript 
    2. to send data with fetch 

a) add channels to INTALLED_APPS
b) create asgi application ASGI_APPLICATION = 'settings.routing.application'
c) add channels layer 
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}

d) add routing to settings
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
ws_pattern =[
    path('ws/tabledata/',)
]

application = ProtocolTypeRouter(
    {
        'websocket':AuthMiddlewareStack(URLRouter(ws_pattern))
    }
)

c) add consumer to your app



to check asgi or wsgi
pip install daphne
daphne -b 0.0.0.0 -p 8000 settings.wsgi:application