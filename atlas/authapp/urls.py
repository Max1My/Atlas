from django.urls import path
from authapp.views import RegisterUser


app_name = 'authapp'

urlpatterns = [
    # path('login/', LoginListView.as_view(),name='login'),
    # path('register/',RegisterListView.as_view(),name='register'),
    # path('profile/',ProfileFormView.as_view(),name='profile'),
    # path('logout/',Logout.as_view(),name='logout'),
    path('register/', RegisterUser.as_view(), name='register')
]