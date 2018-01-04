# Preparatory steps:
* Change the directory for DB to adjust
* Change STATIC_URL and STATIC_ROOT in settings.py

#Steps:
* Create directory sites
* git pull from directory source that is inside the sites
* start virtualenv in ../virtualenv
* install library needed pip install -r requirements.txt 
* manage.py migrate for DB
* collectstatic for static file
* set DEBUG=FALSE & ALLOWED_HOSTS
* restart gunicorn
