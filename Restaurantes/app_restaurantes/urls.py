from django.conf.urls import url, include
from django.contrib import admin
from . import views
from views import RestaurantViewSet
from django.views.generic import TemplateView


urlpatterns = [
    # admin page
    url(r'^admin/', admin.site.urls),
    # show index
    url(r'^index$', views.index, name='index'),
    # show index
    url(r'^$', views.index, name='index'),
    # like a restaurant
    url(r'^like_restaurant/$', views.like_restaurant, name='like_restaurant'),
    # api rest
    url(r'^api/$', RestaurantViewSet.as_view(), name='api'),

    url(r'^api_resta/$', views.api_restaurantes, name ="api_restaurantes"),

    url(r'^api_resta/(?P<pk>[a-zA-Z0-9]+)$', views.api_restaurantes_detail, name="api_restaurantes_detail"),

    url(r'^api_propia/$', TemplateView.as_view(template_name='api.html')),  # angular test

]