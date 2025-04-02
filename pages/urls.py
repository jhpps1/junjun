from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('sign-in/', views.sign_in, name='sign_in'),
]
