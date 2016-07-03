#/bin/bash
cp -r static/ /var/www/static

# Start MongoDB
/usr/bin/mongod &

# Start Nginx
service nginx start

# Populate MongoBD
/usr/bin/python populate.py

# Start gunicorn
/usr/local/bin/gunicorn Restaurantes.wsgi:application --bind 0.0.0.0:8000
