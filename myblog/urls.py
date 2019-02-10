"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import appblog.views
import appQuestion.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', appblog.views.home, name = 'home'),
    path('product/detail/<int:product_id>' , appblog.views.detail, name='detail'),
    path('question/',appQuestion.views.question, name= 'question'),
    path('question/<int:question_id>', appQuestion.views.read_question, name= 'read_question'),
    path('question/write_question', appQuestion.views.write_question, name='write_question'),
    path('question/create', appQuestion.views.create, name = 'create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
