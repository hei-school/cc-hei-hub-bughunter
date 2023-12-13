from django.urls import path
from . import views

urlpatterns = [
    path('', views.FileUploadView.as_view({'get': 'list', 'post' : 'create'}), name='index')
]