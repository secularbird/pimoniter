from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient
import json


# Create your views here.
def index(request):
    return render(request, "index.html", {})


def data(request):
    response_data = {}
    response_data['result'] = 'error'
    response_data['message'] = 'Some error message'
    return HttpResponse(json.dumps(response_data), content_type="application/json")
