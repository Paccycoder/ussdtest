from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import africastalking

def Home(request):
    return render(request,'index.html')

api_key = 'bb297ac052df02a35ccc09eb0603b6864209a953a44aa9acee613535f85edce3'
username = 'paccycoder@gmail.com'
africastalking.initialize(username, api_key)



@csrf_exempt
def registerussd(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')  
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')
        response = ""
        if  text == "":
            response = "CON Murakaza neza kurubuga rw'abahinzi Smart Ikigega \n"
            response += "1.iyandikishe \n"
            response += "2.Kugurisha umusaruro \n"
            response += "3.kugura umusaruro \n"
            response += "4.kubika umusaruro\n"
            response += "5.kwishyura umuhinzi\n"
            response += "6.Kuguza amafaranga"
        elif text == "1":
            response = "CON Andika amazina yawe \n"
        print(response)
        return HttpResponse(response)
    return HttpResponse('Thanks for registration')
