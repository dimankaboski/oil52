from django.contrib import admin
from .models import *

# Register your models here.

class GoodAdmin(admin.ModelAdmin):
    list_display = ('name','cat', 'type', 'viscosity','cost')
    
    # class Media:
    #     js = (
    #         '/static/tiny_mce/tiny_mce.js',
    #         '/static/tiny_mce/tiny_mce_init.js',
    #     )
admin.site.register(Category)
admin.site.register(Good, GoodAdmin)
admin.site.register(Orders)