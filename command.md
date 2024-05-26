python3 -m venv env  
source env/bin/activate 
python3 -m pip install Django
django-admin startproject settings . 
python3 manage.py startapp app

pip install channels
pip freeze > requirements.txt
pip install -r requirements.txt

pip install channels_redis
pip install django-redis

redis-cli

redis-cli ping
# Output: PONG


to check asgi or wsgi
pip install daphne
daphne -b 0.0.0.0 -p 8000 settings.wsgi:application