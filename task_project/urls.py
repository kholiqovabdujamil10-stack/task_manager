from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create_task/', create_task, name='create_task'),
    path('show_task/', show_task, name='my_task'),
    path('update_task/<int:id>/', update_task, name='update_task'),
    path('delete_task/<int:id>/', delete_task, name='delete_task'),
    path('complete_task/<int:id>/', complete_task, name='complete_task'),
]
