from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    # path('register', views.registration, name='reg'),
    # path('login', views.login, name='login'),
    # path('logout', views.logout, name='logout'),
    # path('', views.home, name='index'),
    path('', browse, name='browse'),
    path('about-us/', views.about_us, name='about'),
    path('contact-us/', views.contact_us, name='contact_us'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.registration, name='registration'),
    path('forgot-password/', views.forgotPassword, name='forgotPassword'),
    path('change-password/<token>/', views.changePassword, name='changePassword'),

    path('products/', views.products, name='products'),
    path('product/<id>/', views.product, name='product'),
    path('addProduct/', addProducts, name='addProduct'),
    path('delete-product/<product_id>/', views.deleteProduct, name='deleteProduct'),
    path('jsonProductdata/', views.jsonProductdata, name='jsonProductdata'),

    path('enquirySubmit/<product_id>/', enquirySubmit, name='enquirySubmit'),
    path('enquiries/', enquiries, name='enquiries'),
    
    path('all_products/', all_products, name='all_products'),
    path('search/', all_products_search, name='all_products_search'),
    path('all_products/<category>/', all_products_cat, name='all_products_cat'),
    path('all_products/<category>/<product>/', all_products_cat_pro, name='all_products_cat_pro'),

    path('access_management/', access_management, name='access_management'),
    path('toggle_superuser/<int:user_id>/', toggle_superuser, name='toggle_superuser'),

    # path('product-data', views.productData, name='prod'),
    # path('json-data', views.json_data, name='json_data')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

