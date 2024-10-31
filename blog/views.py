from django.shortcuts import render, HttpResponse
from blog.models import Blog, Contact  # Import the Contact model correctly
import math 

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

def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first() 
    context = {'blog': blog}
    return render(request, 'blogpost.html', context)

def contact(request):
    if request.method == 'POST':
        # Get form data from POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        description = request.POST.get('desc')

        # Validate that all fields are filled
        if not all([name, email, phone, description]):
            return HttpResponse("All fields are required.", status=400)
        
        # Create a new Contact instance and save it to the database
        contact_instance = Contact(name=name, email=email, phone=phone, desc=description)
        contact_instance.save()  # This inserts the data into the database
        
        
    return render(request, 'contact.html')

def search(request):
    return render(request, 'search.html')
