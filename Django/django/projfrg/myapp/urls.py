from django.urls import path
from .views import *
urlpatterns = [
    path('', login_view, name='register'),
    # path('secure_page/', secure_page, name='secure_page'),
    path('logout/', logout_view, name='logout'),
    # path('capture/', login_view, name ='image_captured' )
]
