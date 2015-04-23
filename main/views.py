import json
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic import View
from models import Statistics
from django.core.serializers.json import DjangoJSONEncoder
# from datetime import datetime, date, time
import time
import datetime

# Create your views here.
def spam(request):
	# print datetime.now()
	# print (Statistics.objects.filter()[1]).dt
	# print datetime.strptime((Statistics.objects.filter()[1]).dt, "%Y-%m-%d %H:%M:%S")
	print (Statistics.objects.filter()[1]).dt
	print time.mktime((Statistics.objects.filter()[1]).dt.timetuple())

	return HttpResponse(json.dumps(
		map(lambda A: [time.mktime(A.dt.timetuple()), A.spam], Statistics.objects.filter()), cls=DjangoJSONEncoder
	))

def total(request):
	return HttpResponse(json.dumps(
		map(lambda A: [time.mktime(A.dt.timetuple()), A.total], Statistics.objects.filter()), cls=DjangoJSONEncoder
	))

def reverts(request):
	return HttpResponse(json.dumps(
		map(lambda A: [time.mktime(A.dt.timetuple()), A.reverts], Statistics.objects.filter()), cls=DjangoJSONEncoder
	))

def complaints(request):
	return HttpResponse(json.dumps(
		map(lambda A: [time.mktime(A.dt.timetuple()), A.complaints], Statistics.objects.filter()), cls=DjangoJSONEncoder
	))

class StatisticsView(View):
	model = Statistics