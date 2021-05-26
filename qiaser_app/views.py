from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.http import request
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.shortcuts import render
from.models import *
from . forms import BookForm , CategoryForm,AdminLoginForm, OrderForm

# Create your views here.

def admin_login(request):
    forms = AdminLoginForm()
    if request.method == 'POST':
        forms = AdminLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
    context = {'forms': forms}
    return render(request, 'pages/login.html', context)



def index(request):

    if request.method =='POST':
        add_book =BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()

        add_Category=CategoryForm(request.POST)
        if add_Category.is_valid():
             add_Category.save()


    context ={
        'Category': Category.objects.all(),
        'books':Book.objects.all(),
        'form':BookForm(),
        'formcat':CategoryForm(),
        'allbooks':Book.objects.filter(acvtie=True).count(),
        'booksold':Book.objects.filter(status='sold').count(),
        'bookrented':Book.objects.filter(status='rented').count(),
        'bookavailble':Book.objects.filter(status='available').count(),
        
        
    }
    return render(request,'pages/index.html',context)
def books(request):
    search=Book.objects.all()
    title= None
    if 'search_name'  in request.GET:
        title =request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)


    context ={
    'Category': Category.objects.all(),
    'books':search,
    }

    return render(request,'pages/books.html',context)
def update(request , id):
    book_id =Book.objects.get(id=id)
    if request.method == 'POST':
        book_save = BookForm(request.POST ,request.FILES , instance = book_id)
        if book_save.is_valid():
            book_save.save()
            return  redirect('index')
    else:
        book_save = BookForm(instance=book_id)
    context ={
        'form':book_save,
    }
    return render(request,'pages/update.html',context)

def delete(request , id):
    book_delete =get_object_or_404(Book ,id=id)
    if request.method =='POST':
        book_delete.delete()
        return redirect('/')
    return render(request, 'pages/delete.html')


def about(request):


    return render(request,'pages/about.html')

def Admin(request):
    return render

def orderdata(request):
    context={

        'order':Order.objects.all(),
    }


    return render(request,'pages/orderdata.html',context)


    
    

    

def order(request):

    if request.method =='POST':
        order_book =OrderForm(request.POST, request.FILES)
        if order_book.is_valid():
            order_book.save()
            return  redirect('books')

      
    
            




    context ={
        'the_first_name_of_clint': Order.objects.all(),
        'the_last_name_of_clint':Order.objects.all(),
        'forms':OrderForm(),
        'the_number_phone_of_clint':Order.objects.all(),
        'the_Email_of_clint':Order.objects.all(),
        'the_address_of_clint':Order.objects.all(),
        'the_city_of_clint':Order.objects.all(),
        'the_name_of_book':Order.objects.all(),
        
    }
    return render(request,'pages/orders.html',context)

