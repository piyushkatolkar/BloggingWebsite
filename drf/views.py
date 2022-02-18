from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from drf.models import post

# blog post code 
# display all post in this blog
@login_required(login_url='login')
def blog(request):
    allposts = post.objects.all()
    # print(allposts)
    context = {'allposts' : allposts}
    return render(request, 'blog.html',context)

# display all users blog post in this blog
@login_required(login_url='login')
def blogPost(request, slug):
    Post = post.objects.filter(slug=slug).first()
    # print(Post)  
    context = {'Post':Post}
    return render(request, 'blogPost.html', context)

# add blog
@login_required(login_url='login')
def add_blog(request):
    if request.method=='POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.POST['author']
        if len(title) > 10:
            messages.error(request, "title must be under 10 characters")
            return redirect('add_blog.html')
        ins = post(title=title, content=content, author=author)
        ins.save()
        return HttpResponse("add_blog.html")
        # print("The data has been return to teh DB")
    else:
        return render(request, 'add_blog.html')

# edit blog
@login_required(login_url='login')
def edit_blog(request):

    return render(request, 'edit_blog.html')

# delete post
@login_required(login_url='login')
def delete_blog(request):
    return render(request, 'delete_blog.html')


# ===============================================================================
# user registration, login, homepage, logout
@login_required(login_url='login')
def index(request):
    return render(request, 'main.html')


# user registration

def handleSignup(request):
    if request.method == 'POST':
        #get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errors inputs
        # username should be under 10 characters
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('/')
        
        # username should be alphanumeric
        if not username.isalnum:
            messages.error(request, "Username should contain letters and numbers")
            return redirect('/')

        # passwords should be match
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('/')

        # create user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account has been success")
        return redirect('login')
    else:
        return render(request, 'register.html')
        messages.success(request, "invalid")


# login user

def adminlogin(request):
    if request.method == 'POST':
        loginusername = request.POST["loginusername"]
        loginpassword = request.POST["loginpassword"]    
        user = authenticate(username=loginusername, password=loginpassword)
        
        # If user is authenticated
        if user is not None:
            login(request, user)    
            messages.success(request, "you are logged in successfully")
            return redirect('/')
        # If user is not authenticated
        else:
            messages.error(request, "Wrong Credentials")

    return render(request, 'login.html')


# User logout

def adminlogout(request):
    logout(request)
    messages.success(request,"Logged out")

    return redirect('login')