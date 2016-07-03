from mongoengine import *

connect('restaurantes')

# Create your models here.

class Restaurante(Document):
    name = StringField(max_length=120, required=True)
    description = StringField(max_length=500, required=True)
    #image = FileField()
    image = StringField(max_length=500, required=True)
    likes = IntField(default=0, required=True)

class Platos(Document):
    name =  StringField(max_length=120, required=True)
    image = FileField();
    name_restaurant = StringField(max_length=120, required=True)
    prize = FloatField(default=0, required=True)


