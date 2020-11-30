from django.urls import path
from . import views
app_name="maineventsdaytwo"
urlpatterns=[
    path("", views.index, name="index"),
    path("<str:daytwo>", views.maineventsdaytwo, name="maineventsdaytwo"),
    path("<str:daytwo>/<str:event>", views.event, name="event"),
]