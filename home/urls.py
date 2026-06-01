from django.urls import path
from .views import index, contact
from .views import index, contact, custom_logout

urlpatterns = [
    path('', index, name='home'),
    path('contact/', contact, name='contact'),
    path('logout/', custom_logout, name='custom_logout'),
]