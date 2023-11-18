from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from blog.models import Blog
from .forms import Blogform,ContactBlogModel
# Create your views here.

def index(request):
    queryset = Blog.objects.all()
    dic = {
        "posts":queryset
    }
    return render(request,'index.html',dic)

# def contact(request):
#     if request.method == "POST":
#         form = Contactform(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data.get("name")
#             email = form.cleaned_data.get("email")
#             content = form.cleaned_data.get("content")
#             print(name,email,content)
#     else:
#         form = Contactform()

#     dic = {"form": form}
#     return render(request,"contact.html",dic)

def contact(request):
    form = ContactBlogModel()
    if request.method == "POST":
        form = ContactBlogModel(request.POST)
        if form.is_valid():
            form.save()
            form = ContactBlogModel()
        else:
            form = ContactBlogModel()
    
    dic = {
        "form":form
        }
    return render(request,"contact.html",dic)

def form_create(request):
    form = Blogform(request.POST)
    if form.is_valid():
        form.save()
        form = Blogform()
    dic = {
        "form" : form
        
    }
    return render(request,'blog_create.html',dic)

def detail_view(request,my_id):
    obj = get_object_or_404(Blog,pk=my_id)
    #obj = Blog.objects.get(pk=my_id)
    dic = {
        "object":obj
    }
    return render(request,"detail.html",dic)

def arch_blog_list(request):
    queryset = Blog.objects.all()
    dic = {
        "objects":queryset
    }
    return render(request,"archive.html",dic)

def delete_post(request,my_id):
    dic = {}
    obj = get_object_or_404(Blog,pk=my_id)
    if request.method == "POST":
        obj.delete()
        HttpResponseRedirect("/")
    return render(request,"delete_post.html",dic)

