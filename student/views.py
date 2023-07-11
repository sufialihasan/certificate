from django.shortcuts import render,redirect

from .models import store


# Create your views here.
def home(request):
    return render(request, 'home.html')


def search(request):
    return render(request, 'search.html')


def safe(request):
    if request.method == 'POST':
        name = request.POST['nm']
        email = request.POST['em']
        certificate = request.POST['add']
        radio = request.POST['gen']
        password = request.POST['pw']
        if store(name=name, email=email, certificate=certificate, gender=radio, password=password):
            if store.objects.filter(certificate=certificate):
                return render(request,'home.html',{'msg':'This Certificate No. is Already Exist'})
            else:
                store(name=name, email=email, certificate=certificate, gender=radio, password=password).save()
                msg = "SUBMITTED SUCCESSFUL"
                return render(request, 'home.html', {'msg': msg})
        else:
            msg ="Please Fill Detail"
        return render(request, 'home.html', {'msg': msg})

def update(request):
    return render(request, 'update.html')


def update_data(request):
    if request.method == 'POST':
        name = request.POST['nm']
        email = request.POST['em']
        certificate = request.POST['add']
        password = request.POST['pw']
        store.objects.filter(email=email).update(name=name, certificate=certificate, password=password)
        msg = "Update Done"
        return render(request, 'update.html', {'msg': msg})

def delete(request):
    return render(request, 'delete.html')

def dell(request):
    if request.method == 'POST':
        certificate = request.POST['add']
        store.objects.filter(certificate=certificate).delete()
        msg = "Delete Done"
        return render(request, 'delete.html', {'msg': msg})


def fetch(request):
    if request.method == 'POST':
        certificate = request.POST['add']
        if store.objects.filter(certificate=certificate):
            data = store.objects.filter(certificate=certificate).all()
            return render(request, 'search.html', {'data': data})
        else:
            msg = "Data Not Find"
            return render(request, 'search.html', {'msg': msg})

def signin(request):
    return render(request,'signin.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['em']
        password=request.POST['pw']
        if store.objects.filter(email=email):
            if store.objects.filter(password=password):
                #request.session['user'] = email
                return redirect('home')
            else:
                msg = "Invalid Password"
                return render(request, 'signin.html', {'msg': msg})
        else:
            msg = "Invalid Email Id"
            return render(request, 'signin.html', {'msg': msg})

def prof(request):
    return render(request,'profile.html')

def profile(request):
    email = request.session['user']
    data = store.objects.filter(email=email).all()
    return render(request,'profile.html',{'data':data})

def show(request):
    return render(request, 'show.html')

def showw(request):
    email = request.session['user']
    data = store.objects.filter(email=email).all()
    return render(request,'show.html',{'data':data})

def record(request):
    data = store.objects.all()
    return render(request,'record.html',{'data':data})