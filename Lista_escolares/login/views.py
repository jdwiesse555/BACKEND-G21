from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.

def logeo(request):
    if request.method == 'GET' :
        return render(request,'login.html',{'form': AuthenticationForm})
    else:
        print(request.POST)
        user = authenticate(
            request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'login.html',{'form':AuthenticationForm,'error':'Usuario o password es incorecto'}) 
        else:
            login(request, user)
            return redirect('mostrar_productos')
            
               
      
def Crear_user(request):
    if request.method == 'GET' :
        return render(request,'crear_usuario.html',{'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                return redirect('login') 
            except:
                return render(request,'crear_usuario.html',{'form':UserCreationForm,'error':'Usuario ya existe'})

        else:
            return render(request,'crear_usuario.html',{'form':UserCreationForm,'error':'Password diferentes, deven ser iguales'})


def logout_view(request):
    logout(request) 
    return redirect('') 

def paginainicio(request):
    
    return render(request,'inicio.html') 