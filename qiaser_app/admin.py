from django import forms, shortcuts
from django.contrib import admin
from .models import*
# Register your models here.

class OrderAdmin(admin.ModelAdmin):

    search_fields=['the_name_of_clint','the_number_phone_of_clint','the_Email_of_clint']
    list_display=['the_name_of_clint','the_number_phone_of_clint','the_Email_of_clint','the_address_of_clint','the_city_of_clint','the_name_of_book']
    list_filter=['the_name_of_book']


class BookAdmin(admin.ModelAdmin):
    list_display=['title','auther','price','pages','status','Category']
    list_editable=['auther','price','pages','status','Category']
    search_fields=['title','Category','price','pages']
    list_filter=['Category']



admin.site.site_header ='Site Administration'
admin.site.site_title ='Site Administration'
admin.site.register(Book,BookAdmin)
admin.site.register(Category)
admin.site.register(Order,OrderAdmin)



