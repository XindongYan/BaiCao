from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from .models import Employee, upload
from . import models
from django_markdown.widgets import MarkdownWidget
from . import models
import markdown2
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

import hashlib

def md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

def calc_md5(password):
    return md5(password + 'the-Salt')


def index(request):
    from . import models
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']

        psd = md5(password + 'the-Salt')
        re_psd = calc_md5(re_password)

        data = Employee(username= username, email= email, password= psd)
        data.save()

        if psd != re_psd:
            return HttpResponse(u'两次输入不一样')

    all_content = models.upload.objects.all()

    try:
        value = request.COOKIES['username']
        if value:
            return render(request, 'add.html', {'user_list': all_content})


    except:
        return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        password = calc_md5(password)
        data = Employee.objects.get(username=username)

        psd = data.password
        if psd != password:
            return HttpResponse(u'密码不正确')

        print('ok')

        if data:
            response = render(request, 'index.html', {'user_list': data})
            response.set_cookie('username', username)
            return response
        else:
            return HttpResponse(u'无此用户')

def OK(request):
    return render(request, 'upload.html')

def upload(request):
    if request.method =='POST':
        title = request.POST['title']
        content = request.POST['content']

        file = models.upload(title= title, content= content)
        file.save()

    return HttpResponseRedirect('/')


def test(request, page):
    page = int(page)
    data = models.upload.objects.get(id = page)
    content = data.content
    title = data.title
    data = [title, content]
    return render(request, 'test.html', {'data': data})


register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def custom_markdown(value):
    return mark_safe(markdown2.markdown(force_text(value),
            extras=["fenced-code-blocks", "cuddled-lists", "metadata", "tables",
            "spoiler"]))

        # return render(request, 'add.html', {'user_list': data})
# Create your views here.
