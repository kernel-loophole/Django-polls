
import django
import polls
from django.core.mail import send_mail
from reportlab.lib.units import inch
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from django.views import View
from django.db.models import F,Q
from django import forms
from django import template
from django.http import HttpResponse, response
from django.http import HttpResponseRedirect
from polls.models import Blog, Entry, Question,Choice,booking,test,artist,user,uploadfile
from django.template import loader
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .forms import user_form,name_user,user,createuser
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import authenticate, login
from .forms import UploadFileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
@login_required
@permission_required('polls.index')
# Imaginary function to handle an uploaded file.
def register(request):
    form=createuser()
    if request.method=='POST':
        form=createuser(request.POST)
        if form.is_valid():
            messages.success(request,'user has created')
            form.save()


    content={'form':form}
    return render(request,'polls/register.html',content)

def loginpage(request):
  
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            text={}
            return render(request,'polls/index.html',{})
    content={}
    return render(request,'polls/login.html',content)

def upload_file(request):#view to upload file 
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'upload.html',{})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form':form})


def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
# Redirect to a success page.
    else:
        return HttpResponse("invlid")


class myview(View):
    def get(self,request):
        return HttpResponse("this is class base views")
    def get1(self,request):
        return HttpResponse("another class view")
def make_pdf(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)
    data=user.objects.all()

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(25, 25,"hello boy")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

def text_maker(request):#make the dynimical text base files
    response=HttpResponse(content_type="text/plain")
    response['Content-Disposition']='attachment; filename=this.txt'
    lines=user.objects.all()
    response.writelines(lines)
    return response
def bar(request):#search function for the search froms
    if request.method=="POST":
        searched=request.POST['searched']
        selecter=user.objects.filter(name__contain=searched)
        return render(request,'polls/bar.html',{'searched':searched},{'selecter':selecter})
    else:
        return render(request,'polls/bar.html',{})

def froms_re(request):
    template=loader.get_template('polls/forms.html')
    return HttpResponse(template,request)
def all_events(request):
    x=booking.objects.all()
    return render(request,'polls/events.html',{'x':x})

def page(request):
    return response('this is another page')
def get_name(request):

    form = name_user()
    template=loader.get_template('polls/detail.html')
    return HttpResponse('thanks for next page form django')


def index(request):
    #output=list()
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    #for q in latest_question_list:
     #   output.append(q.question_text)
    #re=','.join(output)
    #return HttpResponse(re)
   # return HttpResponse(response)
    contact_list = user.objects.all()
    paginator = Paginator(contact_list, 2) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    #return render(request, 'list.html', {'page_obj': page_obj})
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    list_booking=user.objects.all()
    bookes=artist.objects.all()
    bloger_test=Entry.objects.filter(number_of_comments__gt=F('number_of_pingbacks'))
    #tester=user.objects.filter(name="ali")#for filtter the query
    #tester=user.objects.filter(name__contains="zain")#feild lookups-----> seee also istartswith and iendswith 
    #tester=user.objects.filter(name__contains="zain")#exclude the thing that no match
    template = loader.get_template('polls/index.html')
    ander=Entry.objects.filter(Q( number_of_pingbacks=90) | Q(number_of_comments='200'))
    context = {
        'latest_question_list': latest_question_list,#extract data from database
    
        'list_booking':list_booking,
        'bookes':bookes,
        'page_obj':page_obj,
        'bloger_test':bloger_test,
        'ander':ander
    }
    #return render(request,'polls/detail.html')
    return HttpResponse(template.render(context, request)) 
def test(request):

    if request.method=='POST':
        form=user_form(request.POST)
        if form.is_valid():
                
            form.save()
            return HttpResponse(request,'thanks')
    
    else: 
        return render(request,'replace.html',{})
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
def te():
    return HttpResponse("thanks to url")

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    return HttpResponse("You're voting on question %s." % question_id)