from django.shortcuts import render
import test
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<b><center>Elo, tu pierwsza strona napisana przeze mnie.</center></b>")
    #return render(request, 'test2.html')
