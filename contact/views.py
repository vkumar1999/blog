from django.shortcuts import render
from .models import contactform
def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contactformdata=contactform(name=name,email=email,subject=subject,message=message)
        contactformdata.save()
    return render(request,'contact.html')