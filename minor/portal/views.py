from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
import json
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from . import forms, models, serializers


class DashboardView(View):
    

    def get(self, request):
        mform=forms.ArticleFileForm()
        articles = models.Article.objects.all()
        context = {
            'articles': articles,
            'form': mform,
            
        }
        return render(request, 'index.html', context)

    def post(self, request, **kwargs):
        f = forms.ArticleFileForm(request.POST, request.FILES)
        f.instance.uploaded_by=request.user.person
        if f.is_valid():
            
            f.save()
        else:
            print(f.errors)
        # article=models.Article(uploaded_by=request.user.person, name=articlename, document=document)
        # do something with your data
        del(f)
        context = {
            'form': forms.ArticleFileForm(),
            'articles': models.Article.objects.all()
        }  #  setrequest your context
        return render(request, 'index.html', context)


class ProfileView(View):

    def get(self, request, username='self'):
        if username == 'self':
            user=request.user

        else:
            user=User.objects.get(username=username)
        articles=models.Article.objects.filter(uploaded_by=user.person)

        context={
            'person' : models.Person.objects.get(user=user),
            'articles': articles,
            'followers': user.person.get_followers(),
            'following': user.person.get_following(),
            'favourites': user.person.get_favourites()
        }
        return render(request, 'profile.html', context)


    def post(self, request, **kwargs):
        my_data = request.POST
        print(my_data)
        # do something with your data
        context = {}  #  set your context
        return render(request, 'profile.html', context)

def logoutuser(request):
    logout(request)
    return redirect('login')


def loginuser(request):
    if(request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username + password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('user found')
            return redirect('/')
        else:
            print('not found')
            return render(request, 'login.html')
    return render(request,'login.html')


def registeruser(request):
    return HttpResponse('<h1>register page</h1>')


def support(request):
    return render(request, 'support.html')

@login_required
def articleView(request, id):

    article = models.Article.objects.get(id=id)
    context = {
        'article' : article
    }
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