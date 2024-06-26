from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserDetailUpdateDeleteView
from user_app.api.views import registration_view, logout_view


urlpatterns = [
    path('api/users/login/', obtain_auth_token, name='login'),
    path('api/users/register/', registration_view, name='register'),
    path('api/users/logout/', logout_view, name='logout'),
    path('api/users/<int:pk>/', UserDetailUpdateDeleteView.as_view(), name='get_user_details'),
]
