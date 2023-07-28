from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator 
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from .models import Post, Freebie
from .forms import ContactForm


# Create your views here.



def index(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/index.html', {
        'posts': latest_posts
    })


def posts(request):
    posts = Post.objects.all().order_by('-date')
    p = Paginator(posts, 3)
    page = request.GET.get('page')
    blog_posts = p.get_page(page)

    return render(request, 'blog/posts.html', {
        'posts': posts,
        'blog_posts': blog_posts
    })

def single_post(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/single-post.html', {
        'post': identified_post,
    })


def freebies(request):
    free_items = Freebie.objects.all().order_by('-date')
    return render(request, 'blog/freebies.html', {
        'items': free_items,
    })

def single_freebie(request, slug):
    identified_item = get_object_or_404(Freebie, slug=slug)
    return render(request, 'blog/single-freebie.html', {
        'item': identified_item,
    })

def about(request):
    return render(request, 'blog/about.html')

def conditions(request):
    return render(request, 'blog/conditions.html')

def privacy(request):
    return render(request, 'blog/privacy.html')

def shop(request):
    return redirect('https://www.etsy.com/shop/Inkflasks')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            subject = "Website Message"
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'subject': form.cleaned_data['subject'],
                'message': form.cleaned_data['message']
            }
            message = '\n'.join(body.values())

            try:
                send_mail(subject, message, 'contact@inkflasks.com', ['contact@inkflasks.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return redirect('blog/index.html')

    else:
        form = ContactForm()

    return render(request, 'blog/contact.html', {
        'form': form,
    })

