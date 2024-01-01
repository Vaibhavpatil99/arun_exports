from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib import messages

from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate

import json
import random

from django.shortcuts import redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail

from django.db.models import *
# Create your views here.

from django.shortcuts import render

import uuid
from django.conf import settings
def about_us(request):
    return render(request, 'about.html')



def contact_us(request):
    return render(request, 'contact-us.html')


def home(request):
    # return HttpResponse("<h1>Page was found</h1>")
    return render(request, 'index.html')


    # if 'name' in request.session:
    #     request.session.modified = True
    #     data = Products.objects.all()
    #     # return JsonResponse(data, safe=False)
    # else:
    #     response = redirect('login')
    #     return response



def registration(request):
    # frm = RegistrationForm(request.POST)
    # if frm.is_valid():
    #     nm = frm.cleaned_data['username']
    #     pw = frm.cleaned_data['password']
    #     em = frm.cleaned_data['email']

        # if User.objects.filter(username = nm).first():
        #     messages.error(request, "This username is already taken")
        #     return render(request, 'register.html')
        # reg = User.objects.create_user(username=nm, password=pw, email=em)
        # reg.save()
        # return render(request, 'login.html',{'form':frm})
    # else:
    #     frm = RegistrationForm()
    #     return render(request, 'register.html',{'form':frm})


    if request.method == 'POST':
        print("Register")
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username = username).first():
            error_message = "This username is already taken"
            print("This username is already taken")
            return render(request, 'register.html', {'error_message': error_message})
        
        if User.objects.filter(email = email).first():
            # messages.error(request, "This Email already exists")
            error_message = "This Email already exists"
            print("This Email already exists")
            return render(request, 'register.html', {'error_message': error_message})
        print(username, email, password )

        reg = User.objects.create_user(username=username, password=password, email=email)
        reg.save()
        return redirect('/login/')
    else:
        # frm = RegistrationForm()
        return render(request, 'register.html')
    



def login(request):
    Users=User.objects.all()
    print(Users)
    if request.method == 'POST':
        username = request.POST.get("username")
        # email = request.POST.get("email")
        password = request.POST.get("password")

        # Validate username and password
        # print(username, password, Users[3].password ,"data")

        # user = authenticate(username = username, password = password)
        user = authenticate(username = username, password = password)
        print(user, "email")
        if user is not None:
            print("ok")
            auth.login(request, user)
            request.session['name'] = 'OkaySession'
            return redirect('/')
        else:
            print("not ok")
            error_message = "Invalid username or password."
        
        return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')


def forgotPassword(request):
    Users=User.objects.all()
    if request.method == 'POST':
        email = request.POST.get("email")
        
        if not User.objects.filter(email = email).first():
            print("No user found with this email.")
            error_message = "No user found with this email."
            # messages.error(request, "No user found with this email")
            return render(request, 'login.html',{'error_message': error_message})
        
        user_obj = User.objects.get(username="patilvb")
        token = str(uuid.uuid4())
        print("User_obj",user_obj)
        # profile_obj = Profile.objects.get(user=user_obj)
        # profile_obj.forgot_password_token = token
        # profile_obj.save()

        try:
            # Attempt to get the profile object
            profile_obj = Profile.objects.get(user=user_obj)
        except Profile.DoesNotExist:
            # If the profile doesn't exist, create a new one
            profile_obj = Profile(user=user_obj)
            profile_obj.save()

        # Update the forgot_password_token and save the profile object
        profile_obj.forgot_password_token = token
        profile_obj.save()

        subject = "Your Forget Password Link"
        message = f'Hi , click on the link to reset your passowrd http://127.0.0.1:8000/change-password/{token}/'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
        # messages.success(request, 'An email is sent.')
        error_message = "An email is sent."
        return render(request, 'login.html', {"error_message" : error_message})
    
    else:
        return render(request, 'login.html')

def changePassword(request, token):
    context = {}
    try:
        profile_obj = Profile.objects.filter(forgot_password_token = token).first()
        context = {'user_id': profile_obj.user.id}
        print(profile_obj)
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            Confirm_password = request.POST.get('Confirm_password')
            user_id = request.POST.get('user_id')
            print(new_password)
            if user_id is None:
                messages.success(request, 'No user id found')
                return redirect(f'/change-password/{token}/')
            
            if new_password != Confirm_password:
                messages.success(request, 'New Password and Confirm Password both should be same')
                return redirect(f'/change-password/{token}/')

            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            print("Password changed successfully")
            return redirect('/login/')
            
    except Exception as e:
        print(e)
    return render(request, 'changePassword.html', context)
    

def logout(request):
    auth.logout(request)
    return redirect('/login/')


def browse(request):
    return render(request, 'browse.html')

def addProducts(request):

    data = Products.objects.all()
    if 'name' in request.session:
        request.session.modified = True
        if request.user.is_superuser:
            if request.method == 'POST':
                print(request.POST)
                name = request.POST.get('name')
                description = request.POST.get('description')
                product_code = request.POST.get('productCode')
                category = request.POST.get('category')
                subcategory = request.POST.get('subcategory')
                images = request.FILES.getlist('image')



                if Products.objects.filter(product_code=product_code).exists():
                    print("Product code already exists.")
                    messages.error(request, "Product code already exists.")
                    return render(request, 'addProduct.html', {'data': data})

                product = Products.objects.create(name=name, desc=description, category=category.replace('_', ' '), subcategory=subcategory, product_code=product_code)

                for image in images:
                    Image.objects.create(product=product, image=image)

                specifications = []
                for i in range(1, 6):  # Adjust the range based on the number of added specifications
                    specHeader = request.POST.get(f'specification_header_{i}')
                    specDescription = request.POST.get(f'specification_description_{i}')
                    if specHeader and description:
                        # specifications.append({'header': header, 'description': specDescription})
                        specification = Specification.objects.create(header=specHeader, description=specDescription)
                        specifications.append(specification)

                print("specifications", specifications,Products)
                for specification in specifications:
                    product.specifications.add(specification)


                return render(request, 'addProduct.html', {'data': data})

            else:
                return render(request, 'addProduct.html', {'data': data})
        else:
            return render(request, 'pageNotAvailable.html')
    else:
        response = redirect('login')
        return response
        






def products(request):
    data = Products.objects.all()
    print(data)

    if len(data) >= 3:
        # Randomly pick 3 items from the queryset
        random_data_items = random.sample(list(data), 3)
    else:
        # If there are fewer than 3 items, just use all items
        random_data_items = data


    return render(request, 'products.html', {'data': data, 'random_data_items': random_data_items})

def jsonProductdata(request):
    products = list(Products.objects.all())
    data = {
        'products': [
            {
                'id': product.id,
                'name': product.name,
                'desc': product.desc,
                'category': product.category,
                'subcategory': product.subcategory,
                'product_code': product.product_code,
                'image': product.images.first().image.url if product.images.first() else None
            }
            for product in products
        ]
    }
    return JsonResponse(data, safe=False)

def product(request, id):
    data = Products.objects.filter(id=id)
    # print(data, "sjufhi")

    # for product in data:
    #     print(product.img.split(','))
    #     product.image_paths = product.img.split(',')
    return render(request, 'product.html', {'data': data})


def deleteProduct(request, product_id):
    product = Products.objects.get(id=product_id)
    product.delete()
    return redirect('addProduct')



def enquirySubmit(request, product_id):
    product = Products.objects.get(id=product_id)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        country_code = request.POST.get('country_code')
        contact_no = request.POST.get('contact_no')
        message = request.POST.get('message')
        contact_number = country_code+contact_no
        Name = first_name + ' ' + last_name
        print("Data:",first_name, last_name, email, contact_number)

        messages.info(request, 'Enquiry getting submitted...')
        print('Enquiry not submitted successfully')
        subject = 'Enquiry from {}'.format(first_name)
        email_body = 'Name: {}\nEmail: {}\ncontact_number: {}\nMessage: {}\nProduct Name: {}\nProduct Description: {}'.format(Name, email,contact_number, message, product.name, product.desc)
        send_mail(subject, email_body, 'patilvb1999@gmail.com', ['patilvb1999@gmail.com'])

        user_subject = 'Enquiry Confirmation'
        user_email_body = 'Dear {},\n\nThank you for your enquiry. We will get back to you shortly.'.format(first_name)
        send_mail(user_subject, user_email_body, 'sender@example.com', [email])

        enquiry = Enquiry(name=Name, email=email, contact_no=contact_number, message=message, product=product)
        enquiry.save()

        # messages.success(request, 'Enquiry submitted successfully.')
        print('Enquiry submitted successfully')
        return JsonResponse({'message': 'Enquiry submitted successfully.'})
    else:
        return render(request, 'product.html')

    
def all_products(request):

    print("defhksuihfi")
    data = Products.objects.all()
    return render(request, 'all_products.html', {'data': data})

    
    
def all_products_cat(request, category):

    print("categoryhhh")
    data = Products.objects.all()
    print(category.replace('_', ' '), "iiii")
    filterCategory = Products.objects.filter(category= category.replace('_', ' ')).all()
    print(category, data, filterCategory)
    return render(request, 'all_products.html', {'data': filterCategory})

    
def all_products_search(request):

    query = request.GET.get('query', '')
    products = Products.objects.filter(Q(name__icontains=query) | Q(category__icontains=query) | Q(subcategory__icontains=query))
    print(products)
    return render(request, 'all_products.html', {'data': products})

    
def all_products_cat_pro(request, category, product):

    print("category, product")
    data = Products.objects.all()
    filterData = Products.objects.filter(category=category.replace('_', ' '), subcategory=product.replace('_', ' ')).all()
    print(category.replace('_', ' '), product.replace('_', ' '), data, filterData)
    return render(request, 'all_products.html', {'data': filterData})

    
def enquiries(request):
    if 'name' in request.session:
        request.session.modified = True
        if request.user.is_superuser:
            enquiries = Enquiry.objects.all()
            return render(request, 'enquiries.html', {'enquiries': enquiries})
        else:
            return render(request, 'pageNotAvailable.html')
    else:
        response = redirect('login')
        return response
    

def access_management(request):
    if 'name' in request.session:
        request.session.modified = True
        if request.user.is_superuser:
            allUsers = User.objects.all()
            return render(request, 'access_management.html', {'allUsers': allUsers})
        else:
            return render(request, 'pageNotAvailable.html')
    else:
        response = redirect('login')
        return response
    
def toggle_superuser(request, user_id):
    user = User.objects.get(pk=user_id)
    print(user, user_id, "super")
    user.is_superuser = not user.is_superuser
    user.save()
    # return JsonResponse({'status': 'success'})
    response = redirect('access_management')
    return response