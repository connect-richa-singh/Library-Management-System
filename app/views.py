from django.shortcuts import render,redirect
from .models import Book
from .forms import SignUpForm
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
def home(request):
    books=Book.objects.all()
    return render(request, 'home.html',{'books':books})

def librarian_view(request):
    books = books=Book.objects.all()
    return render(request, 'librarian.html',{'books':books})

def member_view(request):
        books=Book.objects.all()
        return render(request, 'member.html',{books:books})


def signup(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['username']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        mem_type = request.POST['mem']
        encyPass =  make_password(pass1)
        user=User.objects.create(username=username,first_name=fname, last_name=lname,password=encyPass)
        if mem_type=='librarian':
               group=Group.objects.get(name='librarian')
               group.user_set.add(user) 
        if mem_type=='member':
               group=Group.objects.get(name='member')
               group.user_set.add(user) 
        
        print(fname,lname,username,pass1,pass2,mem_type)

     
        return render(request, 'signup.html')
    else:
         return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass1']   
        user=authenticate(request,username=username,password=password)
        if(user is not None):
            login(request, user)
            if  request.user.groups.filter(name='librarian').exists():
                return redirect('librarian')
            else:
                return redirect('member')
    else:                         
         return render(request,'home.html')
    
def logout_view(request):
     logout(request)
     return redirect('home')


def savebook(request):
     if request.method == 'POST':
          title = request.POST['title']
          image = request.POST['image']
          status = request.POST['status']
          quantity = request.POST['quantity']
          book = Book(title=title,image=image,status=status,quantity=quantity)
          book.save()
          return redirect('librarian')
     
def deletebook(request,id):
     book=Book.objects.get(id=id)
     book.delete()
     return redirect('librarian')
     
     