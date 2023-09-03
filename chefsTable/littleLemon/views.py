from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu
from datetime import datetime

# Create your views here.
def say_hello(request):
    content = "<html><body><h1> Welcome to little Lemon Project Home Page</html></body></h1>"
    return HttpResponse(content)

def dispaly_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def menu(request):
    text = """<h1 style="color: #F4CE14;"> This is Little lemon again! </h1>"""
    return HttpResponse(text)

def menu_by_id(request, menu_id):
    menu = Menu.objects.get(pk=menu_id)
    #return HttpResponse(f"{menu.menu_item}: Type of {menu.cuisine} cuisine.")
    return render(request, 'menu_card.html', {'menu': menu})

#Path parameter in URL
def pathview(request, name, id):
    return HttpResponse("Name : {} UserID : {}".format(name, id))

#Query parameter in URL
def queryview(request):
    queryName = request.GET['name']
    queryID = request.GET['id']
    return HttpResponse("Name : {} UserID : {}".format(queryName, queryID))

#Body parameter in URL
def showform(request):
    return render(request, "form.html")

def getform(request):
    if request.method == "POST":
        bodyID = request.POST['id']
        bodyName = request.POST['name']
    return HttpResponse("Name : {}  UserID: {}".format(bodyName, bodyID))