from django.urls import path

from . import views
from .views import add_user, user_list, edit_user, delete_user

urlpatterns = [
    path('list/', user_list, name='user_list'),
    path('add/', add_user, name='add_user'),
    path('edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete/<int:user_id>/', views.delete_user, name='delete_user'),
]
