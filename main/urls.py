from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('order/', views.order, name='order'),
    path('email/', views.email, name='email'),
    path('motoroil/', views.motoroil, name='motoroil'),
    path('transmission/', views.transmission, name='transmission'),
    path('mototechnic/', views.mototechnic, name='mototechnic'),
    path('technical_liquid/', views.technical_liquid, name='technical_liquid'),
    path('lubricants/', views.lubricants, name='lubricants'),
    path('good/<int:motoroil_id>', views.motoroil_good, name='motoroil_good'),
    path('getgoods/<cat>', views.getgoods, name='getgoods'),
    path('addtocart/<int:good_id>', views.addtocart, name='addtocart'),
    path('getcart', views.getcart, name='getcart'),
    path('getcartinfo', views.getcartinfo, name='getcartinfo'),
    path('gooddelete/<int:good_id>', views.gooddelete, name='gooddelete'),
    path('changecount/<int:good_id>/<int:good_count>', views.changecount, name='changecount'),
    path('deliver/', views.deliver, name='deliver'),
    path('find', views.search, name='search'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)