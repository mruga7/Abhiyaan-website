from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    days=MainDayThree.objects.all()[0]
    day=Daythree.objects.all()
    
    return render(request, "maineventsdaythree/index.html", {
        "days": days,
        "day":day,
        "departmentalfests": ["CSE", "IT", "EXTC", "ME", "CE"],
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })

def maineventsdaythree(request, daythree):
    oday=Daythree.objects.all()
    days=MainDayThree.objects.all()
    tday=Daythree.objects.get(name=daythree)
    events=Event.objects.all()

    return render(request, "maineventsdaythree/maineventsdaythree.html", {
        "days": days,
        "day": oday,
        "tday":tday,
        "events": events,
        "departmentalfests": ["CSE", "IT", "EXTC", "ME", "CE"],
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })

def event(request, daythree, event):
    days=MainDayThree.objects.all()[0]
    oday=Daythree.objects.all()
    tday=Daythree.objects.get(name=daythree)
    events=Event.objects.all()
    tevent=Daythree.objects.get(name=daythree).events.get(name=event)
    
    return render(request, "home/event.html", {
        "days": days,
        "day": oday,
        "tday": tday,
        "events": events,
        "event": tevent,
        "departmentalfests": ["CSE", "IT", "EXTC", "ME", "CE"],
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })