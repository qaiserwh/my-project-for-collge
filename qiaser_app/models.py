from django.contrib.admin.filters import SimpleListFilter

from django.db import models

# Create your models here.

class Category(models.Model):
    name =models.CharField(max_length=200, db_index=True)





    def __str__(Self):
        return Self. name


class Book(models.Model):
    status_book=[
        ('available' ,'available'),
        
        ('sold','sold')
    ]




    title =models.CharField(max_length=250)
    auther =models.CharField(max_length=250, null=True,blank=True)
    photo =models.ImageField(upload_to='photos',null=True,blank=True)
    photo_auther =models.ImageField(upload_to='photos',null=True,blank=True)
    pages =models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True ,blank=True)
    acvtie =models.BooleanField(default=True)
    status =models.CharField(max_length=50,choices=status_book)
    Category =models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    
    

    def __str__(self):
        return self.title

        
class Order(models.Model):
    the_name_of_clint=models.CharField(max_length=50)
    the_number_phone_of_clint=models.CharField(max_length=155)
    the_Email_of_clint=models.EmailField()
    the_address_of_clint=models.CharField(max_length=50)
    the_city_of_clint=models.CharField(max_length=50)
    the_name_of_book=models.ForeignKey(Book, on_delete=models.PROTECT, null=True, blank=True)
    
    
    def __str__(self):
         return self.the_name_of_clint