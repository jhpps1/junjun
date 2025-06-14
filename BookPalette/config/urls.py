from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')), 
    path('api/accounts/', include('accounts.urls')), 
    path('api/community/', include('community.urls')), 
]