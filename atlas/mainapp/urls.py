from django.urls import path, include
from mainapp.views import HomePage

urlpatterns = [

    path('',HomePage.as_view(), name='index')

]
