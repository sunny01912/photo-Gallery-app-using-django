import django
from django.shortcuts import render
from .models import Category,Photo
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import views
from .forms import LoginForm,SignupForm
from django.contrib.auth import login,authenticate

# Create your views here.
@login_required
def gallery(request):
    category=request.GET.get('category',None)
    categories=Category.objects.filter(user=request.user)
    if category==None:
        photos=Photo.objects.filter(user__username=request.user)
    else:
        photos=Photo.objects.filter(Q(category__name=category) & Q(user__username=request.user))

    context={'categories':categories,'photos':photos}
    return render(request,'photos/gallery.html',context)
@login_required
def viewphoto(request,pk):
    photo=Photo.objects.get(id=pk)
    context={'photo':photo}
    return render(request,'photos/photo.html',context)
@login_required
def addphoto(request):
    user=request.user
    categories=Category.objects.filter(user__username=user)
    context={'categories':categories}
    if request.method=="POST":
        data=request.POST
        image=request.FILES.get('image')
        if data['category'] !='none':
            category=Category.objects.get(Q(id=data['category']) & Q(user=user))
        elif data['createCategory'] != '' :
            category,created=Category.objects.get_or_create(name=data['createCategory'],user=user)
        else:
            category=None
        
        photo=Photo.objects.create(
            category=category,
            img=image,
            description=data['description'],
            user=user
        )

        return HttpResponseRedirect('/')
    return render(request,'photos/add.html',context)

class customLoginView(views.LoginView):
    authentication_form=LoginForm
    template_name='photos/login.html'

def signup(request):
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            user=authenticate(request,username=user,password=form.cleaned_data['password1'])
            login(request,user)
            return HttpResponseRedirect('/')
    form=SignupForm()
    return render(request,'photos/signup.html',{'form':form})

def delphoto(request,pk):
    obj=Photo.objects.get(id=pk)
    obj.delete()
    return HttpResponseRedirect('/')

