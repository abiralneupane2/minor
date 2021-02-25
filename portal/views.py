from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
import json
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from . import forms, models, serializers
from django.urls import reverse


class DashboardView(View):
    def get(self, request):
        mform=forms.ArticleForm()
        fform=forms.ArticleFileForm()
        articles = models.Article.objects.all()
        context = {
            'articles': articles,   #list of all articles
            'form': mform,  #form to add article  
            'fform': fform,
        }
        return render(request, 'index.html', context)

    def post(self, request,*args, **kwargs):
        f = forms.ArticleForm(request.POST)
        a = forms.ArticleFileForm(request.POST, request.FILES)
        f.instance.uploaded_by=request.user.person
        if f.is_valid() and a.is_valid():
            f.save()
            files = request.FILES.getlist('file')
            for file in files:
                models.Files(file=file, article=f.instance).save()
        else:
            print(f.errors)
            print(a.errors)
        del(f)
        context = {
            'form': forms.ArticleForm(),
            'fform': forms.ArticleFileForm(),
            'articles': models.Article.objects.all()
        } 
        return render(request, 'index.html', context)


class ProfileView(View):

    def get(self, request, username='self'):
        
        if username == 'self':
            user=request.user
            userForm = forms.UserEditForm(instance=request.user)
            personForm = forms.ProfileCompleteForm(instance=request.user.person)

        else:
            user=User.objects.get(username=username)
        articles=models.Article.objects.filter(uploaded_by=user.person)

        context={
            'person' : models.Person.objects.get(user=user),
            'articles': articles,
            'followers': user.person.get_followers(),
            'following': user.person.get_following(),
            'favourites': user.person.get_favourites(),
            'form1': userForm,
            'form2': personForm
        }
        return render(request, 'profile.html', context)


    def post(self, request, *args, **kwargs):
        userForm = forms.UserEditForm(request.POST, instance=request.user)
        personForm = forms.ProfileCompleteForm(request.POST, instance=request.user.person)
        userForm.save()
        personForm.save()
        return redirect(reverse('profile'))

def logoutuser(request):
    logout(request)
    return redirect(reverse('login'))


def loginuser(request):
    if(request.method=='POST'):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username  = form.cleaned_data.get("username")
            password  = form.cleaned_data.get("password")
            user = User.objects.get(username=username)
            if user is not None:
                if user.check_password(password):
                    login(request, user)        
                    print('user found')
                    return redirect(reverse('index'))
                return render(request, 'login.html', {'errmsg': "password incorrect", "form": form})
            else:
                print('not found')
                return render(request, 'login.html', {'errmsg': "user not found", "form": form})
        else:
            print(form.errors)
    return render(request,'login.html', {'form': forms.LoginForm()})


def registeruser(request):
    if request.method=="POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user=User(username=form.cleaned_data.get("username"))
            user.set_password(form.cleaned_data.get("password"))
            user.save()
            print(form.cleaned_data.get('full_name'))
            person = models.Person(full_name=form.cleaned_data.get('full_name'), user=user)
            person.save()
            print(person)
            login(request, user)
            return redirect(reverse('index'))
        else:
            print(form.errors)

    return render(request, 'register.html', {'form': forms.RegistrationForm()})


def support(request):
    return render(request, 'support.html')

@login_required
def articleView(request, id):
    article = models.Article.objects.get(id=id)
    if request.method=='POST':
        mform = forms.ArticleForm(request.POST, instance=article)
        fform = forms.ArticleFileForm(request.FILES)
        if mform.is_valid() and fform.is_valid():
            models.Files.objects.filter(article=article).delete()
            mform.save()
            files = request.FILES.getlist('file')
            for file in files:
                models.Files(file=file, article=mform.instance).save()
                
    
    context = {
        'article' : article,
        'form' : forms.ArticleForm(instance=article),
        'fform' : forms.ArticleFileForm(instance=models.Files.objects.filter(article=article).first())
    }
    print(context)
    return render(request, 'article.html', context)

@login_required
def toggleFavourite(request):
    person = request.user.person
    articleid=request.GET.get('articleid')
    article = models.Article.objects.get(id=articleid)
    try:
        fav = models.Favourite.objects.get(from_person=person, to_article=article)
        print("deleted")
        fav.delete()
        return JsonResponse({'status': 'deleted'})
    except:
        print("created")
        models.Favourite(from_person=person, to_article=article).save()
        return JsonResponse({'status': 'created'})

class Comment(View):
    def post(self, request):
        person = request.user.person
        print(request.body)
        articleid=request.POST.get('articleid')
        comment=request.POST.get('comment')
        article = models.Article.objects.get(id=articleid)
        comment = models.Comment(from_person=person, to_article=article, comment=comment)
        comment.save()
        return HttpResponse(200)

    def delete(self, request):	
        print(request.body)
        body_unicode = request.body.decode('utf-8')
        print(body_unicode)
        id = body_unicode.split('=')[1]
        models.Comment.objects.get(id=id).delete()
        return HttpResponse(200)
