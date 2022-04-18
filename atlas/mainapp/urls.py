from django.urls import path, include
from mainapp.views import HomePage,create

urlpatterns = [

    path('',HomePage.as_view(), name='index'),
    path('user/<int:pk>/table/create',create,name='create')

]
