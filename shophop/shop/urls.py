from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ShopHome'),
    path('about/', views.about, name='AboutUs'),
    path('contact/', views.contact, name='ContactUs'),
    path('tracker/', views.tracker, name='TrackingStatus'),
    path('search/', views.search, name='search'),
    path('products/<int:myid>', views.productview, name='productview'),
    path('checkout/', views.checkout, name='checkout'),
    path('handlerequest/', views.handlerequest, name='HandleRequest'),
]
