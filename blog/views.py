from django.shortcuts import render,HttpResponse
from blog.models import Blog
import math 

# Create your views here.
def Home(request):
    return render(request, 'index.html')
def blog_home(request):
    page = request.GET.get('page', 1)
    page = int(page)
    no_of_post = 3
    
    blog = Blog.objects.all()
    length = len(blog)
    total_pages = math.ceil(length / no_of_post)
    
    blog = blog[(page-1)*no_of_post: page*no_of_post]
    
    prev = page - 1 if page > 1 else None
    nxt = page + 1 if page < total_pages else None
    
    context = {
        'blog': blog, 
        'prev': f'?page={prev}' if prev else None,
        'nxt': f'?page={nxt}' if nxt else None,
        'current_page': page,
        'total_pages': total_pages
    }
    return render(request, 'bloag_home.html', context)

def blogpost(request,slug):
    blog = Blog.objects.filter(slug=slug).first() 
    context = {'blog': blog}
    return render(request, 'blogpost.html',context)
    
def contact(request):
    return render(request, 'contact.html')
def search(request):
    return render(request, 'search.html')
