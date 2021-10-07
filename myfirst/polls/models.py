from django.core.files import storage
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/home/hiader/Pictures')
class uploadimg(models.Model):
    uploadimg_to=models.ImageField(storage=fs)
class uploadfile(models.Model):
    file_name=models.FileField(storage=fs)
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
class user(models.Model):
    #text_me=models.ForeignKey(Question,on_delete=models.CASCADE)
    email=models.EmailField()
    name=models.CharField(max_length=100 )
    passwd=models.CharField(max_length=200)
    def __str__(self):
        return self.email

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
class test(models.Model):
    test_date=models.CharField(max_length=10)
class booking(models.Model):
    book_name=models.CharField(max_length=200)
    book_isbn=models.CharField(max_length=100)
    aurther=models.CharField(max_length=100)
    book_code=models.IntegerField(max_length=10)
class artist(models.Model):
    book_name=models.CharField(max_length=10)

