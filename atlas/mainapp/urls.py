# from django.urls import path, include
# from mainapp.views import HomePage,addnew
#
# urlpatterns = [
#
#     path('',HomePage.as_view(), name='index'),
#     path('table/create',addnew,name='create')
#
# ]

from django.contrib import admin
from django.urls import path
from mainapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('addnew',views.addnew),
    # path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update,name='update'),
    path('delete/<int:id>', views.destroy),
]