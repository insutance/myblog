from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    home = Blog.objects
    home_list = Blog.objects.all()
    paginator = Paginator(home_list,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'home' : home, 'posts':posts})

def detail(request, product_id):
    product_detail = get_object_or_404(Blog, pk = product_id)
    return render(request, 'detail.html', {'product_detail': product_detail})