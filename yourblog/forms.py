from django import forms
from .models import Post , Category

# categories=[('food recipie', 'food recipie'),('Sports' , 'Sports'),('Fashion' , 'Fashion'),]
choices=Category.objects.all().values_list('name' , 'name')

choice_list=[]
for items in choices: 
    choice_list.append(items)

class PostForm(forms.ModelForm):  
    class Meta: 
        model=Post
        fields=('title','title_tag','author', 'category' ,'body')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Blog Title'}),
            
            'title_tag':forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Your Blog Title tag'}),
            # 'author':forms.Select(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control' , 'value': '' , 'id':'username' ,'type':'hidden'}),

            # 'category':forms.Select(choices= categories ,attrs={'class':'form-control'}),
            'category':forms.Select( choices=choice_list ,attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control','placeholder':'Your Blog Body'}),
        }

class EditForm(forms.ModelForm):  
    class Meta: 
        model=Post
        fields=('title','body')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            
            # 'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            # 'author':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }