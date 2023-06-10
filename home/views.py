from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import Contact,Flames
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from Blogger.models import Post
# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<5 or len(phone)<10 or len(content)<10 or len(phone)>13:
            messages.error(request, 'Please Enter The Correct Details')

        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, 'Thanks For Your Valuable Openion')

    return render(request, 'home/contact.html')
    
def about(request):
    return render(request, 'home/about.html')


def search(request):
    query = request.GET['query']
    if len(query)>100:
        allPost = Post.objects.none()
        messages.error(request, ' Too Long.........')
    else:
        allPostTitle = Post.objects.filter(title__icontains=query)
        allPostContent = Post.objects.filter(content__icontains=query)
        allPostAuthor = Post.objects.filter(author__icontains=query)
        allPost = allPostTitle.union(allPostContent)
        allPost = allPost.union(allPostAuthor)
    if allPost.count() == 0:
        messages.error(request,'Your query does not found please enter differnt related keyword')
    params ={'allPost':allPost , 'query':query}
    return render(request, 'home/search.html', params)


def handleSingUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        # Checksome
        if len(username)>15:
            messages.error(request, 'Username must be less than 15 character')
            return redirect('home')
        if not username.isalnum():
                messages.error(request, 'Username must be only contain letters and number')
                return redirect('home')
        
        if len(pass1) < 6 or len(pass1) > 15:
            messages.error(request, 'Please enter a password that is between 6 to 15 character')
            return redirect('home')
        if pass1.isalnum():
            messages.error(request, 'please enter a password that contains atleast 1 symbol(ex: @!#$%^&*)')
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, 'Your Password does not match please try again')
            return redirect('home')
        
        

        # create the user
        myuser = User.objects.create_user(username, email , pass1 )
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'Your TechBhaiya account has been created successfully')
        return redirect('/')
    else:
        return HttpResponse('404 Not Found')


def handleLogIn(request):
    if request.method == 'POST':
        logInusername = request.POST['logInusername']
        logInpass = request.POST['logInpass']

        user = authenticate(username=logInusername, password=logInpass)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully Logged In')
            return redirect('home')

        else:
            messages.error(request, 'Your Username and Password doesnot match')
            return redirect('home')
    return HttpResponse('LogIn')
def handleLogOut(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out')
    return redirect('home')
    return HttpResponse('LogOut')

def flames(request):
    if request.method == 'POST':
        name1 = request.POST['name1']
        name2 = request.POST['name2']
        Tryer = name1
        onTry = name2
        name1 = name1.lower()
        name2 = name2.lower()
        name1 = name1.replace(' ',"")
        name2 = name2.replace(' ',"")

        for i in name1:
            for j in name2:
                if i==j:
                    name1 = name1.replace(i,'',1)
                    name2 = name2.replace(j,'',1)
                    break
        count = len(name1+name2)

        if count>0:
            list1 = ['Friends','Lovers','Affectionate','Marriage','Enemies','Siblings']
            while len(list1)>1:
                c = count%len(list1)
                s_index = c-1
                if s_index>=0:
                    left = list1[:s_index]
                    right = list1[s_index+1:]
                    list1 = right+left
                else:
                    list1 = list1[:len(list1)-1]
            s_msg = 'And The Relationship Between Both of You I mean '+Tryer   +" And " +onTry +" is " +list1[0]
            messages.success(request, s_msg)
            print(list1[0])
        flames = Flames(name1=Tryer, name2=onTry)
        flames.save()

    return render(request, 'home/flames.html')
