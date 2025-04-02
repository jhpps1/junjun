from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.sign_in, name='sign_in'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
]
