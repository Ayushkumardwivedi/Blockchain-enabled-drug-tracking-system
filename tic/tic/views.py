from django.http import HttpResponse
from django.shortcuts import redirect, render
from . import views
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt

@login_required
def test_view(request):
    return render(request, 'test.html')


def welcome_view(request):
    return render(request, 'welcome.html')

def rfid_detector(request):
    return render(request, 'rfid.html')


@csrf_exempt 
def my_button_view(request):
    if request.method == 'POST':
        return HttpResponse("Signal Sent.")
    return HttpResponse("Only POST requests are allowed.")
