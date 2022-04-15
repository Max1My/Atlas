from django.urls import path
from authapp.views import RegisterUser,LoginUser,logout


app_name = 'authapp'

urlpatterns = [
    path('login/', LoginUser.as_view(),name='login'),
    # path('profile/',ProfileFormView.as_view(),name='profile'),
    path('logout/',logout,name='logout'),
    path('register/', RegisterUser.as_view(), name='register')
]