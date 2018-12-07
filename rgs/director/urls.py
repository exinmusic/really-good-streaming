from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('upload_media', views.model_form_upload),
]