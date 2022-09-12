from django.contrib.auth import models
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
import json
from django.contrib.auth import logout
from django.contrib.auth.models import User 
from .models import Fieldview,SubFieldView,UploadedFile
# Create your views here.
def homePage(request):
    fields=Fieldview.objects.all()
    param={"Fields":fields}
    return render(request,'homePage.html',param)
def SignOut(request):
    logout(request)
    messages.success(request,"Successfully Logout")
    return redirect('/')
def selectPage(request,mode_select):
    
    sub_field=SubFieldView.objects.filter(category_field=mode_select)
    if (mode_select=='VEHICLE'):
        category='VEHICLE'
        link={'VEHICLE':'http://www.transport.mp.gov.in/'}
        
    elif(mode_select=='IDENTITY'):
        category='IDENTITY'
        link={'AADHAR CARD':'https://uidai.gov.in/','AYUSHMAN CARD':'https://pmjay.gov.in/',
        'PAN CARD':'https://www.myutiitsl.com/PAN_ONLINE/ePANCard','VOTER ID':'https://voterportal.eci.gov.in/'}
        
    elif(mode_select=='ACADEMIC'):
        category='ACADEMIC'
        link={'STATE BOARD MARKSHEET':'https://mpbse.mponline.gov.in/Portal/Examinations/MPBSE/marksheet_prov2_input.aspx'
        ,'CBSE MARKSHEET':'www.cbseresults.nic.in'}
       
    elif(mode_select=='APPLICATION-PROOFS'):
        category="APPLICATION-PROOFS"
        link={'ALL CERTIFICATES':'http://mpedistrict.gov.in/MPL/Home.aspx'}
    else:
        category='None'
        link={'OTHERS':'PLEASE CONTACT TO YOUR NEARER SERVICES CENTERS'}
    print(mode_select,category)    
    param={'sub_field':sub_field,'select':mode_select,'link':link,'category':category}
    return render(request,'docCardView.html',param)
def uploadPreview(request,doc_select):
    if request.method == 'POST':
        username=request.user.username
        category=doc_select
        doc_title=request.POST.getlist('docTitle[]')
        files=request.FILES.getlist('file[]')
        
        for i in range(len(doc_title)):
            doc_title1=doc_title[i]
            files1=files[i]
            upload=UploadedFile(username=username,category=category,doc_title=doc_title1,doc_image=files1)
            upload.save()

        messages.success(request,"Successfully uploaded")
        param={'selective_mode':doc_select}
        # return render(request,'homePage.html',param)
        return redirect('/digiapp/')

    else:
        username=request.user.username
        data=UploadedFile.objects.filter(username=username,category=doc_select)
      
        param={'selective_mode':doc_select,'data':data}
        return render(request,'docUploadShow.html',param)
def deleteFile(request,texts):
    username=request.user.username
    data=UploadedFile.objects.filter(username=username,doc_title=texts)
    data.delete()
    return redirect('/digiapp/')
def Addbucket(request):
    field_name="homeDocumnets"
    field_image="hjkkf;agi/jpg"
    field_select="home papers"
    data={'field_name':field_name,"field_image":field_image,"field_select":field_select}
    upload=Fieldview(data)
    upload.save()
    return redirect('/digiap/')