from django.shortcuts import render
from .forms import ScrapperForm
from .models import Scrapper
import shutil, os
import PyPDF2 
from django.contrib import messages

def home_view(request):
    if request.method=='POST':
        newfile=Scrapper(resume_file=request.FILES['document'])
        newfile.save()
        print(newfile.resume_file.name) #name of file getting downloaded
        res1="/home/nidhisha/Desktop/django_projects/document_scrapper/doc_scrap_project/doc_scrap_project/"
        res2=newfile.resume_file.name
        name=res1+res2
        print(name)
        res=PyPDF2.PdfFileReader(name) 
        print(res.getPage(0).extractText())
        messages.info(request, res.getPage(0).extractText())
    return render(request, 'home.html')

# Create your views here.
# def home_view(request):
#     form = ScrapperForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
#         form=ScrapperForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'home.html', context)


