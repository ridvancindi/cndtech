from django.shortcuts import get_object_or_404, redirect, render

from contents.forms import *
from django.utils.translation import get_language, activate, gettext
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from taggit.models import Tag
# Create your views here.
def eskiindex(request):
    models = Maincontent.objects.filter(lang_id = get_language())
    category = Category.objects.all()
    tags = Tag.objects.all()
    post = []
    for person in Maincontent.objects.order_by('?')[0:4]:
        post.append(person)
    trans = translate(language='tr')
    context = {
        "models":models,
        'trans': trans,
        'category' :category,
        'post':post,
        'tags':tags,
    } 
    return render(request,"index.html",context)
def detail(request,url):
    article = get_object_or_404(Maincontent,url = url)
    meta_tags =article.meta_tag.split(",")
    category = Category.objects.all()
    tags = Tag.objects.all()
    all = []
    for person in Maincontent.objects.order_by('?')[0:6]:
        all.append(person)
    context = {
        "article":article,
        'category' :category,
        'allpost':all,
        'tags':tags,
        "metatag" : meta_tags
    } 
    #article = Article.objects.filter(id = id).first()   
    return render(request,"detail.html",context)
def index(request):  
    models = Maincontent.objects.filter(lang_id = get_language(),situation= 1)
    category = Category.objects.all()
    tags = Tag.objects.all()
    all = []
    for person in Maincontent.objects.order_by('?')[0:6]:
        all.append(person)
    context = {
        "models":models,
        'category' :category,
        'allpost':all,
        'tags':tags,
        
    } 
    return render(request,"index.html",context)
def categorypage(request,cat):  
    models = Maincontent.objects.filter(category = cat,situation= 1)
    category = Category.objects.all()
    tags = Tag.objects.all()
    all = []
    for person in Maincontent.objects.order_by('?')[0:6]:
        all.append(person)
    context = {
        "models":models,
        'category' :category,
        'allpost':all,
        'tags':tags,
    } 
    return render(request,"index.html",context)
def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('hello')
    finally:
        activate(cur_language)
    return text
@login_required(login_url = "/")
def edit(request):
    form = PostContent()
    if form.is_valid():
        editmoney =form.save(commit=False)
        editmoney.save()
        messages.success(request,"Başarıyla Düzenlendi")
        return redirect("/")
    return render(request,"form.html",{"form":form})