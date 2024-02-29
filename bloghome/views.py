from django.shortcuts import render,  redirect
from .models import Blog, Comment, Reply
from django.contrib.auth.models import User
from django.contrib.auth import login as authlogin, authenticate, logout as authlogout
from django.contrib import messages
from . forms import CreateForm



# Create your views here.
def home(request):
    blog = Blog.objects.all()
    context = {
        'blog':blog
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def content(request, id):
    blogcontent = Blog.objects.get(id = id)
    comment = Comment.objects.all().order_by("-id")
    reply = Reply.objects.all()
    content = {
        'blog': blogcontent,
        'comment':comment,
        'reply':reply
    }
    return render(request, 'content.html', content) 

def signup(request):
    user = None
    if request.method == "POST":
        username = request.POST.get("fname")
        #email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "you have successfully loged.")
        return redirect('home')
      
    return render(request, 'signup.html')

def login(request): 
    msg = None
    if request.method == "POST":
        username = request.POST.get("fname")
        #email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate( username=username, password=password)

        if user:
             messages.success(request, "you have successfully loged.")
             authlogin(request, user)
             
        else: 
            messages.error(request, "Invalid Credentials")  
        return redirect('home')
    return render(request, 'login.html')

def logout(request):
    authlogout(request)
    return redirect('login')

def comments(request):
    if request.method == "POST":
        name = request.user
        blog_id = request.POST.get('blogid')
        comment = request.POST.get('comment')
        print(name,blog_id,comment)
        blog = Blog.objects.get(id=blog_id)
        commentc = Comment(name=name, blogparent=blog, Comment=comment, cid = blog_id)
        commentc.save()
        messages.success(request, "comment added ")

    return redirect(f"content/{blog_id}")

def replies(request):
    if request.method == "POST":
        name = request.user.username
        commentparent = request.POST.get('commentparent')
        reply = request.POST.get('reply')
        blog_id = request.POST.get('blogid')
        #print(name, reply, blog_id, commentparent)
        
        comment = Comment.objects.get(id=commentparent)
        reply = Reply(name=name, commentparent=comment, reply=reply)
        reply.save()
        messages.success(request, "your reply was added ")


    return redirect(f"content/{blog_id}")

def searchcontent(request): 
    if request.method == "POST":
        to_search = request.POST.get('search')
        obj = Blog.objects.get(title = to_search)
        id = obj.id
    
    blogcontent = Blog.objects.get(id = id)
    comment = Comment.objects.all().order_by("-id")
    reply = Reply.objects.all()
    content = {
        'blog': blogcontent,
        'comment':comment,
        'reply':reply
    }
    return render(request, 'searchcontent.html', content)

def createblog(request):
    return render(request, 'createblog.html')

def submitblog(request):
    if request.method == "POST":
        name = request.POST.get('name')
        title = request.POST.get('title')
        shortdesc = request.POST.get('shortdesc')
        content = request.POST.get('content')
        image = request.FILES['img']
        blog = Blog(name=name, title=title, short_desc=shortdesc, content=content, thumbnail=image)
        blog.save()
    return redirect('home')
   

#    if request.POST:
#         Frm = CreateForm(request.POST, request.FILES)
#         if Frm.is_valid:
#             Frm.save()
#     else:
#         Frm = CreateForm()
    
#     dict = {
#         'form':Frm
#     }
#     return render(request, 'createblog.html', dict)
