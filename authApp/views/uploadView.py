from django.shortcuts import render  
from django.http import HttpResponse  
from functions.functions import handle_uploaded_file  

def post(request):   
    handle_uploaded_file(request.FILES['file'])  
    return HttpResponse("File uploaded successfuly") 