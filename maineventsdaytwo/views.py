from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    days=MainDayTwo.objects.all()[0]
    day=Daytwo.objects.all()
    
    return render(request, "maineventsdaytwo/index.html", {
        "days": days,
        "day":day,
        "departmentalfests": ["CSE", "IT", "EXTC", "ME", "CE"],
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })

def maineventsdaytwo(request, daytwo):
    oday=Daytwo.objects.all()
    days=MainDayTwo.objects.all()
    tday=Daytwo.objects.get(name=daytwo)
    events=Event.objects.all()

    return render(request, "maineventsdaytwo/maineventsdaytwo.html", {
        "days": days,
        "day": oday,
        "tday":tday,
        "events": events,
        "departmentalfests": ["CSE", "IT", "EXTC", "ME", "CE"],
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })

def event(request, daytwo, event):
    days=MainDayTwo.objects.all()[0]
    oday=Daytwo.objects.all()
    tday=Daytwo.objects.get(name=daytwo)
    events=Event.objects.all()
    tevent=Daytwo.objects.get(name=daytwo).events.get(name=event)
    
    return render(request, "home/event.html", {
        "days": days,
        "day": oday,
        "tday": tday,
        "events": events,
        "event": tevent,
        "departmentalfests": ["CSE", "IT", "EXTC", "ME", "CE"],
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })