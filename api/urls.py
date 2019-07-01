from django.urls import include, path

from api import views

urlpatterns = [
    
    path('addAdminUser/', views.AddAdminUser, name='AddAdminUser'),
    
]
