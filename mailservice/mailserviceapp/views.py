import json
import urllib

from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def check(request):
    send_mail("test_subject", "test_message", 'aditya.kapoor@codenation.co.in', ['adityakapoor3252@gmail.com'],
              fail_silently=False)
    return HttpResponse(json.dumps({"message": "Success"}), status=status.HTTP_200_OK)

@api_view(['POST'])
def sns_notification(request):
    js = json.loads(request.data.replace('\n', ''))
    if js["Type"] == "SubscriptionConfirmation":
        subscribe_url = js["SubscribeURL"]
        urllib.urlopen(subscribe_url)
    return HttpResponse(json.dumps({"message": "Success"}), status=status.HTTP_200_OK)
