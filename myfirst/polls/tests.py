from django.test import TestCase
from django.forms import modelformset_factory

from models import Question 

def name():
    AuthorFormSet = modelformset_factory(Question, fields=('name', 'title'))
    AuthorFormSet = modelformset_factory(Question, exclude=('birth_date',))
    formset = AuthorFormSet()
    print(formset)
    
    #print(user) 
# Create your tests here.
name()