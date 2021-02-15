from django.urls import path
from repeater import views

urlpatterns = [
    path('<str:name>/<int:times>', views.repeat, name='repeat')
]
