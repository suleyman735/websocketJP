python3 -m venv env  
source env/bin/activate 
python3 -m pip install Django
django-admin startproject settings . 
python3 manage.py startapp app

pip install channels