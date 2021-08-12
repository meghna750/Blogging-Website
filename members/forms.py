from django.contrib.auth.forms import UserCreationForm , UserChangeForm , PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from yourblog.models import profile 

class ProfilePageForm(forms.ModelForm): 
    class Meta:
        model =profile
        fields= ('bio' , 'profile_pic' ,'website_url' , 'insta_url' , 'fb_url', 'twitter_url' , 'linkedin_url')
    
        widgets = {
            'bio':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Your Bio'}),
            # 'profile_pic':forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Your Blog Title tag'}),
            'website_url':forms.TextInput(attrs={'class':'form-control'}),
            'insta_url':forms.TextInput(attrs={'class':'form-control'}),
            'fb_url':forms.TextInput(attrs={'class':'form-control' , 'placeholder':'your fb url'}),
            'twitter_url':forms.TextInput(attrs={'class':'form-control','placeholder':'Your twitter url'}),
            'linkedin_url':forms.TextInput(attrs={'class':'form-control','placeholder':'Your linkedin url'}),
        }

class SignUpForm(UserCreationForm): 
    email =forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name= forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name= forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta: 
        model = User
        fields=('username', 'first_name' ,'last_name','email', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'

class EditProfileForm(UserChangeForm): 
    email =forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name= forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name= forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username= forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # last_login= forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_superuser= forms.CharField(max_length=50, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_staff = forms.CharField(max_length=50, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_active = forms.CharField(max_length=50, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # is_staff = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta: 
        model = User
        fields=('username', 'first_name' ,'last_name','email','password', 'is_superuser','is_staff' ,'is_active')

class PasswordChangingForm(PasswordChangeForm): 
    old_password =forms.CharField(max_length=50 ,widget=forms.PasswordInput(attrs={'class': 'form-control' , 'type':'password'}))
    new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))

    class Meta: 
        model = User
        fields=('old_password' , 'new_password1' , 'new_password2')