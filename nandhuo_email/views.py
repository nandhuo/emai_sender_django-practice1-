from django.shortcuts import render
from django.core.mail import send_mail,send_mass_mail
from django.http import HttpResponse
from .models import email
from django.core.mail import EmailMessage


#send_mai,send_mass_mail,EmailMessage for sending mails with attachments.mail has been sent to all the members in database.

# Create your views here.
def home(request):
    #send_mail("first_mail","hai bro,u r doing good keep working","nandhakumar.m.126@gmail.com",["nandhakumar.m.126@gmail.com"],fail_silently=False)
    #print("mail sent")
    if request.method=="POST":
        sender=request.POST["from"]
        receiver=request.POST["to"]
        subject=request.POST["subj"]
        message=request.POST["message"]
        lists=[]
        mail=email(mail=receiver)
        mail.save()
        m=email.objects.all()
        for i in m:
            lists.append(str(i.mail))
        #send_mail(subject,message,sender,lists,fail_silently=False)
        #message1=(subject,message,sender,lists)
        #message2=(subject,message,sender,lists)
        #send_mass_mail((message1,message2),fail_silently=False)
        mail=EmailMessage(subject,message,sender,lists)
        file1=request.FILES["file"]
        mail.attach(file1.name,file1.read(),file1.content_type)
        mail.send()

        print("message sent")
        return HttpResponse("message sent")
        
    return render(request,"send.html")
