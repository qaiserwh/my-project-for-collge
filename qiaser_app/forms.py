from django import forms
from . models import Book , Category, Order



class AdminLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = '__all__'
        fields = ['name']
        widgets={'name':forms.TextInput
        (attrs={'class':'form-control'})
        }


class BookForm(forms.ModelForm):
    class Meta:
        model =Book
        fields =[
            'title',
            'auther',
            'photo',
            'photo_auther',
            'pages',
            'price',
            'status',
            'Category',
            ]


        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'auther':forms.TextInput(attrs={'class':'form-control'}),
            'photo':forms.FileInput(attrs={'class':'form-control'}),
            'photo_auther':forms.FileInput(attrs={'class':'form-control'}),
            'pages':forms.NumberInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model =Order
        fields = '__all__'
        widgets ={
            'the_first_name_of_clint': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'the_Email_of_clint': forms.TextInput(attrs={'class':'form-control', 'placeholder':'E-mail'}),
            'the_number_phone_of_clint': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Mobile No +964  '}),
            'the_address_of_clint': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
            'the_city_of_clint': forms.TextInput(attrs={'class':'form-control', 'placeholder':' city '}),
            'the_name_of_book':forms.Select(attrs={'class':'form-control'}),
        }
        
 
    