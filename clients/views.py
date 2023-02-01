from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect  
from clients.forms import ClientForm  
from clients.models import Client  
from django.template import RequestContext


# Create your views here.  
def clnt(request):  
    if request.method == "POST":  
        form = ClientForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  

    else:    
        form = ClientForm() 
    return render(request, 'index.html', {'form': form})  


def show(request):  
    client = Client.objects.all()  
    return render(request, "show.html", {'clients': client})  


def edit(request, id):  
    client = Client.objects.get(cid=id)  
    return render(request, 'edit.html', {'clients': client})  


def update(request, id):  
    client = Client.objects.get(cid=id)  
    form = ClientForm(request.POST, instance = client)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'clients': client})  


def error(request):
    return redirect('/error')      


def destroy(request, id):  
    client = Client.objects.get(cid=id)  
    client.delete()  
    return redirect("/show")  