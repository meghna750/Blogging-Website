from django.shortcuts import render , get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm , UserChangeForm , PasswordChangeForm
from django.contrib.auth.views import  PasswordChangeView
from django.urls import reverse_lazy 
from .forms import SignUpForm , EditProfileForm , PasswordChangingForm , ProfilePageForm
from yourblog.models import profile
# Create your views here.
class CreateProfilePageView(CreateView): 
    model= profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'
    # fields= '__all__'
    def form_valid(self , form): 
        form.instance.user = self.request.user 
        return super().form_valid(form)

class ShowProfilePageView(DetailView): 
    model=profile 
    form_class= ProfilePageForm
    template_name='registration/user_profile.html'
    def get_context_data(self,*args,**kwargs):
        users=profile.objects.all() # it had only one obj - name, so we can call all () here
        context=super(ShowProfilePageView,self).get_context_data()
        page_user= get_object_or_404(profile,id=self.kwargs['pk'])
        context["page_user"]=page_user
        return context

class EditProfilePageView(generic.UpdateView): 
    model =profile
    template_name='registration/edit_profile_page.html'
    fields=['bio','profile_pic','website_url','fb_url','linkedin_url' , 'twitter_url']
    success_url=reverse_lazy('home')
class UserRegisterView(generic.CreateView): 
    form_class= SignUpForm
    template_name= 'registration/register.html'
    success_url=reverse_lazy('login')

class UserEditView(generic.UpdateView): 
    form_class= EditProfileForm
    template_name= 'registration/edit_profile.html'
    success_url=reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView): 
    form_class= PasswordChangingForm
    # form_class= PasswordChangeForm
    success_url= reverse_lazy('password_success')
    # success_url= reverse_lazy('home')

def password_success(request):
    return render(request, 'registration/password_success.html',{}) 
