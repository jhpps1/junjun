from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.sign_in, name='sign_in'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
]
