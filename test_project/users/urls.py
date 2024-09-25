from django.urls import path
from .views import add_user, user_list


urlpatterns = [
    path('list/', user_list, name='user_list'),
    path('add/', add_user, name='add_user'),
]