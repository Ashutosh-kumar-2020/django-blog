from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Contact
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def contact(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        issue_type = request.POST['issue_type']
        desc = request.POST['desc']

        if name == "" or email == "" or issue_type == "" or desc == "":
            messages.error(request, 'Please fill the form correctly')
        else:
            contact = Contact(name=name, email=email, issue_type=issue_type, desc=desc)

            contact.save()

    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def search(request):
    query=request.GET['query']
    allPosts= Post.objects.filter(title__icontains=query)
            
    params={
            'allPosts': allPosts,
            'query': query
            }

    return render(request, 'home/search.html', params)

def HandleSignUp(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        username = request.POST.get("username")
        email = request.POST.get("email")

        pass1 = request.POST.get("password")
        pass2 = request.POST.get("confirm_password")

        #  validate the user
        # 1. Check username length and alpha numeric
        if(len(username) > 20 or len(username) < 2):
            messages.error(request, 'Please choose a username between 2 to 20 characters')
            print(f"\n Please choose a username between 2 to 20 characters \n")
            return redirect("/")

        elif not username.isalnum():
             messages.error(request, 'Please choose a alpha numeric username')
             print(f"\n Please choose a alpha numeric username \n")
             return redirect("/")

        # check password
        elif(pass1 != pass2):
            messages.error(request, 'Your password deos not match confirm password.')
            print(f"\n Your password deos not match confirm password. \n")

            return redirect("/")

        elif(len(pass1) <= 2):
                messages.error(request, 'Your password is too short atleast choose 3 charecters.')
                print(f"\n Your password is too short atleast choose 3 charecters. \n")

                return redirect("/")

        else:
            #create user
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, "Your account has been successfully created")
            print(f"\n Success : Your account has been successfully created \n")
            redirect("/")
    
    else:
        messages.error(request, 'You are not allowed on that page')
        print(f"\n You are not allowed on signup page \n")
        return redirect("/")

def HandleLogIn(request):
    if request.method == "POST":
        login_username = request.POST.get("login_username")
        login_password = request.POST.get("login_password")
        current_loc = request.POST.get("current_loc")

        user = authenticate(username=login_username, password=login_password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfuly logged in !")
            print(f"\n {current_loc} \n")
            return redirect(current_loc)

        else:
             messages.error(request, "Invalid username or password !")
             return redirect(current_loc)

    else:
        messages.error(request, 'You are not allowed on that page')
        return redirect("/")


def HandleLogOut(request):
      logout(request)
      messages.success(request, "Successfully logged out")
      return redirect('home')
      
       

