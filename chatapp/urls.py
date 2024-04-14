# Assuming your app name is 'chatapp'
from django.urls import path
from .views import chatbot_view

urlpatterns = [
    path('chat/', chatbot_view, name='chatbot_view'),
    # Other URL patterns for your application...
]
