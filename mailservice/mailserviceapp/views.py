import json
import urllib

from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from boto import ses

@api_view(['GET'])
def health(request):
    return HttpResponse(json.dumps({"message": "Success"}), status=status.HTTP_200_OK)

@api_view(['POST'])
def send_email(request):
    try:
        subject = request.data['subject']
        to = request.data['to']
        cc = request.data['cc']
        bcc = request.data['bcc']
        body = request.data['body']
        source = request.data['from']
        conn = ses.connect_to_region('us-east-1')
        conn.send_email(source=source,subject=subject,body=body,to_addresses=to, cc_addresses=cc, bcc_addresses=bcc)
        response_message = "success"
        response_status = status.HTTP_201_CREATED
    except KeyError as key_error:
        response_message = "failed as some parameter was missing in input request  : " + str(key_error)
        response_status = status.HTTP_400_BAD_REQUEST
    return HttpResponse(json.dumps({"message": response_message}), status=response_status)
