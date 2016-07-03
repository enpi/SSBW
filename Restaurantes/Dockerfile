from debian:jessie
maintainer jmgn@correo.ugr.es

# variables de ambiente
#     código (solo lectura)
env project_dir /Restaurantes/
#     datos: MEDIA_ROOT, db.sqlite (lectura y escritura)
env volume_dir /var/Volumes/Restaurantes

run apt-get -y update

# Herramintas para django
run apt-get install -y apt-utils
run apt-get install -y python python-dev python-setuptools

# MongoDB
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10
RUN echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.0 main" | tee /etc/apt/sources.list.d/mongodb-org-3.0.list

# Pip
run apt-get install -y git                                                                                             
run easy_install -U pip    

# Directorio donde instalar la aplicación
add . ${project_dir}
workdir $project_dir

run pip install -r requirements.txt

# PRODUCCION
run pip install gunicorn

# Servidor web y watchdog
run apt-get install -y supervisor nginx

#  configuraciones
run cp  deploy/supervisor.conf /etc/supervisor/conf.d/
run cp  deploy/default /etc/nginx/sites-available/default

run sed -i 's/DEBUG = True/DEBUG= False/' Restaurantes/settings.py

expose 80

RUN chmod +x deploy/collect_static.sh
cmd deploy/collect_static.sh && supervisord
