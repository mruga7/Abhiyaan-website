from django.urls import path
from . import views
app_name="maineventsdaythree"
urlpatterns=[
    path("", views.index, name="index"),
    path("<str:daythree>", views.maineventsdaythree, name="maineventsdaythree"),
    path("<str:daythree>/<str:event>", views.event, name="event"),
]