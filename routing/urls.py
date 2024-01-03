from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("create_user",views.create_user,name="create_user"),
    path('show_user/<pk>', views.show_user, name='show_user'),
    path('edit_user/<pk>', views.edit_user, name='edit_user'),
    path('delete_user/<pk>', views.delete_user, name='delete_user')
]