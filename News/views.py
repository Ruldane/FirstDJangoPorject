from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import News
from .forms import RegistrationForm, RegistrationModalForm, DocumentForm  # import the class
from .models import RegistrationData
from django.contrib import messages

def home(request):
    # dictionnary for context
    context = {
        # give a context on home.html
        "text": "this if from context",
        "Mynumber" : 54445,
        "fruits": ["Apple", "Banana", "Pear", "Melon"],
        "number" : 100, # using for if statement in home.html
    }
    # Return a HttpResponse whose content is filled with the result of calling
    return render(request,"home.html", context)


def contact(request):
    context =  {
        "sometext" : "this is from context to the contact page", # using in contact.html
        "mylist" : ["Coucou", "c'est moi", "lolo"] # using in contact.html
    }
    # Return a HttpResponse whose content is filled with the result of calling
    return render(request,"contact.html", context)


def about(request):
    context = {}
    return render(request, "about.html", context)

def news_details(request):
    obj = News.objects.get(id=1) # News means the class news in models.py, will take all information about id = 1
    context = {
    "object":obj # give a name to call in the news_details.html
    }
    # Return a HttpResponse whose content is filled with the result of calling
    return render(request, "news_details.html", context)


def news_year(request, year): # Insert the argument year
    a_list = News.objects.filter(pub_date__year = year) # Filter the news from years
    context = {
    'year':year,
    'article_list': a_list
    }
    # Return a HttpResponse whose content is filled with the result of calling
    return render(request, "news_year.html", context)

def register(request):

     # call the form from the file forms.py and the class RegistrationForm
    context = {"form" : RegistrationForm
    }
    # Return a HttpResponse whose content is filled with the result of calling
    return render(request, "registration.html", context)

def addUser (request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
        # call the class RegistrationData on models.py to save into the database
        register = RegistrationData(username = form.cleaned_data['username'], password = form.cleaned_data['password'], email = form.cleaned_data['email'], phone = form.cleaned_data['phone'])
        register.save()
        # add a message with a resquest, type of the message is a success message, the thrid argument is the message at display on the screen
        messages.add_message(request, messages.SUCCESS, "Your have registered Seccessfull")

    # Then redirect to home
    return redirect('add')

def modalformview(request):
    context = {
        'modalform' : RegistrationModalForm
    }
    return render(request, "modalform.html", context)

def addModalForm(request):
    mymodalform= RegistrationModalForm(request.POST, request.FILES)

    if mymodalform.is_valid():
        mymodalform.save()

    return redirect('addmodalform')


def upload(request):
    context = {
        'upload' : DocumentForm
    }
    return render(request, "upload.html", context)

def addFIle(request):
    myfile = DocumentForm(request.POST)
    if myfile.is_valid():
        upload_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(upload_file.name, upload_file)
        myfile.save()
    return redirect('upload')




