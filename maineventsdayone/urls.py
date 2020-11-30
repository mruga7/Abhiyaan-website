from django.urls import path
from . import views
app_name="maineventsdayone"
urlpatterns=[
    path("", views.index, name="index"),
    path("<str:dayone>", views.maineventsdayone, name="maineventsdayone"),
    path("<str:dayone>/<str:event>", views.event, name="event"),
]