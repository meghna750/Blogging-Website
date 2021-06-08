from django.shortcuts import render
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from.forms import PostForm,EditForm
from django.urls import reverse_lazy


# Create your views here.
class HomeView(ListView): 
    model=Post
    template_name='home.html'
    # ordering= ['-id']
    ordering= ['-post_date']


class ArticleDetailView(DetailView): 
    model=Post
    template_name='blogDetail.html'

class AddPostView(CreateView): 
    model=Post 
    form_class=PostForm
    template_name='add_post.html'
    # fields= '__all__'
    # fields= ('title','author','title_tag','body')

class UpdatePostView(UpdateView):  
    model=Post
    template_name='update_post.html'
    # form_class=PostForm------this will give an uption to update all fields
    # fields=('title','title_tag','body')
    form_class=EditForm

class DeletePostView(DeleteView): 
    model=Post
    template_name='delete_post.html'
    success_url=reverse_lazy('home')
