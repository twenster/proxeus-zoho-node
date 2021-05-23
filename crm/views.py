import json
from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime

# zoho connect
from . import zohoconnect

# zoho CRM
from . import zohocrm

# Proxeus mandatory URL.
def close(request):
    render(request, 'base.html', {})

def config(request):
    render(request, 'base.html', {})

def health(request):
    return render(request, 'base.html', None)

def next(request):
    print(request.body.decode("utf-8"))
    if request.body.decode("utf-8") != "":
        json_data = json.loads(request.body.decode("utf-8"))

        zcrm_module = json_data["module"]
        zcrm_field_api = json_data

        zohoconnect.SDKInitializer.initialize()
        recordDict = zohocrm.Record.search_records(request, zcrm_module, zcrm_field_api)
        print(recordDict)
        return JsonResponse(recordDict)

    return JsonResponse({})

def remove(request):
    render(request, 'base.html', {})

