from django.conf import urls
from django.conf.urls import url
from django.contrib import admin
from django.http.response import HttpResponse
from django.urls.conf import include, re_path
from polls.forms import name_user
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from polls.views import loginpage, my_view, myview, register, upload_file
from polls.views import all_events, bar, froms_re, get_name, make_pdf, page, text_maker
app_name = 'polls'


extra_pattern=[
    path('te',views.te,name='te')

]
urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='polls/login.html')),
    path('index', views.index, name='index'),
   path('login',views.loginpage,name='login'),
   path('register',views.register,name='register'),
    path('about',myview.as_view()),
    path('upload',views.upload_file,name='upload'),
    path('name',views.get_name,name='name'),
   
    path('make_pdf',views.make_pdf,name='make_pdf'),
    path('text_maker',views.text_maker,name='text_maker'),
    path('test',views.test,name='test'),
    path('bar',views.bar,name='bar'),
    path('form',views.froms_re,name='form'),
    path('event',views.all_events,name='event-list'),
    path('page',views.page,name='page'),
     path('<int:question_id>/', views.detail, name='detail'),
     path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    
]
