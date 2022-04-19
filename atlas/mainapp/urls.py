from django.urls import path
from mainapp import views


urlpatterns = [
    path('', views.index,name='index'),
    path('addnew/<int:pk>',views.TableCreateView.as_view()),
    path('update/<int:id>', views.update,name='update'),
    path('delete/<int:id>', views.destroy),
]