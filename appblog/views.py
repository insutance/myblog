from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def home(request):
    home = Blog.objects
    return render(request, 'home.html', {'home' : home})

def detail(request, product_id):
    product_detail = get_object_or_404(Blog, pk = product_id)
    return render(request, 'detail.html', {'product_detail': product_detail})