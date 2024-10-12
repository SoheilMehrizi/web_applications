from email.header import Header
from json import JSONEncoder
from xml.dom.minidom import NamedNodeMap
from django.shortcuts import render
from django.http import JsonResponse
import requests
from web.messenger import Pakat_email_sender, nylas_EtoE_Messenger
from web.models import API_KEYs

"""
Project registration view --> PRV
"""
def PRV(request):
    context = {}
    if request.method == "POST":
       #gathering the form's data via POST method
        context["name"]    = request.POST["name"]
        context["co_name"] = request.POST["co_name"]
        context["tendency"]= request.POST["tendency"]
        context["email"]   = request.POST["email"]
        context["phone"]   = request.POST["phone"]
        context["service"] = request.POST["service"]
        #gave the message data to the email_sender function and email_sender_test function(local smtp_server)
        result = nylas_EtoE_Messenger(context)
        #the result if API Fuctionality
        #calling the Tester function
        print("Email Sent successfully")
        print(result)
        if result:
            #returning HTTPResponse Due to the sending status
            return JsonResponse({"status":201},
                                encoder=JSONEncoder,
                                safe= True)
        else:
            return JsonResponse({"status":404},
                                encoder=JSONEncoder,
                                safe= True)
    else:
        services = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #prepairing Options for the dropdown list in the form
        context={"status":200, "service":services}
        #context dictionary will sending to the front and using its content there.
        return render(request, "index.html", context)
        #render the form template