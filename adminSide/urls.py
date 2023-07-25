from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    # path('register', views.registration, name='reg'),
    # path('login', views.login, name='login'),
    # path('logout', views.logout, name='logout'),
    path('', views.home, name='index'),
    path('about-us/', views.about_us, name='about'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.registration, name='registration'),
    path('products/', views.products, name='products'),
    path('product/<id>/', views.product, name='product'),
    path('addProduct/', views.addProducts, name='addProduct'),
    path('delete-product/<product_id>/', views.deleteProduct, name='deleteProduct'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('jsonProductdata/', views.jsonProductdata, name='jsonProductdata'),
    path('enquiry-submit/<id>/', enquiry_submit, name='enquiry_submit'),
    path('enquirySubmit/<product_id>/', enquirySubmit, name='enquirySubmit'),

    # path('product-data', views.productData, name='prod'),
    # path('json-data', views.json_data, name='json_data')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

