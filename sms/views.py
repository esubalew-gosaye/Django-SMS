from django.http import HttpResponse
from django.shortcuts import render
import requests as req
import json

username = 'mesaye'
password = 'mesaye'
to = '0942443926'
message = 'This is a test message from TeleHakim project @mesayem'

def index(request):
    url = f"http://192.168.0.91:8080/SendSMS?username={username}&password={password}&phone={to}&message={message}"
    response = req.request("GET", url).json()
    print(response)
    return HttpResponse(response.get('message'))
