from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.http import require_POST
import re

from blog.forms import SubscribeForm
from .models import Post, Subscribe
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse


@require_POST
def subscribe_email(request):
    email = request.POST.get('email')
    if email:
        if re.match('^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$',email):
            try:
                subobj, created = Subscribe.objects.get_or_create(email=email)
                if created:
                    return JsonResponse({'status': 'ok'})
                else:
                    return JsonResponse({'status': 'nok', "message": "Already Subscribed"})
            except Exception as e:
                return JsonResponse({'status': 'nok', "message": e})
        else:
            return JsonResponse({'status':'nok', "message":'Email not vaild'})
    return JsonResponse({'status': 'nok', "message": "Email Not Found"})


def post_list_view(request):
    list_objects = Post.published.get_queryset()
    #print("----------")
    paginator = Paginator(list_objects, 3)
    #print(request.GET.get('page'))
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
        #print('success')
    except PageNotAnInteger:
        posts = paginator.page(1)
        print('PageNotAnInteger')
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        print('EmptyPage')
    return render(request, 'blog/post/list.html', {'posts': posts})


def save_subs(request):
    SubscribeForm(request.POST).save()

def post_detail_view(request, year, month, day, post):
    submit_f = SubscribeForm()
    post = get_object_or_404(Post, slug=post, publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post, 'submitform': submit_f})

