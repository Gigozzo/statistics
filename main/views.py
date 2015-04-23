import json
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic import View
from models import Statistics
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.
# Date.UTC(1970,  9, 18)
def spam(request):
    return HttpResponse(json.dumps(
		map(lambda A: [A.dt, A.spam], Statistics.objects.filter()), cls=DjangoJSONEncoder
	))

def total(request):
    return HttpResponse(json.dumps(
		map(lambda A: [A.dt, A.total], Statistics.objects.filter()), cls=DjangoJSONEncoder
	))

def reverts(request):
    return HttpResponse(json.dumps(
		map(lambda A: [A.dt, A.reverts], Statistics.objects.filter()), cls=DjangoJSONEncoder
	))

def complaints(request):
    return HttpResponse(json.dumps(
		map(lambda A: [A.dt, A.complaints], Statistics.objects.filter()), cls=DjangoJSONEncoder
	))

class StatisticsView(View):
    model = Statistics