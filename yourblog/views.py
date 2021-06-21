from django.shortcuts import render
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from .models import Post , Category
from.forms import PostForm,EditForm
from django.urls import reverse_lazy


# Create your views here.
class HomeView(ListView): 
    model=Post
    template_name='home.html'
    # ordering= ['-id']
    ordering= ['-post_date']
    def get_context_data(self,*args,**kwargs):
        cat_menu=Category.objects.all() # it had only one obj - name, so we can call all () here
        context=super(HomeView,self).get_context_data()
        context["cat_menu"]=cat_menu
        return context

def CategoryView(request,cats):
    category_posts= Post.objects.filter(category=cats.replace('-',' '))
    return render(request, 'categories.html',{'cats':cats.title().replace('-',' '), 'category_posts': category_posts})

def CategoryListView(request):
    cat_menu_list=Category.objects.all()
    return render(request, 'category_list.html',{ 'category_menu_list': cat_menu_list})


class ArticleDetailView(DetailView): 
    model=Post
    template_name='blogDetail.html'
    def get_context_data(self,*args,**kwargs):
        cat_menu=Category.objects.all() # it had only one obj - name, so we can call all () here
        context=super(ArticleDetailView,self).get_context_data()
        context["cat_menu"]=cat_menu
        return context

class AddPostView(CreateView): 
    model=Post 
    form_class=PostForm
    template_name='add_post.html'
    # fields= '__all__'
    # fields= ('title','author','title_tag','body')
    def get_context_data(self,*args,**kwargs):
        cat_menu=Category.objects.all() # it had only one obj - name, so we can call all () here
        context=super(AddPostView,self).get_context_data()
        context["cat_menu"]=cat_menu
        return context

class AddCategoryView(CreateView): 
    model=Category 
    # form_class=PostForm
    template_name='add_category.html'
    fields= '__all__'
    def get_context_data(self,*args,**kwargs):
        cat_menu=Category.objects.all() # it had only one obj - name, so we can call all () here
        context=super(AddCategoryView,self).get_context_data()
        context["cat_menu"]=cat_menu
        return context

class UpdatePostView(UpdateView):  
    model=Post
    template_name='update_post.html'
    # form_class=PostForm------this will give an uption to update all fields
    # fields=('title','title_tag','body')
    form_class=EditForm
    def get_context_data(self,*args,**kwargs):
        cat_menu=Category.objects.all() # it had only one obj - name, so we can call all () here
        context=super(UpdatePostView,self).get_context_data()
        context["cat_menu"]=cat_menu
        return context

class DeletePostView(DeleteView): 
    model=Post
    template_name='delete_post.html'
    success_url=reverse_lazy('home')
    def get_context_data(self,*args,**kwargs):
        cat_menu=Category.objects.all() # it had only one obj - name, so we can call all () here
        context=super(DeletePostView,self).get_context_data()
        context["cat_menu"]=cat_menu
        return context
