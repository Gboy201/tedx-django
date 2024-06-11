from django.urls import path
from main.views import home, sponsor, submit, team, speakerShow

urlpatterns = [
    path('', home, name='home'),
    path('sponsor/', sponsor, name='sponsor'),
    path('submit/', submit, name='submit'),
    path('team/', team, name='team'),
    path('speaker/', speakerShow, name='speaker')
]