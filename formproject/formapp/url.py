
from django.conf.urls import url
from .import views
urlpatterns = [
    url(r'^f1/',views.index1),
    url(r'^f2/', views.Create),
    url(r'^f3/', views.read),
    url(r'^f4/', views.Updete),
    url(r'^f5/', views.delete),
    url(r'^f6/', views.createsong),
    
]
