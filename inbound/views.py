from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from users.models import Users
from twilio.twiml.messaging_response import MessagingResponse


@csrf_exempt
def inbound(request):
    number = request.POST.get('From')
    messageBody = request.POST.get('Body')
    user_number = number[9:]

    #search number in database
    qnumber = list(Users.objects.filter(phone_number=user_number))
     
    # evaluate phone number search results
    if len(qnumber) == 1:
        if qnumber.name == None:
            response = MessagingResponse()
            response.message("""
        *what's your name?*
        """)

        else:
            response = MessagingResponse()
            response.message("""
        *We are ready please send us your receipt in form of an image/photo*
        """)



    
    elif len(qnumber) == 0:
        response = MessagingResponse()
        response.message("""
        *Hey Buddy!* 😀
        Welcome *{user_number}* . This is team savanna geeks, we are glad you are here.
        *what's your name?*
        """
        )