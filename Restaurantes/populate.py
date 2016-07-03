import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Restaurantes.settings')

import django
django.setup()

from app_restaurantes.models import Restaurante

def populate():
    addRestaurante("Patatas Miguel", "Restaurante muy flama.", "http://cdn5.sportadictos.com/wp-content/blogs.dir/29/files/2013/02/2776256262_3214b28b85_z-400x300.jpg")
    addRestaurante("Comidas Cristobal", "Si no te gusta, es lo que hay.", "http://www.cocinasana.com/wp-content/uploads/2013/11/sopa-de-lentejas-400x300.jpg")
    addRestaurante("Pollos hermanos", "Simplemente sublimes.", "http://cdn.kiwilimon.com/recetaimagen/23104/thumb400x300-15767.jpg")

def addRestaurante(name, description, image):
    res = Restaurante()
    res.name = name
    res.description = description
    res.image = image
    res.likes = 0
    res.save()
    return res

if __name__ == "__main__":
    populate()

